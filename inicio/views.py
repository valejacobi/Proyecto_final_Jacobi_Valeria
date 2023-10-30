from django.shortcuts import render
from inicio.models import Europa

def inicio (request):
    
     return render (request, 'inicio/inicio.html', {})

def europa_view(request):
     europa = Europa(destino='España', mes="enero", dias=2)
     europa.save()
     
     return render (request, 'inicio/europa.html', {'europa':europa})