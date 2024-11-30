from django.urls import path
from . import views

urlpatterns = [

# HOMEPAGE URL
    path('', views.home, name='home'), # Route is Main URL = /home/

# PROFILE / USERACCOUNT RELATED
    path('useraccount/<int:pk>/', views.UserAccountDetailView.as_view(), name='useraccount_detail'),

# POST RELATED
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = "post_detail"),
    path('post/create/', views.PostCreateView.as_view(), name = 'post-create'),

# POSTCOMMENT RELATED
    path('comment/<int:pk>/create/', views.PostCommentCreateView.as_view(), name='postcomment-create'),

]