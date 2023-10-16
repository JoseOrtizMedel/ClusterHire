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

  
def recuperar_contrasenia(request):
    return render(request,'recuperar_contrasenia.html')

def registrar_ncontrasenia(request):
    return render(request, 'registrar_ncontrasenia.html')

def login(request):
    return render(request,'login.html')

def formulario(request):
    return render(request,'formulario.html')


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

def ofertas_admin(request):
    ofertas = Oferta.objects.all().select_related('fk_id_tipo_cargo')
    print(ofertas)  # Imprime las ofertas en la consola para depuración
    return render(request, 'ofertas_admin.html', {'ofertas': ofertas})

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def eliminar_oferta(request, id_oferta):
    # Verifica si el ID de la oferta existe en la base de datos
    oferta = get_object_or_404(Oferta, id_oferta=id_oferta)
    
    if request.method == 'POST':
        # Realiza la lógica para eliminar la oferta
        oferta.delete()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})

from django.shortcuts import render
from django.http import request
from .models import Oferta
from .forms import OfertaForm
from django import forms

# Otras importaciones...

def formulario(request, nombre_oferta):  # Agregar 'nombre_oferta' como parámetro
    # Otras operaciones si es necesario...
    return render(request, 'formulario.html', {'nombre_oferta': nombre_oferta})




# JORDAAAAAAAN--------------------------------------------------------------