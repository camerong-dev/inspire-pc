from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Post, CpuManufacturerOptions, GpuManufacturerOptions
from .forms import PostForm
from django.core.paginator import Paginator


def CpuManView(request, cpu_man):
    cpu_man_posts = Post.objects.filter(cpu_manufacturer=cpu_man)
    paginator = Paginator(cpu_man_posts, per_page=9)  # Set number of posts per page here
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cpu_man.html', {'cpu_man': cpu_man, 'page_obj': page_obj, 'cpu_man_posts': page_obj})
'''
Data is pulled from the post model after being filtered by a cpu
manufacturer.
'''


def GpuManView(request, gpu_man):
    gpu_man_posts = Post.objects.filter(gpu_manufacturer=gpu_man)
    paginator = Paginator(gpu_man_posts, per_page=9)  # Set number of posts per page here
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gpu_man.html', {'gpu_man': gpu_man, 'page_obj': page_obj, 'gpu_man_posts': page_obj})
'''
Data is pulled from the post model after being filtered by a gpu
manufacturer.  The pagination method is different due to being a function
view, instead of a class view.  
'''


class Home(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 9  # Inherits from ListView
# Pulling data from the post model to display within the home template

    def get_context_data(self, *args, **kwargs):
        cpu_filter_menu = CpuManufacturerOptions.objects.all()
        gpu_filter_menu = GpuManufacturerOptions.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["cpu_filter_menu"] = cpu_filter_menu
        context["gpu_filter_menu"] = gpu_filter_menu
        return context
# Context here is used to display all available manufacturers to filter by


class PCDetail(DetailView):
    model = Post
    template_name = 'pc_detail.html'
# Pulling data from the post model to display within the pc_detail template


class AddPC(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_pc.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

'''
This ensures the author of the post, which is being made, will be automatically
set to the username of the logged in user
'''


class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_pc.html'
    form_class = PostForm