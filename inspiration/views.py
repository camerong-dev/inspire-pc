from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator


class Home(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 1   


class PCDetail(DetailView):
    model = Post
    template_name = 'pc_detail.html'


class AddPC(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_pc.html'
