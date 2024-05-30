from django.urls import path

from .views import index, article_detail

app_name = 'artikel'
urlpatterns = [
    path('<slug:slug_input_article>/', article_detail, name='article_detail'),
    path('', index, name='artikel_index'),
]
