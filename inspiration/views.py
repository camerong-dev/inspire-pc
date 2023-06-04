from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import Post
from .forms import PostForm


class Home(ListView):
    model = Post
    template_name = 'home.html'


class PCDetail(DetailView):
    model = Post
    template_name = 'pc_detail.html'


class AddPC(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_pc.html'
