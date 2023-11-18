from django.urls import path
from cuentas.views import login, registro, ver_perfil, editar_perfil, CambiarPassword
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name='logout'),
    path('registro/', registro, name='registrarse'),
    path('perfil/editar/', ver_perfil, name='ver_perfil'),
    path('perfil/editar/password/', CambiarPassword.as_view(), name='cambiar_password'), 
    path('perfil/editar/editar_perfil/', editar_perfil, name='editar_perfil') 
] 
