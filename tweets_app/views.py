from django.shortcuts import render
from tweets_app.models import UserAccount, Post, PostComment
from django.views import generic

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

# USERACCOUNT MODEL
class UserAccountDetailView(generic.DetailView):
    model = UserAccount

# POST MODEL
class PostDetailView(generic.DetailView):
    model = Post
