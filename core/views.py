from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Oferta, Formulario
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, OfertaForm, FormularioForm
import time
from django import forms
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse




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


def nueva_oferta(request):
    datos = {'form': OfertaForm()}
    if request.method == 'POST':
        formulario = OfertaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
            time.sleep(2.5)
            return redirect('ofertas_admin')
    return render(request, 'nueva_oferta.html', datos)


def ofertas_user(request):
    ofertas = Oferta.objects.all().select_related('fk_id_tipo_cargo')
    print(ofertas)  # Imprime las ofertas en la consola para depuración
    return render(request, 'ofertas_user.html', {'ofertas': ofertas})


def formulario(request, id_oferta, nom_oferta, ):
    datos = {'form': FormularioForm()}
    if request.method == 'POST':
        user_id = request.user.id

        request.POST = request.POST.copy()
        request.POST['fk_id_usuario'] = user_id

        formulario = FormularioForm(request.POST)
        if formulario.is_valid():
            # Aquí debes guardar la información del formulario y redirigir a otra página, o realizar las acciones necesarias.
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
            time.sleep(2.5)
            print("El formulario se ha guardado correctamente")

    return render(request, 'formulario.html', {'id_oferta': id_oferta, 'nom_oferta': nom_oferta})

@login_required
def obtener_id_usuario(request):
    user_id = request.user.id
    return HttpResponse(f'ID del usuario autenticado: {user_id}')


def ofertas_admin(request):
    ofertas = Oferta.objects.all().select_related('fk_id_tipo_cargo')
    print(ofertas)  # Imprime las ofertas en la consola para depuración
    return render(request, 'ofertas_admin.html', {'ofertas': ofertas})


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

def perfil(request):
    return render(request, 'perfil.html')