from django.contrib import messages
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from web.forms import SignUpForm
from web.models import Registro_cliente
from .forms import ProductosForm
from .models import Producto

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def nosotros(request):
    return render(request,'nosotros.html')

@login_required
def galeria(request):
    return render(request,'galeria.html')

def form(request):
    data = {
        'form': SignUpForm()
    }
    if request.method == "POST":
        formulario = SignUpForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            genero = formulario.cleaned_data.get('genero')
            fecha_nac = formulario.cleaned_data.get('fecha_nac')
            cel = formulario.cleaned_data.get('cel')
            Registro_cliente.objects.create(user=user, id_genero=genero, fecha_nac=fecha_nac, cel=cel)
            
            # Authenticate and log in the user
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Te has registrado correctamente")
                return redirect('index')
            else:
                messages.error(request, "Hubo un problema con la autenticación")
        
        data["form"] = formulario
    
    return render(request, 'form.html', data)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to a home page or any other page
            else:
                return HttpResponse("Invalid login")
        else:
            return HttpResponse("Invalid form")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})    # inicia sesion.

def crud(request):
    producto = Producto.objects.all()
    ctx = {
        'producto': producto 
    }
    return render(request, 'producto/crud.html', ctx)       # cambia a la lista de productos para mod,add,del

@staff_member_required
def producto_add(request):
    if request.method == "POST":
        form = ProductosForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = ProductosForm()
    return render(request, 'producto/producto_add.html', {'form': form})

@staff_member_required
def producto_mod(request, id):
    product = Producto.objects.get(id=id)
    ctx = {
        'form': ProductosForm(instance=product),
        'id': id,
    }
    if request.method == "POST":
        form = ProductosForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('crud')
    return render(request, 'producto/producto_mod.html', ctx)

@staff_member_required
def producto_del(request, id):
    product = Producto.objects.get(id=id)
    product.delete()
    return redirect('crud')