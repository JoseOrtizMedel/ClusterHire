from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from .forms import InicioForm
from django.contrib.auth import authenticate, login, logout
from django.http import request
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request,'home.html')


# def registro(request):
#     if request.method == 'POST':
#         form = RegistroUsuarioForm(request.POST)
#         if form.is_valid():
#             # Procesa el formulario y guarda al usuario en la base de datos
#             usuario = form.save(commit=False)            
#             usuario.save()
#             return redirect('home')
#     else:
#         form = RegistroUsuarioForm()
#     return render(request, 'registro.html', {'form': form})


def nueva_oferta(request):
    return render(request,'nueva_oferta.html')

def ofertas_admin(request):
    return render(request,'ofertas_admin.html')

def ofertas_user(request):
    return render(request,'ofertas_user.html')
  
# def recuperar_contrasenia(request):
#     return render(request,'recuperar_contrasenia.html')

# def registrar_ncontrasenia(request):
#     return render(request, 'registrar_ncontrasenia.html')

# def login(request):
#     return render(request,'login.html')

# def login(request):
#     if request.method == 'POST':
#         form = InicioForm(request.POST)
#         if form.is_valid():
#             return render (request, "home.html")
#     else:
#             form = InicioForm()
#             messages.error(request, "Algo está mal, revise su correo y/o contraseña")
#             return redirect("home.html")
    
#     return render(request, 'login.html', {'form' : form})


def register(request):
     
    data= {
        'form':CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    return render(request,'registration/register.html', data)