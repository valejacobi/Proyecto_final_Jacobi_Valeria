from django.shortcuts import render
from inicio.models import Europa, America, Africa, Asia, Oceania

def inicio (request):
    
     return render (request, 'inicio/inicio.html', {})

def europa_view(request):
     europa = Europa(destino='España', mes="enero", dias=2)
     europa.save()
     
     return render (request, 'inicio/europa.html', {'europa':europa})

def america_view(request):
     america = America(destino='España', mes="enero", dias=2)
     america.save()
     
     return render (request, 'inicio/america.html', {'america':america})

def africa_view(request):
     africa = Africa(destino='España', mes="enero", dias=2)
     africa.save()
     
     return render (request, 'inicio/africa.html', {'africa':africa})

def asia_view(request):
     asia = Asia(destino='España', mes="enero", dias=2)
     asia.save()
     
     return render (request, 'inicio/asia.html', {'asia':asia})

def oceania_view(request):
     oceania = Oceania(destino='España', mes="enero", dias=2)
     oceania.save()
     
     return render (request, 'inicio/oceania.html', {'oceania':oceania})