from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from .forms import RegistroUsuarioForm

# Create your views here.
def home(request):
    return render(request,'home.html')


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            # Procesa el formulario y guarda al usuario en la base de datos
            usuario = form.save(commit=False)            
            usuario.save()
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})


def nueva_oferta(request):
    return render(request,'nueva_oferta.html')

def ofertas_admin(request):
    return render(request,'ofertas_admin.html')

def ofertas_user(request):
    return render(request,'ofertas_user.html')
  
def recuperar_contrasenia(request):
    return render(request,'recuperar_contrasenia.html')

def registrar_ncontrasenia(request):
    return render(request, 'registrar_ncontrasenia.html')

def login(request):
    return render(request,'login.html')
