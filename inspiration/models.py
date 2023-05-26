from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from .formatChecker import ContentTypeRestrictedFileField


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='pc_builds')
    feature_image = ContentTypeRestrictedFileField(
        content_types=['image/jpeg', 'image/png'],max_upload_size=10000000)
    secondary_image = ContentTypeRestrictedFileField(
        content_types=['image/jpeg', 'image/png'],max_upload_size=10000000)
    tertiary_image = ContentTypeRestrictedFileField(
        content_types=['image/jpeg', 'image/png'],max_upload_size=10000000)
    created_on = models.DateTimeField(auto_now_add=True)
    cpu_content = models.CharField(max_length=150)
    cpu_cooler_content = models.CharField(max_length=150)
    motherboard_content = models.CharField(max_length=150,)
    ram_content = models.CharField(max_length=200)
    storage_content = models.CharField(max_length=250)
    gpu_content = models.CharField(max_length=150)
    psu_content = models.CharField(max_length=150)
    case_content = models.CharField(max_length=150)
    fans_content = models.CharField(max_length=150)
    likes = models.ManyToManyField(User, related_name='pc_likes', blank=True)

    def get_absolute_url(self):
        return reverse('pc-details', args=(str(self.id)))

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
