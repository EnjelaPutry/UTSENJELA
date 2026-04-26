from django.contrib import admin
from django.urls import path
from . import views  # Ini penting untuk memanggil file views tadi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # Sekarang kita panggil views.home
]