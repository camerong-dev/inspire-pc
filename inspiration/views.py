from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post



class Home(ListView):
    template_name = 'home.html'
    template_name = 'home.html'


class AddPC(CreateView):
    model = Post
    template_name = 'add_pc.html'
    fields = '__all__'
