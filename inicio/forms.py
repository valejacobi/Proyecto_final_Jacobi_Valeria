from django import forms
from ckeditor.fields import RichTextFormField
from .models import Europa



class EuropaFormulario(forms.Form):
    destino = forms.CharField(max_length=30)
    mes = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    dias = forms.IntegerField()
    fecha_creacion = forms.DateField()
    imagen = forms.ImageField(required=False)

class EuropaFormulario(forms.ModelForm):
    class Meta:
        model = Europa
        fields = ['destino', 'mes', 'descripcion', 'dias', 'fecha_creacion', 'imagen']
    
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
    imagen = forms.ImageField()
    
