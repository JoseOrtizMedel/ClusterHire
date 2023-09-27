from django.urls import path
from .views import home, nueva_oferta

urlpatterns = [
    path('', home, name="home"),
    path('nueva_oferta', nueva_oferta, name="nueva_oferta")
]