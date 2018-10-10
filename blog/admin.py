from django.contrib import admin
from .models import Post, PostComment, Video, VideoComment, Profile, Contact

admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Video)
admin.site.register(VideoComment)
admin.site.register(Profile)
admin.site.register(Contact)
