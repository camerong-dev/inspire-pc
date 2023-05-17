from django.shortcuts import render
from django.views import generic
from .models import Post

class Home(generic.ListView):
    model = Post
    template_name = 'home.html'