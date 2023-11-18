from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.urls import reverse_lazy
from cuentas.forms import MiFormularioDeCreacion
#from cuentas.models import DatosExtra


def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra = formulario.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)
            
            django_login(request, user)
            
            #DatosExtra.objects.get_or_create(user=request.user)
            
            return redirect('inicio')
              
    return render(request, 'cuentas/login.html', {'formulario_de_login': formulario})

def registro(request):
    formulario = MiFormularioDeCreacion()
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('login')
            
    return render(request, 'cuentas/registro.html', {'formulario_de_registro': formulario})
