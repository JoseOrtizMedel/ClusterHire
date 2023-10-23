from django.shortcuts import render, redirect
from django.http import request
from .models import Oferta, Formulario
from .forms import OfertaForm, FormularioForm
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
            return redirect('ofertas_admin')                   
    return render(request, 'nueva_oferta.html', datos)


def ofertas_user(request):
    ofertas = Oferta.objects.all().select_related('fk_id_tipo_cargo')
    print(ofertas)  # Imprime las ofertas en la consola para depuración
    return render(request, 'ofertas_user.html', {'ofertas': ofertas})


def formulario(request, id_oferta, nom_oferta):
    datos = {'form': FormularioForm()}
    if request.method == 'POST':
        formulario = FormularioForm(request.POST)
        if formulario.is_valid():
            # Aquí debes guardar la información del formulario y redirigir a otra página, o realizar las acciones necesarias.
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
            time.sleep(2.5)
                    
    return render(request, 'formulario.html',{'id_oferta': id_oferta ,'nom_oferta': nom_oferta})




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




# JORDAAAAAAAN--------------------------------------------------------------