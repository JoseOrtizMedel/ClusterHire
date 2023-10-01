from django.shortcuts import render
from django.http import request

# Create your views here.
def home(request):
    return render(request,'home.html')

def registro(request):
    return render(request,'registro.html')

def recuperar_contrasenia(request):
    return render(request,'recuperar_contrasenia.html')

def registrar_ncontrasenia(request):
    return render(request, 'registrar_ncontrasenia.html')