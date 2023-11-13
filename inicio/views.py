from django.shortcuts import render, redirect
from inicio.models import Europa, America, Africa, Asia, Oceania
from inicio.forms import EuropaFormulario, BusquedaEuropaFormulario, ActualizarEuropaFormulario

def inicio (request):

     return render (request, 'inicio/inicio.html', {})

def buscador(request):
     
     destino_a_buscar = request.GET.get('destino')
     
     if destino_a_buscar:
          listado_de_europa = Europa.objects.filter(destino__icontains=destino_a_buscar)
     else:
          listado_de_europa = Europa.objects.all()
     
     return render(request, 'inicio/buscador.html', {'listado_de_europa': listado_de_europa})

     #  formulario = BusquedaEuropaFormulario(request.GET)

     #  if formulario.is_valid():
     #       destino_a_buscar = formulario.cleaned_data.get('destino')
     #       listado_de_europa = Europa.objects.filter(destino__icontains=destino_a_buscar)

     #  formulario = BusquedaEuropaFormulario()
     #  return render (request, 'inicio/buscador.html', {'formulario': formulario, 'listado_de_europa': listado_de_europa})
     

          # destino_a_buscar = request.GET.get('destino')
          # if destino_a_buscar:
          #     listado_de_europa = Europa.objects.filter(destino__icontains=destino_a_buscar)
          
          # else:
          #      listado_de_europa = Europa.objects.all()
          
          # formulario = BusquedaEuropaFormulario()
          # return render(request, 'inicio/buscador.html', {'formulario': formulario, 'listado_de_europa': listado_de_europa})

def eliminar_europa(request, europa_id):
     europa_a_eliminar = Europa.objects.get(id=europa_id)            
     europa_a_eliminar.delete()
     return redirect('Buscador')

def actualizar_europa(request, europa_id):         	
    europa_a_actualizar = Europa.objects.get(id=europa_id)
    
    if request.method == "POST":
        formulario = ActualizarEuropaFormulario(request.POST) 
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            europa_a_actualizar.destino = info_nueva.get('destino')
            europa_a_actualizar.mes = info_nueva.get('mes')
            europa_a_actualizar.dias = info_nueva.get('dias')
            
            europa_a_actualizar.save()
            return redirect('Buscador')
        else:
            return render(request, 'inicio/actualizar_europa.html', {'formulario': formulario})
				
    formulario = ActualizarEuropaFormulario(initial={'destino': europa_a_actualizar.destino, 'mes': europa_a_actualizar.mes,'dias': europa_a_actualizar.dias})
    return render(request, 'inicio/actualizar_europa.html', {'formulario': formulario})

def detalle_europa(request, europa_id):
    europa = Europa.objects.get(id=europa_id)
    return render(request, 'inicio/detalle_europa.html', {'europa': europa})


def europa_view(request):
     # if request.method == 'POST':
     #      destino = request.POST.get('destino')
     #      mes = request.POST.get('mes')
     #      dias = request.POST.get('dias')

     #      europa = Europa(destino=destino, mes=mes, dias=dias)
     #      europa.save()

     #      return render (request, 'inicio/europa.html', {})

     if request.method == 'POST':
          formulario = EuropaFormulario(request.POST)
          if formulario.is_valid():
               info_limpia = formulario.cleaned_data

               destino = info_limpia.get('destino')
               mes = info_limpia.get('mes')
               dias = info_limpia.get('dias')

               europa = Europa(destino=destino.lower(), mes=mes, dias=dias)
               europa.save()

               return redirect('Buscador')
          else:
               return render(request, 'inicio/europa.html', {'formulario':formulario})

     formulario = EuropaFormulario()
     return render(request, 'inicio/europa.html', {'formulario':formulario})

def america_view(request):
     if request.method == 'POST':
          destino = request.POST.get('destino')
          mes = request.POST.get('mes')
          dias = request.POST.get('dias')

          america = America(destino=destino, mes=mes, dias=dias)
          america.save()

          return render (request, 'inicio/america.html', {})

     return render(request, 'inicio/america.html', {})

def africa_view(request):

     if request.method == 'POST':
          destino = request.POST.get('destino')
          mes = request.POST.get('mes')
          dias = request.POST.get('dias')


          africa = Africa(destino=destino, mes=mes, dias=dias)
          africa.save()

          return render (request, 'inicio/africa.html', {})

     return render(request, 'inicio/africa.html', {})

def asia_view(request):

     if request.method == 'POST':
          destino = request.POST.get('destino')
          mes = request.POST.get('mes')
          dias = request.POST.get('dias')

          asia = Asia(destino=destino, mes=mes, dias=dias)
          asia.save()

          return render (request, 'inicio/asia.html', {})

     return render(request, 'inicio/asia.html', {})


def oceania_view(request):
     if request.method == 'POST':
          destino = request.POST.get('destino')
          mes = request.POST.get('mes')
          dias = request.POST.get('dias')


          oceania = Oceania(destino=destino, mes=mes, dias=dias)
          oceania.save()

          return render (request, 'inicio/oceania.html', {})

     return render(request, 'inicio/oceania.html', {})