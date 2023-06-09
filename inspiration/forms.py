from django import forms
from .models import Post
from django.contrib.auth.models import User


cpu_choices = [('Intel', 'Intel'), ('AMD', 'AMD')]
gpu_choices = [('Intel', 'Intel'), ('AMD', 'AMD'), ('Nvidia', 'Nvidia')]
# Hard coding manufacturer choices here to be used in the choices widgets below


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)  # Excluding author as this gets auto filled
        fields = ('title', 'feature_image', 'secondary_image',
                  'tertiary_image', 'cpu', 'cpu_manufacturer', 'cpu_cooler',
                  'motherboard', 'ram', 'storage',
                  'gpu', 'gpu_manufacturer', 'psu', 'case', 'fans',)
# Listing all data fields which requires user input

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control item',
                'placeholder': 'Give your PC a name'
            }),
            'feature_image': forms.FileInput(attrs={
                'class': 'form-control item',
                'placeholder': 'Please upload JPEG or PNG'
            }),
            'secondary_image': forms.FileInput(attrs={
                'class': 'form-control item',
                'placeholder': 'Please upload JPEG or PNG'
            }),
            'tertiary_image': forms.FileInput(attrs={
                'class': 'form-control item',
                'placeholder': 'Please upload JPEG or PNG'
            }),
            'cpu_manufacturer': forms.Select(choices=cpu_choices, attrs={
                'class': 'form-control item'
            }),
            'cpu': forms.TextInput(attrs={
                'class': 'form-control item'
            }),
            'cpu_cooler': forms.TextInput(attrs={
                'class': 'form-control item'
            }),
            'motherboard': forms.TextInput(attrs={
                'class': 'form-control item'
            }),
            'ram': forms.TextInput(attrs={
                'class': 'form-control item'
            }),
            'storage': forms.TextInput(attrs={
                'class': 'form-control item'
            }),
            'gpu_manufacturer': forms.Select(choices=gpu_choices, attrs={
                'class': 'form-control item'
            }),
            'gpu': forms.TextInput(attrs={
                'class': 'form-control item'
            }),
            'psu': forms.TextInput(attrs={
                'class': 'form-control item'
            }),
            'case': forms.TextInput(attrs={
                'class': 'form-control item'
            }),
            'fans': forms.TextInput(attrs={
                'class': 'form-control item'
            }),
        }
