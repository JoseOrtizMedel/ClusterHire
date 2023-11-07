from django.urls import path

from .views import home, nueva_oferta, ofertas_admin, ofertas_user, perfilCompe, perfilDire, perfilExp, register, login, eliminar_oferta, formulario, perfilPers, compe_oferta


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
    path('compe_oferta/<int:id_oferta>', compe_oferta, name='compe_oferta'),
    path('perfil_direccion/', perfilDire, name='perfil_direccion'),
    path('perfil_personal/', perfilPers, name='perfil_personal'),
    path('perfil_experiencia/', perfilExp, name='perfil_experiencia'),
    path('perfil_competencias/', perfilCompe, name='perfil_competencias'),

    path('ciencia', ciencia_datos, name="ciencia"),
    path('exportar-csv/', exportar_datos_a_csv, name='exportar_csv'),

]