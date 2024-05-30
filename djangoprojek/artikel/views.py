from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article, Category

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-pub_date')
    paginator = Paginator(articles, 3)

    page_number = request.GET.get('page')
    articles_all = paginator.get_page(page_number)

    context = {
        'title':'Artikel | Sumantri S | Full Steck Developers',
        'articles': articles_all,
    }
    return render(request, 'artikel/index.html', context)

def article_detail(request, slug_input_article):
    list_categories = Category.objects.all();
    article_details = Article.objects.get(slug=slug_input_article)
    return render(request, 'artikel/artikel_detail.html', {'article_details':article_details,'list_categories':list_categories,})