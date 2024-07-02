from django.contrib import messages
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from web.forms import SignUpForm
from web.models import Registro_cliente

# Create your views here.

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request,'nosotros.html')

def galeria(request):
    return render(request,'galeria.html')

def form(request):
    data ={
        'form' : SignUpForm()
    }
    if request.method=="POST":
        formulario= SignUpForm(data=request.POST)
        if formulario.is_valid():
            user        = formulario.save()
            genero      = formulario.cleaned_data.get('genero')
            fecha_nac   = formulario.cleaned_data.get('fecha_nac')
            cel         = formulario.cleaned_data.get('cel')  
            Registro_cliente.objects.create(user=user, id_genero=genero, fecha_nac=fecha_nac, cel=cel)
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect('index')
        data["form"] = formulario
    return render(request, 'form.html',data)

def login(request):
    return render(request,'login.html')
