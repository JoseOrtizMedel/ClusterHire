from django.urls import path
from .views import home, registro, recuperar_contrasenia, registrar_ncontrasenia

urlpatterns = [
    path('', home, name="home"),
    path('', registro, name="registro"),
    path('', recuperar_contrasenia, name="recuperar_contrasenia"),
    path('', registrar_ncontrasenia, name="registrar_ncontrasenia")
]