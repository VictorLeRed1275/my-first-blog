from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
		
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)

class PostComment(models.Model):
	post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text
		
class Video(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	url = models.URLField()
	title = models.CharField(max_length=200)
	discription = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
	
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)
		
class VideoComment(models.Model):
	video = models.ForeignKey('blog.Video', on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text
		
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
	
TOPIC_CHOICES = (
	('General', 'General enquiry'),
	('Bug', 'Bug report'),
	('Suggestion', 'Suggestion'),
	('Profile', 'Profile'),
	('Security', 'Security'),
	('Other', 'Other'),
)
	
class Contact(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	topic = models.CharField(max_length=30, choices=TOPIC_CHOICES, default=1)
	message = models.TextField(max_length=1000)
	published_date = models.DateTimeField(default=timezone.now)