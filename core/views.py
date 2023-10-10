from django.shortcuts import render, redirect
from django.http import request
from .models import Oferta
from .forms import OfertaForm
from django import forms
import time

# Create your views here.
def home(request):
    return render(request,'home.html')

def registro(request):
    return render(request,'registro.html')

def nueva_oferta(request):
    return render(request,'nueva_oferta.html')

def ofertas_admin(request):
    return render(request,'ofertas_admin.html')

def ofertas_user(request):
    return render(request,'ofertas_user.html')
  
def recuperar_contrasenia(request):
    return render(request,'recuperar_contrasenia.html')

def registrar_ncontrasenia(request):
    return render(request, 'registrar_ncontrasenia.html')

def login(request):
    return render(request,'login.html')


#base de datos

# JORDAAAAAAAN--------------------------------------------------------------

def nueva_oferta(request):
    datos = {'form': OfertaForm()}
    if request.method == 'POST':
        formulario = OfertaForm(request.POST)        
        if formulario.is_valid:            
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"  
            time.sleep(2.5)                      
    return render(request, 'nueva_oferta.html', datos)


def ofertas_user(request):
    ofertas = Oferta.objects.all().select_related('fk_id_tipo_cargo')
    print(ofertas)  # Imprime las ofertas en la consola para depuración
    return render(request, 'ofertas_user.html', {'ofertas': ofertas})




# JORDAAAAAAAN--------------------------------------------------------------