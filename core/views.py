from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Oferta, Formulario, Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CiudadForm, CompetenciaForm, ComunaForm, CustomUserCreationForm, DireccionForm, EducacionForm, ExperienciaForm, HabilidadForm, IdiomaForm, OfertaForm, FormularioForm, TituloProfForm, Usuario_logroForm, UsuarioForm
import time

# Create your views here.


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

    return render(request, 'formulario.html', {'id_oferta': id_oferta, 'nom_oferta': nom_oferta})


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

# ALVARO--------------------------------------------------------------

def perfilPers(request):
    datos = {
        'usuario_form': UsuarioForm(),
        'direccion_form': DireccionForm(),
        'experiencia_form': ExperienciaForm(),
        
        }

    if request.method == 'POST':
        form_direccion = DireccionForm(request.POST)
        form_usuario = UsuarioForm(request.POST)
        form_experiencia = ExperienciaForm(request.POST)

        if form_direccion.is_valid()  and form_usuario.is_valid() and form_experiencia.is_valid(): 

        #----------FormUsuario y FormDireccion (fk)-------------------------#

            # Guarda la dirección
            direccion = form_direccion.save()

            # Obtén la instancia de Usuario sin guardarla todavía
            form_usuario_instance = form_usuario.save(commit=False)

            # Establece el campo fk_id_direccion como la instancia de la direccion
            form_usuario_instance.fk_id_direccion = direccion

            # Ahora guarda la instancia de Usuario
            form_usuario_instance.save()

            #----------FormExperiencia y FormUsuario (fk)-------------------------#

            usuario = form_usuario.save()

            form_experiencia_instance = form_experiencia.save(commit=False)

            form_experiencia_instance.fk_id_usuario = usuario

            form_experiencia_instance.save()

            datos['mensaje'] = "Guardado Correctamente"
            time.sleep(2.5)
            return redirect('home')

    return render(request, 'perfil.html', datos)

#def perfilExp(request):
#    datos = {
#        'experiencia_form': ExperienciaForm(),

#        }

#    if request.method == 'POST':
#        form_usuario = UsuarioForm(request.POST)
#        form_experiencia = ExperienciaForm(request.POST)

#        if form_experiencia.is_valid(): 

#            usuario = form_usuario.save()

#            form_experiencia_instance = form_experiencia.save(commit=False)

#            form_experiencia_instance.fk_id_usuario = usuario

#            form_experiencia_instance.save()

#            datos['mensaje'] = "Guardado Correctamente"
#            time.sleep(2.5)
#            return redirect('home')

#    return render(request, 'perfil.html', datos)
