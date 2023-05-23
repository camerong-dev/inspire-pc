from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Post


class Home(ListView):
    model = Post
    template_name = 'home.html'


class PCDetail(DetailView):
    model = Post
    template_name = 'pc_detail.html'


class AddPC(CreateView):
    model = Post
    template_name = 'add_pc.html'
    fields = '__all__'
