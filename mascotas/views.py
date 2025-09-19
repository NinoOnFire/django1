from django.shortcuts import render, redirect
from mascotas.models import Mascotas
from .forms import RegistroForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def galeria(request):
    mascotas = Mascotas.objects.all()
    data = {'mascotas': mascotas }
    return render(request, 'galeria.html', data)

def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("galeria")  # 👈 usa el nombre de tu vista/URL de galería
    else:
        form = RegistroForm()
    return render(request, "registro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # crea la sesión
            return redirect("inicio")  # redirige a tu página principal
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    
    return render(request, "login.html")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("login")
