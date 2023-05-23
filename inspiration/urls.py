from . import views
from django.urls import path
from .views import Home, AddPC


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('add_pc/', AddPC.as_view(), name='add_pc'),
]