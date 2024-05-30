from django.shortcuts import render
from django.core.paginator import Paginator
from projek.models import Project
from layanan.models import Testimony

def index(request):
    projects = Project.objects.all().order_by('-pub_date')
    testimonials = Testimony.objects.all()
    paginator = Paginator(projects, 2)

    page_number = request.GET.get('page')
    projects_all = paginator.get_page(page_number)
    context = {
        'title':'Sumantri S | Full Stack Developers',
        'projects':projects_all,
        'testimonials':testimonials,
    }
    return render(request, 'index.html', context)

def error_404(request, exception):
    data = {
        'title':'Page not found',
    }
    return render(request, '404.html', data, status=404)
