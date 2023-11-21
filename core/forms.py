import time
from django import forms
from django.http import HttpResponse, JsonResponse
from .models import CompetenciaOferta, CompetenciaUsuario, HabilidadUsuario, IdiomaUsuario, Institucion, ModalidadTrabajo, Usuario, UsuarioLogro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from .models import Oferta, TipoCargo, Usuario, Direccion, Comuna, Ciudad, Formulario, Educacion, TituloProf, FormacionAcademica, Experiencia, TipoEmpleo, Competencia, Habilidad, LogroAcademico, Idioma, ModalidadTrabajo


from django.shortcuts import render, redirect


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']


# JORDAAAAAAAN--------------------------------------------------------------




class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['id_oferta','nom_oferta', 'fecha_oferta', 'anhos_experiencia', 'fk_id_tipo_cargo', 'fk_id_modalidad', 'fk_id_comuna']

    fk_id_tipo_cargo = forms.ModelChoiceField(
        queryset=TipoCargo.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_modalidad = forms.ModelChoiceField(
        queryset=ModalidadTrabajo.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_comuna = forms.ModelChoiceField(
        queryset=Comuna.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personaliza las etiquetas del campo fk_id_tipo_cargo
        self.fields['fk_id_tipo_cargo'].label_from_instance = self.label_from_tipo_cargo_instance

        # Personaliza las etiquetas del campo fk_id_modalidad
        self.fields['fk_id_modalidad'].label_from_instance = self.label_from_modalidad_instance

         # Personaliza las etiquetas del campo fk_id_comuna
        self.fields['fk_id_comuna'].label_from_instance = self.label_from_comuna_instance

    def label_from_tipo_cargo_instance(self, obj):
        return obj.nom_cargo

    def label_from_modalidad_instance(self, obj):
        return obj.nom_modalidad

    def label_from_comuna_instance(self, obj):
        return obj.nom_comuna
    

    
class CompeOfeForm (forms.ModelForm):
    class Meta:
        model = CompetenciaOferta
        fields = ['id_comp_oferta','fk_id_oferta','fk_id_competencia']

    fk_id_competencia = forms.ModelChoiceField(
        queryset=Competencia.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class':'form-control'})
    )

    fk_id_oferta = forms.ModelChoiceField(
        queryset=Oferta.objects.all(),  # Asegúrate de que esto sea el modelo correcto
        empty_label=None,
        widget=forms.Select(attrs={'class':'form-control'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_id_competencia'].label_from_instance = self.label_from_competencia_instance

    def label_from_competencia_instance(self, obj):
        return obj.nombre_competencia
    


class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = [
            'id_formulario', 'fecha_formulario', 'pretencion_renta',
            'info_adicional', 'fk_id_usuario', 'fk_id_oferta'
        ]



# JORDAAAAAAAN--------------------------------------------------------------

# ALVARO--------------------------------------------------------------

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=50, required=True,
        label="Usuario",
        error_messages={'required': 'El usuario es obligatorio'})
    password = forms.CharField(widget=forms.PasswordInput, max_length=20,
        label="Contraseña", required=True, 
        error_messages={'required': 'La contraseña es obligatoria'})
        

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['id_direccion','numeracion', 'nombre_calle', 'fk_d_comuna']

    fk_d_comuna = forms.ModelChoiceField(
        queryset=Comuna.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_d_comuna'].label_from_instance = self.label_from_comuna_instance

    def label_from_comuna_instance(self, obj):
        return obj.nom_comuna

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'id_usuario', 'rut_usuario', 'dv_usuario', 'nombre', 'segundo_nombre',
            'primer_apellido', 'segundo_apellido', 'fecha_nacimiento', 'nacionalidad',
            'telefono', 'correo', 'fk_id_direccion']
        
    fk_id_direccion = forms.ModelChoiceField(
        queryset=Direccion.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_id_direccion'].label_from_instance = self.label_from_direccion_instance

    def label_from_direccion_instance(self, obj):
        return obj.id_direccion
        
class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = [
            'id_formulario', 'fecha_formulario', 'pretencion_renta',
            'info_adicional', 'fk_id_usuario', 'fk_id_oferta',
        ]

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['nombre_empleo', 'fecha_inicio_exp', 'fecha_termino_exp', 'descripcion', 'fk_id_comuna', 'fk_id_tipo_empleo', 'fk_id_usuario', 'fk_id_modalidad', 'fk_id_tipo_cargo']

    fk_id_comuna = forms.ModelChoiceField(
        queryset=Comuna.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_tipo_empleo = forms.ModelChoiceField(
        queryset=TipoEmpleo.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_modalidad = forms.ModelChoiceField(
        queryset=ModalidadTrabajo.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_tipo_cargo = forms.ModelChoiceField(
        queryset=TipoCargo.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_id_tipo_empleo'].label_from_instance = self.label_from_tipo_empleo_instance
        self.fields['fk_id_usuario'].label_from_instance = self.label_from_usuario_instance
        self.fields['fk_id_modalidad'].label_from_instance = self.label_from_modalidad_instance
        self.fields['fk_id_comuna'].label_from_instance = self.label_from_comuna_instance
        self.fields['fk_id_tipo_cargo'].label_from_instance = self.label_from_tipoCargo_instance
        
    def label_from_comuna_instance(self, obj):
        return obj.nom_comuna

    def label_from_usuario_instance(self, obj):
        return obj.id_usuario

    def label_from_modalidad_instance(self, obj):
        return obj.nom_modalidad
    
    def label_from_tipo_empleo_instance(self, obj):
        return obj.nom_tipo_empleo
    
    def label_from_tipoCargo_instance(self, obj):
        return obj.nom_cargo
    
class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['id_institucion', 'nombre_institucion', 'tipo_institucion', 'fk_id_direccion']

        fk_id_direccion = forms.ModelChoiceField(
        queryset=Direccion.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_id_direccion'].label_from_instance = self.label_from_direccion_instance

    def label_from_direccion_instance(self, obj):
        return obj.id_direccion

    
class Usuario_logroForm(forms.ModelForm):
    class Meta:
        model = UsuarioLogro
        fields = ['id_usuario_logro', 'fk_id_usuario', 'fk_id_logro_academico']

    fk_id_usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_logro_academico = forms.ModelChoiceField(
        queryset=LogroAcademico.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_id_usuario'].label_from_instance = self.label_from_usuario_instance
        self.fields['fk_id_logro_academico'].label_from_instance = self.label_from_logro_academico_instance

    def label_from_usuario_instance(self, obj):
        return obj.id_usuario

    def label_from_logro_academico_instance(self, obj):
        return obj.nom_logro

class TituloProfForm(forms.ModelForm):
    class Meta:
        model = TituloProf
        fields = ['nombre_titulo', 'descripcion']

class EducacionForm(forms.ModelForm):
    class Meta:
        model = Educacion
        fields = ['id_educacion', 'annio_inicio_educ', 'annio_fin_educ', 'fk_id_usuario', 'fk_id_institucion', 'fk_id_formacion', 'fk_id_titulo']

    fk_id_usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_institucion = forms.ModelChoiceField(
        queryset=Institucion.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_formacion = forms.ModelChoiceField(
        queryset=FormacionAcademica.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_titulo = forms.ModelChoiceField(
    queryset=TituloProf.objects.all(),
    empty_label=None,
    widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_id_usuario'].label_from_instance = self.label_from_usuario_instance
        self.fields['fk_id_institucion'].label_from_instance = self.label_from_institucion_instance
        self.fields['fk_id_formacion'].label_from_instance = self.label_from_formacion_instance
        self.fields['fk_id_titulo'].label_from_instance = self.label_from_titulo_instance

    def label_from_usuario_instance(self, obj):
        return obj.id_usuario

    def label_from_institucion_instance(self, obj):
        return obj.nombre_institucion
    
    def label_from_formacion_instance(self, obj):
        return obj.tipo_formacion
        
    def label_from_titulo_instance(self, obj):
        return obj.nombre_titulo

class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ['nom_comuna', 'fk_id_ciudad']

        fk_id_ciudad = forms.ModelChoiceField(
        queryset=Ciudad.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#        self.fields['fk_id_usuario'].label_from_instance = self.label_from_usuario_instance
        self.fields['fk_id_ciudad'].label_from_instance = self.label_from_ciudad_instance

    def label_from_ciudad_instance(self, obj):
        return obj.nom_ciudad


class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nom_ciudad']
        

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = CompetenciaUsuario
        fields = ['id_compe_usuario', 'fk_id_competencia', 'fk_id_usuario']

    fk_id_competencia = forms.ModelChoiceField(
        queryset=Competencia.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_id_competencia'].label_from_instance = self.label_from_competencia_instance
        self.fields['fk_id_usuario'].label_from_instance = self.label_from_usuario_instance

    def label_from_competencia_instance(self, obj):
        return obj.nombre_competencia

    def label_from_usuario_instance(self, obj):
        return obj.id_usuario
    
    def clean(self):
        # Valida que solo se puedan ingresar como máximo 3 competencias
        competencias = CompetenciaUsuario.objects.filter(fk_id_usuario=self.cleaned_data['fk_id_usuario'])
        if len(competencias) >= 3:
            raise forms.ValidationError("Solo se pueden ingresar como máximo 3 competencias")
        return super().clean()

class IdiomaForm(forms.ModelForm):
    class Meta:
        model = IdiomaUsuario
        fields = ['id_idioma_usuario', 'fk_id_idioma', 'fk_id_usuario']

    fk_id_idioma = forms.ModelChoiceField(
        queryset=Idioma.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_id_usuario'].label_from_instance = self.label_from_usuario_instance
        self.fields['fk_id_idioma'].label_from_instance = self.label_from_idioma_instance

    def label_from_usuario_instance(self, obj):
        return obj.id_usuario

    def label_from_idioma_instance(self, obj):
        return obj.nombre_idioma
    
    def clean(self):
        # Valida que solo se puedan ingresar como máximo 3 idiomas
        idiomas = IdiomaUsuario.objects.filter(fk_id_usuario=self.cleaned_data['fk_id_usuario'])
        if len(idiomas) >= 3:
            raise forms.ValidationError("Solo se pueden ingresar como máximo 3 idiomas")
        return super().clean()

class HabilidadForm(forms.ModelForm):
    class Meta:
        model = HabilidadUsuario
        fields = ['id_habilidad_usuario', 'fk_id_habilidad', 'fk_id_usuario']

    fk_id_habilidad = forms.ModelChoiceField(
        queryset=Habilidad.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_id_habilidad'].label_from_instance = self.label_from_habilidad_instance
        self.fields['fk_id_usuario'].label_from_instance = self.label_from_usuario_instance

    def label_from_habilidad_instance(self, obj):
        return obj.nombre_habilidad

    def label_from_usuario_instance(self, obj):
        return obj.nombre
    
    def clean(self):
        # Valida que solo se puedan ingresar como máximo 3 habilidades
        habilidades = HabilidadUsuario.objects.filter(fk_id_usuario=self.cleaned_data['fk_id_usuario'])
        if len(habilidades) >= 3:
            raise forms.ValidationError("Solo se pueden ingresar como máximo 3 habilidades")
        return super().clean()
    
class PerfilEdit(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [
            "rut_usuario",
            "dv_usuario",
            "nombre",
            "segundo_nombre",
            "primer_apellido",
            "segundo_apellido",
            "fecha_nacimiento",
            "nacionalidad",
            "telefono",
            "correo",
            "fk_id_direccion",
        ]

        labels = {
            'rut_usuario': ('Rut'),
            'dv_usuario': ('DV'),
            'nombre': ('Primer nombre'),
            'segundo_nombre': ('Segundo nombre'),
            'primer_apellido': ('Primer apellido'),
            'segundo_apellido': ('Segundo apellido'),
            'fecha_nacimiento': ('Fecha de nacimiento'),
            'nacionalidad': ('Nacionalidad'),
            'telefono': ('Teléfono'),
            'correo': ('Correo'),
            'fk_id_direccion': ('Dirección'),
        }

        widgets = {
            "rut_usuario": forms.TextInput(attrs={'placeholder': 'Ej: 19638272', 'name': 'rut_usuario', 'id': 'rut_usuario', 'class': 'input-class_name'}),
            "dv_usuario": forms.TextInput(attrs={'placeholder': '(número del 1 al 9 o letra k)', 'name': 'dv_usuario', 'id': 'dv_usuario', 'class': 'input-class_name'}),
            "nombre": forms.TextInput(attrs={'placeholder': 'Ej: Juan', 'name': 'nombre', 'id': 'nombre', 'class': 'input-class_name'}),
            "segundo_nombre": forms.TextInput(attrs={'placeholder': 'Ej: Andrés', 'name': 'segundo_nombre', 'id': 'segundo_nombre', 'class': 'input-class_name'}),
            "primer_apellido": forms.TextInput(attrs={'placeholder': 'Ej: Castro', 'name': 'primer_apellido', 'id': 'primer_apellido', 'class': 'input-class_name'}),
            "segundo_apellido": forms.TextInput(attrs={'placeholder': 'Ej: Gómez', 'name': 'segundo_apellido', 'id': 'segundo_apellido', 'class': 'input-class_name'}),
            "fecha_nacimiento": forms.TextInput(attrs={'placeholder': 'Ej: 2023-07-21', 'name': 'fecha_nacimiento', 'id': 'fecha_nacimiento', 'class': 'input-class_name'}),
            "nacionalidad": forms.TextInput(attrs={'placeholder': 'Ej: Chileno', 'name': 'nacionalidad', 'id': 'nacionalidad', 'class': 'input-class_name'}),
            "telefono": forms.NumberInput(attrs={'placeholder': 'Ej: 32762572', 'name': 'telefono', 'id': 'telefono', 'class': 'input-class_name'}),
            "correo": forms.TextInput(attrs={'placeholder': 'Ej: micorreo@gmail.com', 'name': 'correo', 'id': 'correo', 'class': 'input-class_name'}),
            #"fk_id_direccion": forms.ModelChoiceField(queryset=Comuna.objects.all(),forms.Select(attrs={'class': 'form-control'}))
        }

class DireccionEdit(forms.ModelForm):

    class Meta:
        model = Direccion
        fields = [
            "numeracion",
            "nombre_calle",
            "fk_d_comuna",
        ]

        labels = {
            'numeracion': ('Numeración'),
            'nombre_calle': ('Calle'),
            'fk_d_comuna': ('Comuna'),
        }

        widgets = {
            "numeracion": forms.NumberInput(attrs={'placeholder': 'Ej: 1234', 'name': 'numeracion', 'id': 'numeracion', 'class': 'input-class_name'}),
            "nombre_calle": forms.TextInput(attrs={'placeholder': 'Ej: Av Kennedy', 'name': 'nombre_calle', 'id': 'nombre_calle', 'class': 'input-class_name'}),
        }

    fk_d_comuna = forms.ModelChoiceField(
        queryset=Comuna.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_d_comuna'].label_from_instance = self.label_from_comuna_instance

    def label_from_comuna_instance(self, obj):
        return obj.nom_comuna


class EducEdit(forms.ModelForm):

    class Meta:
        model = Educacion
        fields = [
            "annio_inicio_educ",
            "annio_fin_educ",
            "fk_id_usuario",
            "fk_id_institucion",
            "fk_id_formacion",
            "fk_id_titulo"
        ]

        labels = {
            'annio_inicio_educ': ('Año de inicio'),
            'annio_fin_educ': ('Año de término'),
            'fk_id_usuario': ('Usuario'),
            'fk_id_institucion': ('Institución'),
            'fk_id_formacion': ('Formación'),
            'fk_id_titulo': ('Título'),
        }

        widgets = {
            "annio_inicio_educ": forms.TextInput(attrs={'placeholder': 'Ej: 2020', 'name': 'annio_inicio_educ', 'id': 'annio_inicio_educ', 'class': 'input-class_name'}),
            "annio_fin_educ": forms.TextInput(attrs={'placeholder': 'Ej: 2023', 'name': 'annio_fin_educ', 'id': 'annio_fin_educ', 'class': 'input-class_name'})
        }

    fk_id_usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_institucion = forms.ModelChoiceField(
        queryset=Institucion.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_formacion = forms.ModelChoiceField(
        queryset=FormacionAcademica.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_titulo = forms.ModelChoiceField(
    queryset=TituloProf.objects.all(),
    empty_label=None,
    widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_id_usuario'].label_from_instance = self.label_from_usuario_instance
        self.fields['fk_id_institucion'].label_from_instance = self.label_from_institucion_instance
        self.fields['fk_id_formacion'].label_from_instance = self.label_from_formacion_instance
        self.fields['fk_id_titulo'].label_from_instance = self.label_from_titulo_instance

    def label_from_usuario_instance(self, obj):
        return obj.id_usuario

    def label_from_institucion_instance(self, obj):
        return obj.nombre_institucion
    
    def label_from_formacion_instance(self, obj):
        return obj.tipo_formacion
        
    def label_from_titulo_instance(self, obj):
        return obj.nombre_titulo
    
class ExpEdit(forms.ModelForm):

    class Meta:
        model = Experiencia
        fields = [
            "nombre_empleo",
            "fecha_inicio_exp",
            "fecha_termino_exp",
            "fk_id_comuna",
            "fk_id_tipo_empleo",
            "fk_id_usuario",
            "fk_id_modalidad",
            "fk_id_tipo_cargo",
            "descripcion",
        ]

        labels = {
            'nombre_empleo': ('Fecha de inicio'),
            'fecha_inicio_exp': ('Fecha de término'),
            'fecha_termino_exp': ('Usuario'),
            'fk_id_comuna': ('Comuna'),
            'fk_id_tipo_empleo': ('Tipo empleo'),
            'fk_id_usuario': ('Usuario'),
            'fk_id_modalidad': ('Modalidad'),
            'fk_id_tipo_cargo': ('Cargo'),
            'descripcion': ('Descripción'),
        }

        widgets = {
            "nombre_empleo": forms.TextInput(attrs={'placeholder': 'Ej: Jefe Operaciones Middleware', 'name': 'nombre_empleo', 'id': 'nombre_empleo', 'class': 'input-class_name'}),
            "fecha_inicio_exp": forms.TextInput(attrs={'placeholder': 'Ej: 15/07/2019', 'name': 'fecha_inicio_exp', 'id': 'fecha_inicio_exp', 'class': 'input-class_name'}),
            "fecha_termino_exp": forms.TextInput(attrs={'placeholder': 'Ej: 28/10/2023', 'name': 'fecha_termino_exp', 'id': 'fecha_termino_exp', 'class': 'input-class_name'}),
            "descripcion": forms.Textarea(attrs={'placeholder': 'Ej: Agrega una descripción acerca de esta experiencia laboral...', 'name': 'descripcion', 'id': 'descripcion', 'class': 'input-class_name'})
        }

    fk_id_comuna = forms.ModelChoiceField(
        queryset=Comuna.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_tipo_empleo = forms.ModelChoiceField(
        queryset=TipoEmpleo.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_modalidad = forms.ModelChoiceField(
        queryset=ModalidadTrabajo.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    fk_id_tipo_cargo = forms.ModelChoiceField(
        queryset=TipoCargo.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_id_tipo_empleo'].label_from_instance = self.label_from_tipo_empleo_instance
        self.fields['fk_id_usuario'].label_from_instance = self.label_from_usuario_instance
        self.fields['fk_id_modalidad'].label_from_instance = self.label_from_modalidad_instance
        self.fields['fk_id_comuna'].label_from_instance = self.label_from_comuna_instance
        self.fields['fk_id_tipo_cargo'].label_from_instance = self.label_from_tipoCargo_instance
        
    def label_from_comuna_instance(self, obj):
        return obj.nom_comuna

    def label_from_usuario_instance(self, obj):
        return obj.id_usuario

    def label_from_modalidad_instance(self, obj):
        return obj.nom_modalidad
    
    def label_from_tipo_empleo_instance(self, obj):
        return obj.nom_tipo_empleo
    
    def label_from_tipoCargo_instance(self, obj):
        return obj.nom_cargo