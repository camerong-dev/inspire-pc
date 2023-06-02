from . import views
from django.urls import path
from .views import Home, AddPC, PCDetail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('pc-build/<int:pk>', PCDetail.as_view(), name="pc-details"),
    path('add_pc/', AddPC.as_view(), name='add_pc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
