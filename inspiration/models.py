from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pc_builds')
    feature_image = CloudinaryField('image', default='placeholder')
    secondary_image = CloudinaryField('image', default='placeholder')
    tertiary_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    cpu_content = models.TextField()
    gpu_content = models.TextField()
    likes = models.ManyToManyField(User, related_name='pc_likes', blank=True)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    
    def number_of_likes(self):
        return self.likes.count()
