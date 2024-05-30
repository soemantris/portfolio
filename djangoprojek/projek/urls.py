from django.urls import path

from .views import index, project_detail

app_name = "projek"
urlpatterns = [
    path('', index, name="projek_index"),
    path('<slug:slug_projek>/', project_detail, name="project_detail"),
]
