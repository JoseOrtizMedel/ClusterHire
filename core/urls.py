from django.urls import path

from .views import perfil_admin, ciencia, edit_direccion, edit_educacion, edit_experiencia, edit_personal, eliminar_compes, eliminar_educacion, eliminar_exps, eliminar_habis, eliminar_idiomas, eliminar_logros, nueva_oferta, ofertas_admin, ofertas_user, perfil_user, register, eliminar_oferta, formulario, compe_oferta

from .views import  ciencia, edit_direccion, edit_educacion, edit_experiencia, edit_personal, eliminar_compes, eliminar_educacion, eliminar_exps, eliminar_habis, eliminar_idiomas, eliminar_logros, error_404, nueva_oferta, ofertas_admin, ofertas_user, perfil_admin, register, eliminar_oferta, formulario, compe_oferta, user_login

from .ciencia import  read_csv, exportar_csv

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LoginView, LogoutView

urlpatterns = [
    #path('', LoginView.as_view(template_name='registration/login.html'), name="home"),
    path('', user_login, name="home"),
    path('404', error_404, name="404"),
    path('nueva_oferta', nueva_oferta, name="nueva_oferta"),
    path('ofertas_admin', ofertas_admin, name="ofertas_admin"),
    path('ofertas_user', ofertas_user, name="ofertas_user"),
    path('register', register, name="register"),
    path('eliminar_oferta/<id_oferta>/', eliminar_oferta, name='eliminar_oferta'),
    path('formulario/<int:id_oferta>/<str:nom_oferta>/', formulario, name='formulario'),
    path('compe_oferta/<int:id_oferta>/<str:nom_oferta>/', compe_oferta, name='compe_oferta'),
    path('perfil_user/', perfil_user, name='perfil_user'),
    path('perfil_admin/<int:id_usuario>/<int:id_oferta>/', perfil_admin, name='perfil_admin'),
    path('eliminar-competencia/<pk>/', eliminar_compes, name="eliminar_compes"),
    path('eliminar-habilidad/<pk>/', eliminar_habis, name="eliminar_habis"),
    path('eliminar-idioma/<pk>/', eliminar_idiomas, name="eliminar_idiomas"),
    path('eliminar_educacion/<pk>/', eliminar_educacion, name="eliminar_educacion"),
    path('eliminar_logros/<pk>/', eliminar_logros, name="eliminar_logros"),
    path('eliminar_exps/<pk>/', eliminar_exps, name="eliminar_exps"),

    path('edit_educacion/<pk>/', edit_educacion, name="edit_educacion"),
    path('edit_experiencia/<pk>/', edit_experiencia, name="edit_experiencia"),
    path('edit_direccion/<pk>/', edit_direccion, name="edit_direccion"),
    path('edit_personal/<pk>/', edit_personal, name="edit_personal"),

    path('exportar_csv/<int:id_oferta>/<str:nom_oferta>/', exportar_csv, name='exportar_csv'),
    path('ciencia/<int:id_oferta>/<str:nom_oferta>/', ciencia, name='ciencia'),
    path('read_csv/<int:id_oferta>/', read_csv, name='read_csv'),
]

