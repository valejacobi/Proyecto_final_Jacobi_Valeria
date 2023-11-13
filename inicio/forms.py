from django import forms

class EuropaFormulario(forms.Form):
    destino = forms.CharField(max_length=30)
    mes = forms.CharField(max_length=30)
    dias = forms.IntegerField()
    
class BusquedaEuropaFormulario(forms.Form):
    destino = forms.CharField(max_length=30, required=False)
    mes = forms.CharField(max_length=30, required=False)
    dias = forms.IntegerField()
    
class ActualizarEuropaFormulario(forms.Form):
    destino = forms.CharField(max_length=30, required=False)
    mes = forms.CharField(max_length=30, required=False)
    dias = forms.IntegerField()