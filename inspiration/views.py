from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Post, CpuManufacturerOptions, GpuManufacturerOptions
from .forms import PostForm
from django.core.paginator import Paginator


def SearchView(request):
    return render(request, 'search_result.html')


def CpuManView(request, cpu_man):
    cpu_man_posts = Post.objects.filter(cpu_manufacturer=cpu_man)
    paginator = Paginator(cpu_man_posts, per_page=9)  # Set number of posts per page here
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cpu_man.html', {'cpu_man': cpu_man, 'page_obj': page_obj, 'cpu_man_posts': page_obj})


def GpuManView(request, gpu_man):
    gpu_man_posts = Post.objects.filter(gpu_manufacturer=gpu_man)
    paginator = Paginator(gpu_man_posts, per_page=9)  # Set number of posts per page here
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gpu_man.html', {'gpu_man': gpu_man, 'page_obj': page_obj, 'gpu_man_posts': page_obj})

class Home(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 9  #Inherits from ListView

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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
