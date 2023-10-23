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
from core import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('', include('core.urls')), 
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('registro/', views.registro, name='registro'),
    path('nueva_oferta/', views.nueva_oferta, name='nueva_oferta'),
    path('ofertas_admin/', views.ofertas_admin, name='ofertas_admin'),
    path('ofertas_user/', views.ofertas_user, name='ofertas_user'),
 
    # path('recuperar_contrasenia/', views.recuperar_contrasenia, name='recuperar_contrasenia'),
    # path('registrar_ncontrasenia/', views.registrar_ncontrasenia, name='registrar_ncontrasenia'),
    # path('login/', views.login, name='login'),

    path('accounts/', include('django.contrib.auth.urls')),

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



    
]
