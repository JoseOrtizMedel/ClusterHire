from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):

    correo = forms.EmailField()
    contrasenha = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['correo', 'contrasenha', 'nombre', 'primer_apellido', 'telefono']
        help_texts = {k:"" for k in fields }