from . import views
from django.urls import path
from .views import Home, AddPC, PCDetail, CpuManView, GpuManView, UpdatePost, RemovePost


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('pc-build/<int:pk>', PCDetail.as_view(), name="pc-details"),
    path('add_pc/', AddPC.as_view(), name='add_pc'),
    path('cpu_manufacturer/<str:cpu_man>/', CpuManView, name='cpuman'),
    path('gpu_manufacturer/<str:gpu_man>/', GpuManView, name='gpuman'),
    path('pc-build/edit/<int:pk>', UpdatePost.as_view(), name='editpost'),
    path('pc-build/delete/<int:pk>', RemovePost.as_view(), name='deletepost'),
]
