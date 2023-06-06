import django_filters
from .models import Post


class HomeFilter(django_filters.FilterSet):

    class Meta:
        model = Post
        fields = ('title', 'cpu_content', 'cpu_cooler_content',
                  'motherboard_content', 'ram_content', 'storage_content',
                  'gpu_content', 'psu_content', 'case_content',
                  'fans_content')