from django.urls import path

from .views import index

app_name = "akun"
urlpatterns = [
    path('', index, name='akun_index'),
]