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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
	
def home(request):
	return render(request, 'blog/home.html')
	
@login_required
def update_profile(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('home')
	else:
		user_form = UserForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.profile)
	return render(request, 'blog/profile.html', {
		'user_form': user_form,
		'profile_form': profile_form
	})

def view_profile(request, pk):
	profile = get_object_or_404(Profile, pk=pk)
	return render(request, 'blog/profile_view.html', {'profile': profile})
	
def shop_list(request):
	return render(request, 'blog/shop.html')

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	query = request.GET.get('q', '')
	if query:
		qset = (
			Q(title__icontains=query) |
			Q(text__icontains=query)
		)
		results = Post.objects.filter(qset).distinct()
	else:
		results = []
	return render(request, 'blog/post_list.html', {
		'posts': posts,
		"results": results,
		"query": query
	})
	
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostCommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostCommentForm()
	return render(request, 'blog/post_detail.html', {
		'post': post,
		'form': form,
	})
	
@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
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
		form = PostForm(request.POST, instance=post)
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
def post_comment_approve(request, pk):
    comment = get_object_or_404(PostComment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def post_comment_remove(request, pk):
    comment = get_object_or_404(PostComment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
	
def contact_support(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ContactForm()
	return render(request, 'blog/support.html', {'form': form})
	
@login_required
def enquiry_list(request):
	enquiries = Contact.objects.order_by('published_date')
	return render(request, 'blog/support_list.html', {'enquiries': enquiries})
	
@login_required
def enquiry_remove(request, pk):
    enquiry = get_object_or_404(Contact, pk=pk)
    enquiry.delete()
    return redirect('support_list')