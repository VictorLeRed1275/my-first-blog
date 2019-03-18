from django import forms

from .models import Post, PostComment, Profile, Contact
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
		
class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', )

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('first_name', 'last_name', 'bio', 'location', 'birth_date','profile_picture',)
		
class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('user', 'topic', 'message')