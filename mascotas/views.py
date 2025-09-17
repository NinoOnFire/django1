from django.shortcuts import render
from mascotas.models import Mascotas
# Create your views here.

def galeria(request):
    mascotas = Mascotas.objects.all()
    data = {'mascotas': mascotas }
    return render(request, 'galeria.html', data)