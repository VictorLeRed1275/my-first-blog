from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Like)
