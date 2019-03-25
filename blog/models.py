from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200, help_text='Needs to be short and catchy. A maximum of 200 characters')
	text = models.TextField()
	post_picture = models.ImageField(upload_to='post_pictures/')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class PostComment(models.Model):
	post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	comment = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text
		
class Item(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200, help_text='Needs to be short and catchy. A maximum of 200 characters')
	description = models.TextField()
	item_picture = models.ImageField(upload_to='item_pictures/')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
		
class ItemReview(models.Model):
	item = models.ForeignKey('blog.Item', on_delete=models.CASCADE, related_name='reviews')
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
	review = models.TextField(blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.text
		
def user_pic_dir(instance, filename):
    return 'profile_pictures/user_{0}/{1}'.format(instance.user.id, filename)
	
		
class Profile(models.Model):
	profile_picture = models.ImageField(upload_to=user_pic_dir, default='profile_pictures/user.png')
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30, null=True, blank=True, help_text='A maximum of 30 characters')
	last_name = models.CharField(max_length=30, null=True, blank=True, help_text='A maximum of 30 characters')
	bio = models.TextField(max_length=500, blank=True, help_text='A maximum of 500 characters')
	location = models.CharField(max_length=30, blank=True, help_text='A maximum of 30 characters')
	birth_date = models.DateField(null=True, blank=True, help_text='Format: YYYY-MM-DD.')
	email_list = models.BooleanField(default=True)
	email_confirmed = models.BooleanField(default=False)
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
	
class Cart(models.Model):
	item = models.ForeignKey('blog.Item', on_delete=models.CASCADE, related_name='carts')
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	add_to_cart = models.BooleanField(default=False)
	
class Contact(models.Model):
	email = models.CharField(max_length=254, help_text='Required. Inform a valid email address.')
	name = models.CharField(max_length=30, null=True, blank=True, help_text='Optional')
	message = models.TextField(max_length=1000, help_text='A maximum of 1000 characters')
	published_date = models.DateTimeField(default=timezone.now)