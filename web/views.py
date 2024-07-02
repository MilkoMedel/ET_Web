from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request,'nosotros.html')

def galeria(request):
    return render(request,'galeria.html')