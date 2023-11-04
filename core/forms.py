from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Oferta, ModalidadTrabajo, TipoCargo, Usuario, Direccion, Comuna, Ciudad, Formulario, Educacion, TituloProf, FormacionAcademica, Experiencia, TipoEmpleo, Competencia, Habilidad, LogroAcademico, Idioma, CompetenciaOferta


from django.shortcuts import render, redirect

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']



# JORDAAAAAAAN--------------------------------------------------------------




class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['nom_oferta', 'fecha_oferta', 'anhos_experiencia', 'fk_id_tipo_cargo', 'fk_id_modalidad', 'fk_id_comuna']

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

        # Personaliza las etiquetas del campo fk_id_competencia
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