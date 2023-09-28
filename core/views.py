from django.shortcuts import render
from django.http import request

# Create your views here.
def home(request):
    return render(request,'home.html')

def registro(request):
    return render(request,'registro.html')

#def nueva_oferta(request):
#   return render(request,'nueva_oferta.html')

def login(request):
    return render(request,'login.html')