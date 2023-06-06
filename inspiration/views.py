from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Post, CpuManufacturerOptions, GpuManufacturerOptions
from .forms import PostForm
from django.core.paginator import Paginator


def CpuManView(request, cpu_man):
    cpu_man_posts = Post.objects.filter(cpu_manufacturer=cpu_man)
    return render(request, 'cpu_man.html', {'cpu_man': cpu_man, 'cpu_man_posts': cpu_man_posts})

def GpuManView(request, gpu_man):
    gpu_man_posts = Post.objects.filter(gpu_manufacturer=gpu_man)
    return render(request, 'gpu_man.html', {'gpu_man': gpu_man, 'gpu_man_posts': gpu_man_posts})


class Home(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 9

    def get_context_data(self, *args, **kwargs):
        cpu_filter_menu = CpuManufacturerOptions.objects.all()
        gpu_filter_menu = GpuManufacturerOptions.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["cpu_filter_menu"] = cpu_filter_menu
        context["gpu_filter_menu"] = gpu_filter_menu
        return context


class PCDetail(DetailView):
    model = Post
    template_name = 'pc_detail.html'


class AddPC(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_pc.html'
