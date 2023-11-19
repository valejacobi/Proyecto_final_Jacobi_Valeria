from django.shortcuts import render, redirect
from inicio.models import Europa
from inicio.forms import EuropaFormulario, BusquedaEuropaFormulario, ActualizarEuropaFormulario
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin 

def inicio (request):

     return render (request, 'inicio/inicio.html', {})

def acerca_de_mi (request):
     
     return render (request, 'inicio/acerca_de_mi.html', {})

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

# @login_required
# def eliminar_europa(request, europa_id):
#      europa_a_eliminar = Europa.objects.get(id=europa_id)            
#      europa_a_eliminar.delete()
#      return redirect('Buscador')

class eliminar_europa(LoginRequiredMixin, DeleteView):
    model = Europa
    template_name = "inicio/eliminar_europa.html"
    success_url = reverse_lazy('Buscador') 


@login_required
def actualizar_europa(request, europa_id):         	
    europa_a_actualizar = Europa.objects.get(id=europa_id)
    
    if request.method == "POST":
        formulario = ActualizarEuropaFormulario(request.POST, request.FILES) 
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            europa_a_actualizar.destino = info_nueva.get('destino')
            europa_a_actualizar.mes = info_nueva.get('mes')
            europa_a_actualizar.descripcion = info_nueva.get('descripcion')
            europa_a_actualizar.dias = info_nueva.get('dias')
            europa_a_actualizar.fecha_creacion = info_nueva.get('fecha_creacion')
            europa_a_actualizar.imagen = info_nueva.get('imagen')
            
            europa_a_actualizar.save()
            return redirect('Buscador')
        else:
            return render(request, 'inicio/actualizar_europa.html', {'formulario': formulario})
				
    formulario = ActualizarEuropaFormulario(initial={'destino': europa_a_actualizar.destino, 'mes': europa_a_actualizar.mes, 'descripcion': europa_a_actualizar.descripcion, 'dias': europa_a_actualizar.dias, 'fecha_creacion': europa_a_actualizar.fecha_creacion, 'imagen': europa_a_actualizar.imagen})
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
          formulario = EuropaFormulario(request.POST, request.FILES)
          if formulario.is_valid():
               
               info_limpia = formulario.cleaned_data

               destino = info_limpia.get('destino')
               mes = info_limpia.get('mes')
               descripcion = info_limpia.get('descripcion')
               dias = info_limpia.get('dias')
               fecha_creacion = info_limpia.get('fecha_creacion')
               imagen = info_limpia.get('imagen')

               europa = Europa(destino=destino.lower(), mes=mes, descripcion=descripcion, dias=dias, fecha_creacion=fecha_creacion, imagen=imagen)
               europa.save()

               return redirect('Buscador')
          else:
               return render(request, 'inicio/europa.html', {'formulario':formulario})

     formulario = EuropaFormulario()
     return render(request, 'inicio/europa.html', {'formulario':formulario})