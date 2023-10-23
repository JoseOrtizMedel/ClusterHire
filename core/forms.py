from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class RegistroUsuarioForm(forms.ModelForm):

#     correo = forms.EmailField()
#     contrasenha = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

#     class Meta:
#         model = Usuario
#         fields = ['correo', 'contrasenha', 'nombre', 'primer_apellido', 'telefono']
#         help_texts = {k:"" for k in fields }






class InicioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["correo", "contrasenha"]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']