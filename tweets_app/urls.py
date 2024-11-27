from django.urls import path
from . import views

urlpatterns = [

    # When a URL is accessed, the Function in the View.py file will be accessed and run
    path('', views.home, name='home'), # Route is Main URL = /home/

]