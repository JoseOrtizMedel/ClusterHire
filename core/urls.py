from django.urls import path

from .views import home, nueva_oferta, ofertas_admin, ofertas_user, registro, recuperar_contrasenia, registrar_ncontrasenia, login

urlpatterns = [
    path('', home, name="home"),
    path('nueva_oferta', nueva_oferta, name="nueva_oferta"),
    path('ofertas_admin', ofertas_admin, name="ofertas_admin"),
    path('ofertas_user', ofertas_user, name="ofertas_user"),
    path('', registro, name="registro"),
    path('', recuperar_contrasenia, name="recuperar_contrasenia"),
    path('', registrar_ncontrasenia, name="registrar_ncontrasenia"),
    path('login', login, name="login")
]

