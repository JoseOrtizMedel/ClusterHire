from django.urls import path

from .views import edit_direccion, edit_educacion, edit_experiencia, edit_personal, eliminar_compes, eliminar_educacion, eliminar_exps, eliminar_habis, eliminar_idiomas, eliminar_logros, nueva_oferta, ofertas_admin, ofertas_user, perfil, perfilDire, perfilEduc, perfilExp, register, eliminar_oferta, formulario, perfilPers, compe_oferta


from .ciencia import ciencia_datos, exportar_datos_a_csv

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html'), name="home"),
    path('nueva_oferta', nueva_oferta, name="nueva_oferta"),
    path('ofertas_admin', ofertas_admin, name="ofertas_admin"),
    path('ofertas_user', ofertas_user, name="ofertas_user"),
    path('register', register, name="register"),
    path('eliminar_oferta/<id_oferta>/', eliminar_oferta, name='eliminar_oferta'),
    path('formulario/<int:id_oferta>/<str:nom_oferta>/', formulario, name='formulario'),
    path('compe_oferta/<int:id_oferta>/<str:nom_oferta>/', compe_oferta, name='compe_oferta'),
    path('perfil_direccion/', perfilDire, name='perfil_direccion'),
    path('perfil_personal/', perfilPers, name='perfil_personal'),
    path('perfil_experiencia/', perfilExp, name='perfil_experiencia'),
    #path('perfil_competencias/', perfilCompe, name='perfil_competencias'),
    path('perfil_educacion/', perfilEduc, name='perfil_educacion'),
    path('perfil/', perfil, name='perfil'),
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

    path('ciencia', ciencia_datos, name="ciencia"),
    path('exportar-csv/', exportar_datos_a_csv, name='exportar_csv'),

]