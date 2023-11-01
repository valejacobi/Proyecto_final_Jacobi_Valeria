from django.shortcuts import render
from inicio.models import Europa, America, Africa, Asia, Oceania

def inicio (request):
    
     return render (request, 'inicio/inicio.html', {})

def europa_view(request):
     if request.method == 'POST':
          destino = request.POST.get('destino')
          mes = request.POST.get('mes')
          dias = request.POST.get('dias')

  
          
          if not destino or not mes or not dias:
            return render(request, 'inicio/europa.html', {'error_message': 'Por favor, completa todos los campos'})
          
          europa = Europa(destino=destino, mes=mes, dias=dias)
          europa.save()
          
          return render (request, 'inicio/europa.html', {})
     
     return render(request, 'inicio/europa.html', {})

def america_view(request):
     if request.method == 'POST':
          destino = request.POST.get('destino')
          mes = request.POST.get('mes')
          dias = request.POST.get('dias')
          
          if not destino or not mes or not dias:
            return render(request, 'inicio/america.html', {'error_message': 'Por favor, completa todos los campos'})
          
          america = America(destino=destino, mes=mes, dias=dias)
          america.save()
          
          return render (request, 'inicio/america.html', {})
     
     return render(request, 'inicio/america.html', {})

def africa_view(request):
     
     if request.method == 'POST':
          destino = request.POST.get('destino')
          mes = request.POST.get('mes')
          dias = request.POST.get('dias')

          
          if not destino or not mes or not dias:
            return render(request, 'inicio/africa.html', {'error_message': 'Por favor, completa todos los campos'})
          
          africa = Africa(destino=destino, mes=mes, dias=dias)
          africa.save()
          
          return render (request, 'inicio/africa.html', {})
     
     return render(request, 'inicio/africa.html', {})

def asia_view(request):
     
     if request.method == 'POST':
          destino = request.POST.get('destino')
          mes = request.POST.get('mes')
          dias = request.POST.get('dias')

          
          if not destino or not mes or not dias:
            return render(request, 'inicio/asia.html', {'error_message': 'Por favor, completa todos los campos'})
          
          asia = Asia(destino=destino, mes=mes, dias=dias)
          asia.save()
          
          return render (request, 'inicio/asia.html', {})
     
     return render(request, 'inicio/asia.html', {})


def oceania_view(request):
     if request.method == 'POST':
          destino = request.POST.get('destino')
          mes = request.POST.get('mes')
          dias = request.POST.get('dias')

          
          if not destino or not mes or not dias:
            return render(request, 'inicio/oceania.html', {'error_message': 'Por favor, completa todos los campos'})
          
          oceania = Oceania(destino=destino, mes=mes, dias=dias)
          oceania.save()
          
          return render (request, 'inicio/oceania.html', {})
     
     return render(request, 'inicio/oceania.html', {})