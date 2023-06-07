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
        content_types=['image/jpeg', 'image/png'], max_upload_size=10000000)
    secondary_image = ContentTypeRestrictedFileField(
        content_types=['image/jpeg', 'image/png'], max_upload_size=10000000)
    tertiary_image = ContentTypeRestrictedFileField(
        content_types=['image/jpeg', 'image/png'], max_upload_size=10000000)
    created_on = models.DateTimeField(auto_now_add=True)
    cpu = models.CharField(max_length=150)
    cpu_manufacturer = models.CharField(max_length=100)
    cpu_cooler = models.CharField(max_length=150)
    motherboard = models.CharField(max_length=150)
    ram = models.CharField(max_length=200)
    storage = models.CharField(max_length=250)
    gpu = models.CharField(max_length=150)
    gpu_manufacturer = models.CharField(max_length=100)
    psu = models.CharField(max_length=150)
    case = models.CharField(max_length=150)
    fans = models.CharField(max_length=150)
    likes = models.ManyToManyField(User, related_name='pc_likes', blank=True)

    def get_absolute_url(self):
        return reverse('pc-details', kwargs={"pk": self.id} )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class CpuManufacturerOptions(models.Model):
    cpu_manufacturer = models.CharField(max_length=150)

    def __str__(self):
        return self.cpu_manufacturer

    def get_absolute_url(self):
        return reverse('cpuman', kwargs={"cpu_man": self.id} )


class GpuManufacturerOptions(models.Model):
    gpu_manufacturer = models.CharField(max_length=150)

    def __str__(self):
        return self.gpu_manufacturer

    def get_absolute_url(self):
        return reverse('pc-details', kwargs={"pk":self.id} )
