from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'feature_image', 'secondary_image', 'tertiary_image', 'cpu_content', 'cpu_cooler_content', 'motherboard_content', 'ram_content', 'storage_content', 'gpu_content', 'psu_content', 'case_content', 'fans_content')

        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.TextInput(attrs={'class': 'form-control'}),
            'feature_image': forms.FileInput(attrs={'class': 'form-control'}),
            'secondary_image': forms.FileInput(attrs={'class': 'form-control'}),
            'tertiary_image': forms.FileInput(attrs={'class': 'form-control'}),
            'cpu_content': forms.TextInput(attrs={'class': 'form-control'}),
            'cpu_cooler_content': forms.TextInput(attrs={'class': 'form-control'}),
            'motherboard_content': forms.TextInput(attrs={'class': 'form-control'}),
            'ram_content': forms.TextInput(attrs={'class': 'form-control'}),
            'storage_content': forms.TextInput(attrs={'class': 'form-control'}),
            'gpu_content': forms.TextInput(attrs={'class': 'form-control'}),
            'psu_content': forms.TextInput(attrs={'class': 'form-control'}),
            'case_content': forms.TextInput(attrs={'class': 'form-control'}),
            'fans_content': forms.TextInput(attrs={'class': 'form-control'}),
        }
