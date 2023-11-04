from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Oferta, Formulario, CompetenciaOferta
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, OfertaForm, FormularioForm, CompeOfeForm
import time
from django import forms

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.db.models import Count
from django.db import connection




def home(request):
    return render(request, 'home.html')

def register(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(
                username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    return render(request, 'registration/register.html', data)

# JORDAAAAAAAN--------------------------------------------------------------

@login_required
def obtener_id_usuario(request):
    user_id = request.user.id
    return HttpResponse(f'ID del usuario autenticado: {user_id}')


def nueva_oferta(request):
    datos = {
        'oferta_form': OfertaForm(),
        'compeofe_form': CompeOfeForm()
    }

    if request.method == 'POST':
        oferta_formulario = OfertaForm(request.POST)
        compeofe_formulario = CompeOfeForm(request.POST)

        if oferta_formulario.is_valid()  and compeofe_formulario.is_valid(): 

            # Guarda la oferta
            oferta = oferta_formulario.save()

            # Obtén la instancia de CompetenciaOferta sin guardarla todavía
            compeofe_instance = compeofe_formulario.save(commit=False)

            # Establece el campo fk_id_oferta como la instancia de la oferta
            compeofe_instance.fk_id_oferta = oferta

            # Ahora guarda la instancia de CompetenciaOferta
            compeofe_instance.save()

            datos['mensaje'] = "Guardado Correctamente"
            time.sleep(2.5)
            return redirect('ofertas_admin')

    return render(request, 'nueva_oferta.html', datos)




def formulario(request, id_oferta, nom_oferta, ):
    datos = {'form': FormularioForm()}
    if request.method == 'POST':
        user_id = request.user.id

        request.POST = request.POST.copy()
        request.POST['fk_id_usuario'] = user_id

        formulario = FormularioForm(request.POST)
        if formulario.is_valid():
            # Aquí debes guardar la información del formulario y redirigir a otra página, o realizar las acciones necesarias.
            formulario.fk_id_usuario = request.user.id
            formulario.fk_id_oferta = id_oferta  # O cualquier otro valor que desees

            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
            time.sleep(2.5)
            print("El formulario se ha guardado correctamente")
            return redirect('ofertas_user')
    return render(request, 'formulario.html', {'id_oferta': id_oferta, 'nom_oferta': nom_oferta})

def obtener_conteo_formularios():
    conteo_formularios = Oferta.objects.annotate(num_postulantes=Count('formulario'))
    return conteo_formularios

def ofertas_admin(request):
    ofertas = Oferta.objects.all().select_related('fk_id_tipo_cargo').prefetch_related('competenciaoferta_set__fk_id_competencia')
    ofertas = Oferta.objects.annotate(num_formularios=Count('formulario'))
    print(ofertas)  # Imprime las ofertas en la consola para depuración
    return render(request, 'ofertas_admin.html', {'ofertas': ofertas})

def ofertas_user(request):
    ofertas = Oferta.objects.all().select_related('fk_id_tipo_cargo').prefetch_related('competenciaoferta_set__fk_id_competencia')
    print(ofertas)  # Imprime las ofertas en la consola para depuración
    return render(request, 'ofertas_user.html', {'ofertas': ofertas}) 
 

@csrf_exempt
def eliminar_oferta(request, id_oferta):
    # Verifica si el ID de la oferta existe en la base de datos
    oferta = get_object_or_404(Oferta, id_oferta=id_oferta)

    if request.method == 'POST':
        # Realiza la lógica para eliminar la oferta
        oferta.delete()
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

@csrf_exempt
def eliminar_oferta(request, id_oferta):
    if request.method == 'POST':
        try:
            oferta = Oferta.objects.get(id_oferta=id_oferta)
            # Eliminar las relaciones CompetenciaOferta relacionadas
            CompetenciaOferta.objects.filter(fk_id_oferta=oferta).delete()
            oferta.delete()
            return JsonResponse({'success': True})
        except Oferta.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Oferta no encontrada'})
    return JsonResponse({'success': False})




# JORDAAAAAAAN--------------------------------------------------------------

def perfil(request):
    return render(request, 'perfil.html')