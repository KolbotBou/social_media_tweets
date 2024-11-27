from django.contrib import admin
from tweets_app.models import UserAccount, Post, PostComment

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Post)
admin.site.register(PostComment)