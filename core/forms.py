from django import forms
from .models import Usuario

class InicioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["correo", "contrasenha"]

""" class InicioForm(forms.Form):
    email = forms.EmailField
    password = forms.PasswordInput """