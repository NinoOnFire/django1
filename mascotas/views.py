from django.shortcuts import render, redirect
from mascotas.models import Mascotas
from .forms import RegistroForm
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
