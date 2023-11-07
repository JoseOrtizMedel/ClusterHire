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
    usuario = UsuarioForm()       

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

    
class Usuario_logroForm(forms.ModelForm):
    class Meta:
        model = UsuarioLogro
        fields = ['id_usuario_logro', 'fk_id_usuario', 'fk_id_logro_academico']

    pf_id_usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    pf_id_logro_academico = forms.ModelChoiceField(
        queryset=LogroAcademico.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_id_usuario'].label_from_instance = self.label_from_usuario_instance
        self.fields['fk_id_logro_academico'].label_from_instance = self.label_from_logro_academico_instance

    def label_from_usuario_instance(self, obj):
        return obj.nombre

    def label_from_logro_academico_instance(self, obj):
        return obj.nom_logro
    
class IdiomaForm(forms.ModelForm):
    class Meta:
        model = IdiomaUsuario
        fields = ['id_idioma_usuario', 'fk_id_idioma', 'fk_id_usuario']

    pf_id_idioma = forms.ModelChoiceField(
        queryset=Idioma.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    pf_id_usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#        self.fields['pf_id_usuario'].label_from_instance = self.label_from_usuario_instance
        self.fields['fk_id_idioma'].label_from_instance = self.label_from_idioma_instance

#    def label_from_usuario_instance(self, obj):
#        return obj.nombre

    def label_from_idioma_instance(self, obj):
        return obj.nombre_idioma

class TituloProfForm(forms.ModelForm):
    class Meta:
        model = TituloProf
        fields = ['nombre_titulo', 'descripcion']
            
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
#        self.fields['fk_id_usuario'].label_from_instance = self.label_from_usuario_instance
        self.fields['fk_id_institucion'].label_from_instance = self.label_from_institucion_instance
        self.fields['fk_id_formacion'].label_from_instance = self.label_from_formacion_instance
        self.fields['fk_id_titulo'].label_from_instance = self.label_from_titulo_instance

#    def label_from_usuario_instance(self, obj):
#        return obj.nombre_habilidad

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
        


  