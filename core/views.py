from django.shortcuts import render
from django.http import request

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
