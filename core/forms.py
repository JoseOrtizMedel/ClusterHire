from django import forms
from django.forms import ModelForm
from .models import Oferta, TipoCargo


class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['nom_oferta', 'descripcion_oferta', 'fecha_oferta', 'fk_id_tipo_cargo']

    fk_id_tipo_cargo = forms.ModelChoiceField(
        queryset=TipoCargo.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza las etiquetas del campo fk_id_tipo_cargo
        self.fields['fk_id_tipo_cargo'].label_from_instance = self.label_from_tipo_cargo_instance

    def label_from_tipo_cargo_instance(self, obj):
        return obj.nom_cargo
