import datetime
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.urls import reverse
from django.utils import timezone
from hitcount.views import HitCountMixin
from hitcount.models import HitCount

def error_404_view(request, exception):
    return render(request,'blog/404.html')
	
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form': form})

def home(request):
	posts = []
	count = 0
	first_posts = Post.objects.all() # Fix me!!! .order_by('hit_count_generic__hits')
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
	enquiries = Contact.objects.order_by('published_date')
	return render(request, 'blog/development_tools.html', {'enquiries': enquiries})

@login_required
def view_profile(request, pk):
	profile = get_object_or_404(Profile, pk=pk)
	posts = Post.objects.all().prefetch_related('likes').get()
	return render(request, 'blog/profile_view.html', {
		'profile': profile,
		'posts': posts,
	})
	
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
	likes = Like.objects.all()
	post = get_object_or_404(Post, pk=pk)
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
		'likes': likes,
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
def contact_remove(request, pk):
    enquiry = get_object_or_404(Contact, pk=pk)
    enquiry.delete()
    return redirect('contact_list')

@login_required
def liked(user, pk):
    post = Post.objects.get(pk=pk)
    return Like.objects.filter(user=user, post=post).exists()

@login_required
def like(request, pk):
	post = Post.objects.get(pk=pk)
	if not Like.objects.filter(user=request.user, post=post).exists():
		print("True")
		Like.objects.create(user=request.user, post=post, timestamp=timezone.now())
	else:
		print("False")
		Like.objects.filter(user=request.user, post=post).delete()
	return redirect('home')