from django import forms

from .models import Post, PostComment, Profile, Contact, Item, ItemReview, Cart
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'post_picture',)
		
class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('comment',)
		
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'description', 'item_picture',)

class ItemReviewForm(forms.ModelForm):
    class Meta:
        model = ItemReview
        fields = ('rating', 'review',)
		
class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', )

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('profile_picture','first_name', 'last_name', 'bio', 'location', 'birth_date','email_list')
		
class CartForm(forms.ModelForm):
	class Meta:
		model = Cart
		fields = ()
	
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email')
		
class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('email', 'name', 'message')