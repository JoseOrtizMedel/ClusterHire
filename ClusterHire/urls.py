"""ClusterHire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django .conf import settings
from core import views, ciencia
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LoginView, LogoutView


urlpatterns = [
    path('', include('core.urls')), 
    path('admin/', admin.site.urls),
    path('', views.user_login, name="login"),
    #path('', LoginView.as_view(template_name='registration/login.html'), name='home'),
    path('nueva_oferta/', views.nueva_oferta, name='nueva_oferta'),
    path('ofertas_admin/', views.ofertas_admin, name='ofertas_admin'),
    path('ofertas_user/', views.ofertas_user, name='ofertas_user'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    #path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('password-reset/',
         PasswordResetView.as_view(
             template_name='users/password_reset.html',
             html_email_template_name='users/password_reset_email.html'
         ),
         name='password-reset'
         ),
    path('password_reset_done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('eliminar_oferta/<id_oferta>/', views.eliminar_oferta, name='eliminar_oferta'),    
    path('formulario/<int:id_oferta>/<str:nom_oferta>/', views.formulario, name='formulario'),
    path('compe_oferta/<int:id_oferta>/<str:nom_oferta>/', views.compe_oferta, name='compe_oferta'),
    path('exportar_csv/<int:id_oferta>/<str:nom_oferta>/', ciencia.exportar_csv, name='exportar_csv'),
    path('ciencia/<int:id_oferta>/<str:nom_oferta>/', views.ciencia, name='ciencia'),
    path('read_csv/<int:id_oferta>/', ciencia.read_csv, name='read_csv'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil2/', views.perfil2, name='perfil2'),
    path('perfil_user/<pk>/', views.perfil_user, name='perfil_user'),
    path('perfil_admin/<int:id_usuario>/<int:id_oferta>/', views.perfil_admin, name='perfil_admin'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

