from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'feature_image', 'secondary_image', 'tertiary_image', 'cpu_content', 'cpu_cooler_content', 'motherboard_content', 'ram_content', 'storage_content', 'gpu_content', 'psu_content', 'case_content', 'fans_content')

        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Name of your PC'}),
            'feature_image': forms.FileInput(attrs={'class': 'form-control item'}),
            'secondary_image': forms.FileInput(attrs={'class': 'form-control item'}),
            'tertiary_image': forms.FileInput(attrs={'class': 'form-control item'}),
            'cpu_content': forms.TextInput(attrs={'class': 'form-control item'}),
            'cpu_cooler_content': forms.TextInput(attrs={'class': 'form-control item'}),
            'motherboard_content': forms.TextInput(attrs={'class': 'form-control item'}),
            'ram_content': forms.TextInput(attrs={'class': 'form-control item'}),
            'storage_content': forms.TextInput(attrs={'class': 'form-control item'}),
            'gpu_content': forms.TextInput(attrs={'class': 'form-control item'}),
            'psu_content': forms.TextInput(attrs={'class': 'form-control item'}),
            'case_content': forms.TextInput(attrs={'class': 'form-control item'}),
            'fans_content': forms.TextInput(attrs={'class': 'form-control item'}),
        }
