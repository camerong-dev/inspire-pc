from . import views
from django.urls import path
from .views import Home, AddPC, PCDetail


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('pc-build/<int:pk>', PCDetail.as_view(), name="pc-details"),
    path('add_pc/', AddPC.as_view(), name='add_pc'),
]
