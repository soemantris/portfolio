from django.shortcuts import render
from .models import Project, Category

# Create your views here.
def index(request):
    categories = Category.objects.all().order_by('-pub_date')
    projects = Project.objects.all().order_by('-pub_date')
    conteks = {
        'title':'Projek | Sumantri S | Full stack Developers',
        'categories':categories,
        'projects':projects,
    }
    return render(request, 'projek/index.html', conteks)

def project_detail(request, slug_projek):
    detail_project = Project.objects.get(slug=slug_projek)
    context = {
        'title':'Detail Projek | Sumantri S | Full stack Developers',
        'detail_project':detail_project,
    }
    return render(request, 'projek/detail_projek.html', context)