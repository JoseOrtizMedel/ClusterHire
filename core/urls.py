from django.urls import path
from .views import home, registro, recuperar_contrasenia

urlpatterns = [
    path('', home, name="home"),
    path('', registro, name="registro"),
    path('', recuperar_contrasenia, name="recuperar_contrasenia")
]