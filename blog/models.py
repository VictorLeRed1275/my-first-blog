from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from vote.models import VoteModel

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.contenttypes.fields import GenericRelation

from hitcount.models import HitCount, HitCountMixin

class Post(VoteModel, models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200, help_text='Needs to be short and catchy. A maximum of 200 characters')
	text = models.TextField()
	hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
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
	email_confirmed = models.BooleanField(default=False)
	
	def __str__(self):
		return self.user
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Contact(models.Model):
	email = models.CharField(max_length=254, help_text='Required. Inform a valid email address.')
	name = models.CharField(max_length=30, null=True, blank=True, help_text='Optional')
	subject = models.CharField(max_length=50, null=True, blank=True, help_text='Optional')
	message = models.TextField(max_length=1000, help_text='A maximum of 1000 characters')
	published_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.email