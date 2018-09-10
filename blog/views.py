from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.db.models import Q
from django.utils import timezone
from .models import Post, PostComment, Video, VideoComment, Profile
from .forms import PostForm, PostCommentForm, VideoCommentForm, VideoForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth import login, authenticate

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
	com = VideoComment.objects.filter(approved_comment=True)
	videos = Video.objects.filter(comments__in=com)
	return render(request, 'blog/home.html', {'videos': videos})
	
def post_search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
			Q(title__icontains=query) |
			Q(author__first_name__icontains=query) |
			Q(author__last_name__icontains=query)
		)
		results = Post.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("blog/post_search.html", {
		'results': results,
		'query': query,
	})
	
def video_search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
			Q(title__icontains=query) |
			Q(author__first_name__icontains=query) |
			Q(author__last_name__icontains=query)
		)
		results = Video.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("blog/video_search.html", {
		'results': results,
		'query': query,
	})
	
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
	
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})
	
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
	
def video_list(request):
	videos = Video.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/video_list.html', {'videos': videos})
	
def video_detail(request, pk):
	video = get_object_or_404(Video, pk=pk)
	return render(request, 'blog/video_detail.html', {'video': video})
	
@login_required
def video_new(request):
	if request.method == "POST":
		form = VideoForm(request.POST)
		if form.is_valid():
			video = form.save(commit=False)
			video.author = request.user
			video.save()
		return redirect('video_detail', pk=video.pk)
	else:
		form = VideoForm()
	return render(request, 'blog/new_video.html', {'form': form})
	
@login_required
def video_edit(request, pk):
	video = get_object_or_404(Video, pk=pk)
	if request.method == "POST":
		form = VideoForm(request.POST, instance=video)
		if form.is_valid():
			video = form.save(commit=False)
			video.author = request.user
			video.save()
		return redirect('video_detail', pk=video.pk)
	else:
		form = VideoForm(instance=video)
	return render(request, 'blog/video_new.html', {'form': form})

@login_required
def video_draft_list(request):
    videos = Video.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/video_draft_list.html', {'videos': videos})

@login_required
def video_publish(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.publish()
    return redirect('video_detail', pk=pk)

@login_required
def video_remove(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.delete()
    return redirect('video_list')
	
@login_required
def add_comment_to_post(request, pk):
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
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
	
@login_required
def add_comment_to_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        form = VideoCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video = video
            comment.save()
            return redirect('video_detail', pk=video.pk)
    else:
        form = VideoCommentForm()
    return render(request, 'blog/add_comment_to_video.html', {'form': form})
	
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
	
@login_required
def video_comment_approve(request, pk):
    comment = get_object_or_404(VideoComment, pk=pk)
    comment.approve()
    return redirect('video_detail', pk=comment.video.pk)

@login_required
def video_comment_remove(request, pk):
    comment = get_object_or_404(VideoComment, pk=pk)
    comment.delete()
    return redirect('video_detail', pk=comment.video.pk)