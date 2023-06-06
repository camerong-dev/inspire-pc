from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
from .filters import HomeFilter


class Home(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = HomeFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PCDetail(DetailView):
    model = Post
    template_name = 'pc_detail.html'


class AddPC(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_pc.html'
