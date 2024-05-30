from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Layanan | Sumantri S | Full Stack Developers',
    }
    return render(request, 'layanan/index.html', context)