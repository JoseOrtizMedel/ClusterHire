from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django .conf import settings
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),

    path('nueva_oferta/', views.nueva_oferta, name='nueva_oferta'),
    path('ofertas_admin/', views.ofertas_admin, name='ofertas_admin'),
    path('ofertas_user/', views.ofertas_user, name='ofertas_user'),
 
    path('recuperar_contrasenia/', views.recuperar_contrasenia, name='recuperar_contrasenia'),
    path('registrar_ncontrasenia/', views.registrar_ncontrasenia, name='registrar_ncontrasenia'),
  
]
