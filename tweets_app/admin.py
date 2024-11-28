from django.contrib import admin
from tweets_app.models import UserAccount, Post, PostComment

# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('user','bio')
admin.site.register(UserAccount, UserAccountAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('useraccount', 'post_date', 'caption')
    list_filter = ('useraccount', 'post_date')
admin.site.register(Post, PostAdmin)

class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('useraccount', 'post_date', 'description', 'post')
    list_filter = ('useraccount', 'post_date', 'post')
admin.site.register(PostComment, PostCommentAdmin)