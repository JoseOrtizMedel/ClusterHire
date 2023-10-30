from django.urls import path
from .views import home, nueva_oferta, ofertas_admin, ofertas_user, register, login, eliminar_oferta, formulario, perfil
from .ciencia import ciencia_datos, exportar_datos_a_csv
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', home, name="home"),
    path('nueva_oferta', nueva_oferta, name="nueva_oferta"),
    path('ofertas_admin', ofertas_admin, name="ofertas_admin"),
    path('ofertas_user', ofertas_user, name="ofertas_user"),
    path('register', register, name="register"),
    path('eliminar_oferta/<id_oferta>/', eliminar_oferta, name='eliminar_oferta'),
    path('formulario/<int:id_oferta>/<str:nom_oferta>/', formulario, name='formulario'),
    path('perfil', perfil, name="perfil"),
    path('ciencia', ciencia_datos, name="ciencia"),
    path('exportar-csv/', exportar_datos_a_csv, name='exportar_csv'),

]
