from django.urls import path
from inicio.views import inicio, europa_view

urlpatterns = [
    path('', inicio,name='inicio'),
    path('Europa/', europa_view,name='Europa'),
    
]