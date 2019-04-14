from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.db.models import Q
from django.utils import timezone
from .models import Post, PostComment, Profile, Contact
from .forms import PostForm, PostCommentForm, SignUpForm, UserForm, ProfileForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.core.mail import send_mail

from django.contrib.auth.models import User

from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt

from hitcount.models import HitCount
from hitcount.views import HitCountMixin

def error_404_view(request, exception):
    return render(request,'blog/404.html')
	
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			subject = 'Activate Your MySite Account'
			message = render_to_string('blog/account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode,
				'token': account_activation_token.make_token(user),
			})
			email_from = settings.EMAIL_HOST_USER
			print(email_from)
			recipient_list = [user.email,]
			send_mail(subject, message, email_from, recipient_list)
			return redirect('account_activation_sent')
	else:
		form = SignUpForm()
	return render(request, 'reg/signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'blog/account_activation_sent.html')
	
def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')
    else:
        return render(request, 'blog/account_activation_invalid.html')

def home(request):
	posts = []
	count = 0
	hit_count = HitCount.objects.annotate(num_hit=Count('hit')).order_by('-num_hit')
	print(hit_count)
	first_posts = Post.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')
	for post in first_posts:
		if post not in posts:
			if count < 3:
				posts.append(post)
				count += 1
			else:
				break
	return render(request, 'blog/home.html', {'posts': posts})
	
@login_required
def dev_tools(request):
	return render(request, 'blog/development_tools.html')

@login_required
def view_profile(request, pk):
	profile = get_object_or_404(Profile, pk=pk)
	return render(request, 'blog/profile_view.html', {'profile': profile})
	
@login_required
def update_profile(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('profile_view', pk=request.user.pk)
	else:
		user_form = UserForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.profile)
	return render(request, 'blog/profile.html', {
		'user_form': user_form,
		'profile_form': profile_form
	})

def post_list(request):
	post_listing = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
	page = request.GET.get('page', 1)

	paginator = Paginator(post_listing, 10)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	
	return render(request, 'blog/post_list.html', {
		'posts': posts,
	})
	
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	votecount = post.votes.count()
	viewcount = HitCount.objects.get_for_object(post)
	hit_count_response = HitCountMixin.hit_count(request, viewcount)
	if request.method == "POST":
		form = PostCommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.author = request.user
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostCommentForm()
	return render(request, 'blog/post_detail.html', {
		'post': post,
		'form': form,
		'votecount': votecount
	})
	
@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})
	
@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
		return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})
	
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
	
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def post_comment_remove(request, pk):
    comment = get_object_or_404(PostComment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
	
@login_required
def vote_up(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.votes.up(request.user.pk)
	return redirect('post_detail', pk=post.pk)

@login_required
def vote_down(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.votes.down(request.user.pk)
	return redirect('post_detail', pk=post.pk)
	
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ContactForm()
	return render(request, 'blog/contact.html', {'form': form})
	
@login_required
def contact_list(request):
	enquiries = Contact.objects.order_by('published_date')
	return render(request, 'blog/contact_list.html', {'enquiries': enquiries})
	
@login_required
def contact_remove(request, pk):
    enquiry = get_object_or_404(Contact, pk=pk)
    enquiry.delete()
    return redirect('contact_list')