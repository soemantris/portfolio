from django.urls import path

from .views import index

app_name="layanan"
urlpatterns = [
    path('', index, name='layanan_index'),
]
