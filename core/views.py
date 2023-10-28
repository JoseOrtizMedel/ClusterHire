from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Oferta, Formulario, Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CompetenciaForm, CustomUserCreationForm, EducacionForm, ExperienciaForm, HabilidadForm, IdiomaForm, OfertaForm, FormularioForm, Usuario_logroForm, UsuarioForm
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

def perfil(request):
    datos = {
        'form': ExperienciaForm(),
        'formCompetencia': CompetenciaForm(),
        'formUsuarioLogro': Usuario_logroForm(),
        'formIdioma': IdiomaForm(),
        'formHabilidad': HabilidadForm(),
        'formEducacion': EducacionForm(),
        'formUsuario': UsuarioForm(),

        }
    if request.method == 'POST':
        form_experiencia = ExperienciaForm(request.POST)

        if form_experiencia.is_valid():
            form_experiencia.save()

    if request.method == 'POST':
        form_competencia = CompetenciaForm(request.POST)

        if form_competencia.is_valid():
            form_competencia.save()

    if request.method == 'POST':
        form_usuarioLogro = Usuario_logroForm(request.POST)

        if form_usuarioLogro.is_valid():
            form_usuarioLogro.save()

    if request.method == 'POST':
        form_idioma = IdiomaForm(request.POST)

        if form_idioma.is_valid():
            form_idioma.save()

    if request.method == 'POST':
        form_habilidad = HabilidadForm(request.POST)

        if form_habilidad.is_valid():
            form_habilidad.save()

    if request.method == 'POST':
        form_educacion = EducacionForm(request.POST)

        if form_educacion.is_valid():
            form_educacion.save()

    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST)

        if form_usuario.is_valid():
            form_usuario.save()

        datos['mensaje'] = "Guardado Correctamente"
        time.sleep(2.5)
        return redirect('home')
    return render(request, 'perfil.html', datos)