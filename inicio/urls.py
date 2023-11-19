from django.urls import path
from inicio.views import inicio, acerca_de_mi, europa_view, buscador, detalle_europa, eliminar_europa, actualizar_europa

urlpatterns = [
    path('', inicio,name='inicio'),
    path('Acerca de mi/', acerca_de_mi, name='acerca_de_mi'),
    path('buscador/', buscador,name='Buscador'),
    path('Europa/', europa_view,name='Europa'),
    path('Europa/<int:europa_id>/', detalle_europa, name='detalle_europa'),
    path('Europa/<int:pk>/eliminar/', eliminar_europa.as_view(), name='eliminar_europa'),
    path('Europa/<int:europa_id>/actualizar/', actualizar_europa, name='actualizar_europa'),

]