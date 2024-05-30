from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Akun Selamat Datang',
    }
    return render(request, 'akun/index.html', context)