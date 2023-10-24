from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Oferta, ModalidadTrabajo, TipoCargo, Usuario, Direccion, Comuna, Ciudad, Formulario, Educacion, TituloProf, FormacionAcademica, Experiencia, TipoEmpleo, Competencia, Habilidad, LogroAcademico, Idioma


from django.shortcuts import render, redirect

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']



# JORDAAAAAAAN--------------------------------------------------------------

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['id_oferta', 'nom_oferta', 'fecha_oferta', 'anhos_experiencia', 'fk_id_tipo_cargo', 'fk_id_modalidad', 'fk_id_comuna']

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
    
class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = [
            'id_formulario', 'fecha_formulario', 'pretencion_renta',
            'info_adicional', 'fk_id_usuario', 'fk_id_oferta',
        ]


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['numeracion', 'nombre_calle', 'fk_d_comuna']

        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'id_usuario', 'rut_usuario', 'dv_usuario', 'nombre', 'segundo_nombre',
            'primer_apellido', 'segundo_apellido', 'fecha_nacimiento', 'nacionalidad',
            'telefono', 'correo', 'fk_id_direccion',
        ]
    direccion = DireccionForm()  # Agrega el formulario de dirección como subformulario









class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ['nom_comuna', 'fk_id_ciudad']

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nom_ciudad']



class EducacionForm(forms.ModelForm):
    class Meta:
        model = Educacion
        fields = [
            'annio_inicio_educ', 'annio_fin_educ', 'fk_id_usuario', 'fk_id_institucion',
            'fk_id_formacion',
        ]

class TituloProfForm(forms.ModelForm):
    class Meta:
        model = TituloProf
        fields = ['nombre_titulo', 'descripcion', 'fk_id_educacion']

class FormacionAcademicaForm(forms.ModelForm):
    class Meta:
        model = FormacionAcademica
        fields = ['tipo_formacion']

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = [
            'cargo_empleo', 'nombre_empleo', 'fecha_inicio_exp',
            'fecha_termino_exp', 'descripcion', 'fk_id_comuna', 'fk_id_tipo_empleo',
            'fk_id_usuario',
        ]

class TipoEmpleoForm(forms.ModelForm):
    class Meta:
        model = TipoEmpleo
        fields = ['nom_tipo_empleo']

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nombre_competencia']


class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = ['nombre_habilidad']

class LogroAcademicoForm(forms.ModelForm):
    class Meta:
        model = LogroAcademico
        fields = ['nom_logro', 'descripcion_logro']

class IdiomaForm(forms.ModelForm):
    class Meta:
        model = Idioma
        fields = ['nombre_idioma']
    
# JORDAAAAAAAN--------------------------------------------------------------