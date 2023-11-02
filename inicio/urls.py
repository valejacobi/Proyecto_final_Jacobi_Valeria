from django.urls import path
from inicio.views import inicio, europa_view, america_view, africa_view, asia_view, oceania_view, buscador

urlpatterns = [
    path('', inicio,name='inicio'),
    path('buscador/', buscador,name='Buscador'),
    path('Europa/', europa_view,name='Europa'),
    path('America/', america_view,name='America'),
    path('Africa/', africa_view,name='Africa'),
    path('Asia/', asia_view,name='Asia'),
    path('Oceania/', oceania_view,name='Oceania')
]