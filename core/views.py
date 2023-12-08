

import locale
from random import randint
from django import forms
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect


from .models import Ciudad, CompetenciaUsuario, Comuna, Direccion, Educacion, Experiencia, FormacionAcademica, Habilidad, HabilidadUsuario, Idioma, IdiomaUsuario, Institucion, ModalidadTrabajo, Oferta, Formulario, TipoCargo, TipoEmpleo, TituloProf, Usuario, Competencia, UsuarioLogro

from .models import Ciudad, CompetenciaUsuario, Comuna, Direccion, Educacion, Experiencia, Formulario, HabilidadUsuario, IdiomaUsuario, Oferta, Usuario, Competencia, UsuarioLogro


from .models import CompetenciaOferta, CompetenciaUsuario, Direccion, Educacion, Experiencia, HabilidadUsuario, IdiomaUsuario, Oferta, Usuario, Competencia, UsuarioLogro

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CompetenciaForm, CustomUserCreationForm, DireccionEdit, DireccionForm, EducEdit, EducacionForm, ExpEdit, ExperienciaForm, HabilidadForm, IdiomaForm, LoginForm, PerfilEdit,  Usuario_logroForm, UsuarioForm, OfertaForm, FormularioForm, CompeOfeForm

import time
import locale

from django.db.models import Count

def is_superadmin(user):
    return user.is_superuser

#---- Error 404:
def error_404(request):
    context = {}
    response = render(request, '404.html', context=context)
    response.status_code = 404
    return response

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            user = authenticate(request, username=usuario, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('ofertas_admin')
                if user.is_active:
                    login(request, user)
                    return redirect('perfil_user')
                else:
                    return HttpResponse("Cuenta deshabilitada")
            else:
                return redirect('404')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


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
            return redirect('perfil_user')
    return render(request, 'registration/register.html', data)

# JORDAAAAAAAN--------------------------------------------------------------

@login_required
def obtener_id_usuario(request):
    user_id = request.user.id
    return HttpResponse(f'ID del usuario autenticado: {user_id}')

def nueva_oferta(request):

    datos = {
        'oferta_form': OfertaForm()
    }

    if request.method == 'POST':
        oferta_formulario = OfertaForm(request.POST)

        if oferta_formulario.is_valid(): 

            # Guarda la oferta
            oferta = oferta_formulario.save()

            datos['mensaje'] = "Guardado Correctamente"
            time.sleep(2.5)
            return redirect('ofertas_admin')

    return render(request, 'nueva_oferta.html', datos)


@login_required
def compe_oferta(request, id_oferta, nom_oferta):
    # Crea un formulario vacío
    compeofe_formulario = CompeOfeForm()
    message_error = ''

    # Si la solicitud es POST, valida el formulario
    if request.method == 'POST':
        # Crea un formulario con los datos del formulario enviado
        compeofe_formulario = CompeOfeForm(request.POST)

        # Si el formulario es válido, guarda los datos
        if compeofe_formulario.is_valid():
            # Obtiene la competencia del formulario
            competencia = compeofe_formulario.cleaned_data['fk_id_competencia']

            # Verifica si la competencia ya existe
            competencia_existente = CompetenciaOferta.objects.filter(fk_id_oferta=id_oferta, fk_id_competencia=competencia).first()

            # Si la competencia no existe, la guarda
            if not competencia_existente:
                # Guarda el formulario
                compeofe_formulario.save()

                # Redirecciona al usuario a la página de administración de ofertas
                return redirect('ofertas_admin')

            # Si la competencia existe, muestra un mensaje de error
            else:
                # Muestra el mensaje de error
                message_error = 'La competencia ya existe'

    # Obtén las competencias disponibles
    competencias_disponibles = Competencia.objects.all()

    # Devuelve la plantilla de la página
    return render(request, 'compe_oferta.html', {'id_oferta': id_oferta, 'nom_oferta': nom_oferta, 'compeofe_form': compeofe_formulario, 'competencias': competencias_disponibles, 'message_error': message_error})



def formulario(request, id_oferta, nom_oferta, ):
    datos = {'form': FormularioForm(request)}
    message_error = ''

    if request.method == 'POST':
        user_id = request.user.id

        request.POST = request.POST.copy()
        request.POST['fk_id_usuario'] = user_id

        formulario = FormularioForm(request.POST)
        if formulario.is_valid():
            # Aquí debes guardar la información del formulario y redirigir a otra página, o realizar las acciones necesarias.
            formulario.fk_id_usuario = request.user.id
            formulario.fk_id_oferta = id_oferta  # O cualquier otro valor que desees

            formulario_existente = Formulario.objects.filter(fk_id_oferta=id_oferta, fk_id_usuario=request.user.id).first()

            if not formulario_existente:

                formulario.save()
                datos['mensaje'] = "Guardado Correctamente"
                time.sleep(2.5)
                print("El formulario se ha guardado correctamente")
                return redirect('ofertas_user')
            
            else:
                message_error = 'Ya postulaste a esta oferta'

    return render(request, 'formulario.html', {'id_oferta': id_oferta, 'nom_oferta': nom_oferta, 'message_error': message_error})
    

def ciencia(request, id_oferta, nom_oferta, ):
    context = {
        'id_oferta': id_oferta,
        'nom_oferta': nom_oferta,
        # Otros datos que quieras pasar al contexto
    }
    return render(request, 'ciencia.html', context)

@login_required
def obtener_conteo_formularios():
    conteo_formularios = Oferta.objects.annotate(num_postulantes=Count('formulario'))
    return conteo_formularios


#@user_passes_test(is_superadmin)
def ofertas_admin(request):    

    ofertas = Oferta.objects.all().select_related('fk_id_tipo_cargo').prefetch_related('competenciaoferta_set__fk_id_competencia')
    ofertas = Oferta.objects.annotate(num_formularios=Count('formulario'))

    return render(request, 'ofertas_admin.html', {'ofertas': ofertas})

def ofertas_user(request):
    ofertas = Oferta.objects.all().select_related('fk_id_tipo_cargo').prefetch_related('competenciaoferta_set__fk_id_competencia')
    print(ofertas)  # Imprime las ofertas en la consola para depuración
    return render(request, 'ofertas_user.html', {'ofertas': ofertas}) 
 

import traceback
@login_required
@csrf_exempt
def eliminar_oferta(request, id_oferta):
    if request.method == 'POST':
        try:
            oferta = Oferta.objects.get(id_oferta=id_oferta)

            # Eliminar formularios asociados a la oferta
            Formulario.objects.filter(fk_id_oferta=oferta).delete()

            # Eliminar las relaciones CompetenciaOferta relacionadas
            CompetenciaOferta.objects.filter(fk_id_oferta=oferta).delete()

            # Finalmente, elimina la oferta
            oferta.delete()

            return JsonResponse({'success': True})
        except Oferta.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Oferta no encontrada'})
        except Exception as e:
            traceback.print_exc()
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False})

def perfil_admin(request, id_usuario, id_oferta):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    
    try:
        id_user = id_usuario
        usuarios = Usuario.objects.get(id_usuario = id_user)

        #id_dire = usuarios.fk_id_direccion_id
        #direcciones =Direccion.objects.get(id_direccion = id_dire)

        #id_comu = direcciones.fk_d_comuna_id
        #comunas = Comuna.objects.get(id_comuna = id_comu)

        #id_ciu = comunas.fk_id_ciudad_id
        #ciudades = Ciudad.objects.get(id_ciudad = id_ciu)

        compesuser = CompetenciaUsuario.objects.filter(fk_id_usuario=id_user)
        competencias = Competencia.objects.filter(competenciausuario__in=compesuser)

        habiuser = HabilidadUsuario.objects.filter(fk_id_usuario=id_user)
        habilidades = Habilidad.objects.filter(habilidadusuario__in=habiuser)

        idiouser = IdiomaUsuario.objects.filter(fk_id_usuario=id_user)
        idiomas = Idioma.objects.filter(idiomausuario__in=idiouser)
   
        experiencias = Experiencia.objects.filter(fk_id_usuario=id_user)

        fkempleos = experiencias.values_list('fk_id_tipo_empleo', flat=True)
        empleos = TipoEmpleo.objects.filter(id_tipo_empleo__in=fkempleos)

        fkcargos = experiencias.values_list('fk_id_tipo_cargo', flat=True)
        cargos = TipoCargo.objects.filter(id_tipo_cargo__in=fkcargos)

        fkmodalidad = experiencias.values_list('fk_id_modalidad', flat=True)
        modalidades = ModalidadTrabajo.objects.filter(id_modalidad__in = fkmodalidad)


        educaciones = Educacion.objects.filter(fk_id_usuario=id_user)

        fkforma = educaciones.values_list('fk_id_formacion', flat=True)
        formaciones = FormacionAcademica.objects.filter(id_formacion__in=fkforma)

        fktitu = educaciones.values_list('fk_id_titulo', flat=True)
        titulos = TituloProf.objects.filter(id_titulo__in=fktitu)

        fkinsti = educaciones.values_list('fk_id_institucion', flat=True).first()
        instituciones = Institucion.objects.filter(id_institucion=fkinsti)




    except Usuario.DoesNotExist:
        # Manejar el caso en el que el usuario no se encuentre
        print("No se encontró un usuario")

    datos = {
        'id_user' : id_user,
        'id_oferta' : id_oferta,
        'usuarios' : usuarios,
        #'direcciones' : direcciones,
        #'comunas' : comunas,
        #'ciudades' : ciudades,
        'compesuser' : compesuser,
        'competencias' : competencias,
        'habilidades' : habilidades,
        'idiomas' : idiomas,
        'experiencias' : experiencias,
        'empleos' : empleos,
        'cargos' : cargos,
        'modalidades' : modalidades,
        'educaciones' : educaciones,
        'formaciones' : formaciones,
        'titulos' : titulos,
        'instituciones' : instituciones
    }


    if empleos.exists():
        modalidades = modalidades.first()
        print(modalidades.nom_modalidad)
    else:        
        print("No se encontró información sobre el tipo de empleo.")


    return render(request, 'perfil_admin.html', datos)

# JORDAAAAAAAN--------------------------------------------------------------

# ALVARO--------------------------------------------------------------

def perfil_user(request):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    
    # Obtiene las competencias del usuario
    competencias = CompetenciaUsuario.objects.filter(fk_id_usuario=request.user.id)

    # Obtiene las habilidades del usuario
    habilidades = HabilidadUsuario.objects.filter(fk_id_usuario=request.user.id)

    # Obtiene los idiomas del usuario
    idiomas = IdiomaUsuario.objects.filter(fk_id_usuario=request.user.id)

    # Obtiene la educación del usuario
    educaciones = Educacion.objects.filter(fk_id_usuario=request.user.id)

    # Obtiene la educación del usuario
    logros = UsuarioLogro.objects.filter(fk_id_usuario=request.user.id)

    # Obtiene la experiencia laboral del usuario
    experiencias = Experiencia.objects.filter(fk_id_usuario=request.user.id)

    # Obtiene al usuario (columna dirección)
    usuarios = Usuario.objects.filter(id_usuario=request.user.id)


    datos = {
        'competencia_form': CompetenciaForm(),
        'habilidad_form': HabilidadForm(),
        'idioma_form': IdiomaForm(),
        'educacion_form': EducacionForm(),
        'logros_form': Usuario_logroForm(),
        'exps_form': ExperienciaForm(),
        'u_dires_form': UsuarioForm(),

    }

    # Agrega las competencias a los datos
    datos['competencias'] = competencias
    datos['habilidades'] = habilidades
    datos['idiomas'] = idiomas
    datos['educaciones'] = educaciones
    datos['logros'] = logros
    datos['experiencias'] = experiencias
    datos['usuarios'] = usuarios

    if request.method == 'POST':
        form_competencia = CompetenciaForm(request.POST)
        form_habilidad = HabilidadForm(request.POST)
        form_idioma = IdiomaForm(request.POST)
        form_educacion = EducacionForm(request.POST)
        form_logro = Usuario_logroForm(request.POST)
        form_experiencia = ExperienciaForm(request.POST)
        form_usuarios = UsuarioForm(request.POST)
        
        if form_usuarios.is_valid():

            # Asigna la instancia de Usuario
            form_usuario_instance = form_usuarios.save(commit=False)

            # Asigna el valor request.user.id a la propiedad id_usuario
            form_usuario_instance.id_usuario = request.user.id

            # Ahora guarda la instancia de Usuario
            form_usuario_instance.save()

            datos['mensaje'] = "Guardado Correctamente"
            time.sleep(2.5)
            return redirect('perfil_user')
        
        if form_competencia.is_valid():

            # Obtiene la competencia del formulario
            competencia = form_competencia.cleaned_data['fk_id_competencia']

            # Verifica si la competencia ya existe
            competencia_existente = CompetenciaUsuario.objects.filter(fk_id_usuario=request.user.id, fk_id_competencia=competencia).first()

            # Verifica si la competencia es nueva
            if not competencia_existente:
                # La competencia es nueva
                form_competencia.save()

                datos['mensaje'] = "Guardado Correctamente"
                time.sleep(2.5)
                return redirect('perfil_user')
            else:
                # La competencia ya existe
                # Muestra un mensaje de validación
                datos['mensaje'] = "La competencia ya existe"

        if form_habilidad.is_valid():

            # Obtiene la competencia del formulario
            habilidad = form_habilidad.cleaned_data['fk_id_habilidad']

            # Verifica si la competencia ya existe
            habilidad_existente = HabilidadUsuario.objects.filter(fk_id_usuario=request.user.id, fk_id_habilidad=habilidad).first()

            # Verifica si la competencia es nueva
            if not habilidad_existente:
                # La competencia es nueva
                form_habilidad.save()

                datos['mensaje'] = "Guardado Correctamente"
                time.sleep(2.5)
                return redirect('perfil_user')
            else:
                # La competencia ya existe
                # Muestra un mensaje de validación
                datos['mensaje'] = "La habilidad ya existe"

        if form_idioma.is_valid():

            # Obtiene la competencia del formulario
            idioma = form_idioma.cleaned_data['fk_id_idioma']

            # Verifica si la competencia ya existe
            idioma_existente = IdiomaUsuario.objects.filter(fk_id_usuario=request.user.id, fk_id_idioma=idioma).first()

            # Verifica si la competencia es nueva
            if not idioma_existente:
                # La competencia es nueva
                form_idioma.save()

                datos['mensaje'] = "Guardado Correctamente"
                time.sleep(2.5)
                return redirect('perfil_user')
            else:
                # La competencia ya existe
                # Muestra un mensaje de validación
                datos['mensaje'] = "El idioma ya existe"
    
        if form_educacion.is_valid():

            form_educacion.save()

            datos['mensaje'] = "Guardado Correctamente"
            time.sleep(2.5)
            return redirect('perfil_user')

        if form_logro.is_valid():

            # Obtiene la competencia del formulario
            logro = form_logro.cleaned_data['fk_id_logro_academico']

            # Verifica si la competencia ya existe
            logro_existente = UsuarioLogro.objects.filter(fk_id_usuario=request.user.id, fk_id_logro_academico=logro).first()

            # Verifica si la competencia es nueva
            if not logro_existente:
                # La competencia es nueva
                form_logro.save()

                datos['mensaje'] = "Guardado Correctamente"
                time.sleep(2.5)
                return redirect('perfil_user')
            else:
                # La competencia ya existe
                # Muestra un mensaje de validación
                datos['mensaje'] = "La competencia ya existe"
        
        if form_experiencia.is_valid():

            form_experiencia.save()

            datos['mensaje'] = "Guardado Correctamente"
            time.sleep(2.5)
            return redirect('perfil_user')

    return render(request, 'perfil_user.html', datos)

#Vista para eliminar Competencias
@login_required
def eliminar_compes(request, pk):

    var = CompetenciaUsuario.objects.get(id_compe_usuario=pk)

    var.delete()

    return redirect(to="perfil_user")

#Vista para eliminar Habilidades
@login_required
def eliminar_habis(request, pk):

    var = HabilidadUsuario.objects.get(id_habilidad_usuario=pk)

    var.delete()

    return redirect(to="perfil_user")

#Vista para eliminar Idiomas
@login_required
def eliminar_idiomas(request, pk):

    var = IdiomaUsuario.objects.get(id_idioma_usuario=pk)

    var.delete()

    return redirect(to="perfil_user")

#Vista para eliminar Educación
@login_required
def eliminar_educacion(request, pk):

    var = Educacion.objects.get(id_educacion=pk)

    var.delete()

    return redirect(to="perfil_user")

#Vista para eliminar Logros Académicos
@login_required
def eliminar_logros(request, pk):

    var = UsuarioLogro.objects.get(id_usuario_logro=pk)

    var.delete()

    return redirect(to="perfil_user")

#Vista para eliminar Experiencia Laboral
@login_required
def eliminar_exps(request, pk):

    var = Experiencia.objects.get(id_experiencia=pk)

    var.delete()

    return redirect(to="perfil_user")


#---- Editar Educación:

def edit_educacion(request, pk):
    educacion = Educacion.objects.get(id_educacion=pk)

    datos = {
        'form': EducEdit(instance=educacion) 
    }

    if request.method == 'POST':
        formulario_edit = EducEdit(request.POST, request.FILES, instance=educacion)
        if formulario_edit.is_valid:
            formulario_edit.save()
            return redirect(to="perfil_user")

    else:
        datos = {
            'form': EducEdit(instance=educacion) 
        }
        return render(request, 'perfil_educacion_edit.html', datos)
    
#---- Editar Experiencia Laboral:

def edit_experiencia(request, pk):
    experiencia = Experiencia.objects.get(id_experiencia=pk)

    datos = {
        'form': ExpEdit(instance=experiencia) 
    }

    if request.method == 'POST':
        formulario_edit = ExpEdit(request.POST, request.FILES, instance=experiencia)
        if formulario_edit.is_valid:
            formulario_edit.save()
            return redirect(to="perfil_user")

    else:
        datos = {
            'form': ExpEdit(instance=experiencia) 
        }
        return render(request, 'perfil_experiencia_edit.html', datos)
    
#---- Editar Dirección:

def edit_direccion(request, pk):
    direccion = Direccion.objects.get(id_direccion=pk)

    datos = {
            'form': DireccionEdit(instance=direccion) 
    }

    if request.method == 'POST':
        formulario_edit = DireccionEdit(request.POST, request.FILES, instance=direccion)
        if formulario_edit.is_valid:
            formulario_edit.save()
            return redirect(to="perfil_user")

    else:
        datos = {
            'form': DireccionEdit(instance=direccion) 
        }
        return render(request, 'perfil_direccion_edit.html', datos)
    
#---- Editar Datos personales:
    
def edit_personal(request, pk):
    
    personal = Usuario.objects.get(id_usuario=pk)

    datos = {
        'form': PerfilEdit(instance=personal) 
    }

    if request.method == 'POST':
        formulario = PerfilEdit(data=request.POST, files=request.FILES, instance=personal)
        if formulario.is_valid():
            formulario.save()
            return redirect('perfil_user')
            
        else:
            datos = {
                'form': PerfilEdit(instance=personal) 
            }

    return render(request, 'perfil_personal_edit.html', datos)