from django import forms

from .models import Post, PostComment, Video, VideoComment, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
		
class PostCommentForm(forms.ModelForm):

    class Meta:
        model = PostComment
        fields = ('author', 'text',)
		
class VideoCommentForm(forms.ModelForm):

    class Meta:
        model = VideoComment
        fields = ('author', 'text',)
		
class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('url', 'title', 'discription',)
		
class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2', )