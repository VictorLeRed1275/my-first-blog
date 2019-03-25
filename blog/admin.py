from django.contrib import admin
from .models import Post, PostComment, Profile, Contact, Item, ItemReview, Cart

admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Item)
admin.site.register(ItemReview)
admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(Contact)
