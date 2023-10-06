from django.shortcuts import render, redirect
from django.http import request

from .forms import OfertaForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def registro(request):
    return render(request,'registro.html')

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


#base de datos

def nueva_oferta(request):
    datos = {'form': OfertaForm()}
    if request.method == 'POST':
        formulario = OfertaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
            
    return render(request, 'nueva_oferta.html', datos)

""" def nueva_oferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la oferta en la base de datos
            return redirect('página_de_confirmación')  # Redirecciona a una página de confirmación
    else:
        form = OfertaForm()

    return render(request, 'nueva_oferta.html', {'form': form}) """