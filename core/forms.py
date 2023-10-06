from django import forms
from django.forms import ModelForm
from .models import Oferta



class OfertaForm(ModelForm):

    class Meta:
        model = Oferta
        fields = ['id_oferta','nom_oferta','descripcion_oferta','fecha_oferta', 'fk_id_tipo_cargo']



