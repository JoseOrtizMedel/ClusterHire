from django.urls import path
from .views import home, login

#urlpatterns = [
 #   path('', nueva_oferta, name="nueva_oferta"),
 #   path('nueva_oferta', nueva_oferta, name="nueva_oferta")
#]

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login")
]