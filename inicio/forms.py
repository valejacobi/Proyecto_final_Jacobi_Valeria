from django import forms
from ckeditor.fields import RichTextFormField



class EuropaFormulario(forms.Form):
    destino = forms.CharField(max_length=30)
    mes = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    dias = forms.IntegerField()
    fecha_creacion = forms.DateField()
    
class BusquedaEuropaFormulario(forms.Form):
    destino = forms.CharField(max_length=30)
    mes = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    dias = forms.IntegerField()
    fecha_creacion = forms.DateField()
    
class ActualizarEuropaFormulario(forms.Form):
    destino = forms.CharField(max_length=30)
    mes = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    dias = forms.IntegerField()
    fecha_creacion = forms.DateField()