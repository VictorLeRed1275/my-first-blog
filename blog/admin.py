from django.contrib import admin
from .models import Post, PostComment, Profile, Contact

admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Profile)
admin.site.register(Contact)
