from django.contrib import admin
from .models import Post, CpuManufacturerOptions, GpuManufacturerOptions


admin.site.register(Post)
admin.site.register(CpuManufacturerOptions)
admin.site.register(GpuManufacturerOptions)
