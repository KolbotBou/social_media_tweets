from django.shortcuts import get_object_or_404, render
from tweets_app.models import UserAccount, Post, PostComment
from django.views import generic

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

# USERACCOUNT MODEL
class UserAccountDetailView(generic.DetailView):
    model = UserAccount

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# POST MODEL
class PostDetailView(generic.DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['caption']

    # Pre-select 'Useraccount' field
    def get_form(self):
        form = super().get_form()
        
        # form.instance.useraccount = self.request.user
        # CODE ABOVE: can be used just like in PostCommentCreateView below
        # Given that Post has Instance 'useraccount=ForeignKey(User)'
        # But, in our Model we have 'useraccount=ForeignKey(UserAccount)'
        # So, 2 Choices -- Either change the FK to (USER), or use below CODE

        form.instance.useraccount = UserAccount.objects.get(user = self.request.user)

        return form

# POSTCOMMENT MODEL
class PostCommentCreateView(LoginRequiredMixin, CreateView):
    model = PostComment
    fields = ['description']

    def get_form(self):
        form = super().get_form()
        
        # Pre-select the 'user' and 'post' fields
        form.instance.useraccount = self.request.user  # Assign logged-in user to the 'user' field

        post = get_object_or_404(Post, pk= self.kwargs.get('pk'))
        form.instance.post = get_object_or_404(Post, pk= post.pk)  # Assign 'post' to the 'post' field

        return form

    # Before the form is submitted, the ForeignKey field is empty 
    # because the user has not selected a Post object yet.
    # So we have to create 'get_context_data' with Pre-Select Post ID to have it rendered before Form Submission
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['selected_post'] = Post.objects.get(id = self.kwargs.get('pk'))

        return context

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs.get('pk')})
