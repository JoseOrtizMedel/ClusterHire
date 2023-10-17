from django.shortcuts import redirect, render
from django.http import request
from .forms import InicioForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def registro(request):
    return render(request,'registro.html')

#def nueva_oferta(request):
#   return render(request,'nueva_oferta.html')

""" def login(request):
    return render(request,'login.html') """

""" def login(request):
    data = {
        'form': InicioForm()
    }
    return render (request, 'login.html', data) """

""" def login(request):

    if request.method == "POST":
        username = request.POST.get('email')
        pass1 = request.POST.get('pass1')
    
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return render(request, "login.html")
        else:
            messages.error(request, "Algo está mal, revise su correo y/o contraseña")
            return redirect("home.html")

    return render(request, "login.html") """

def login(request):
    if request.method == 'POST':
        form = InicioForm(request.POST)
        if form.is_valid():
            return render (request, "home.html")
    else:
            form = InicioForm()
            messages.error(request, "Algo está mal, revise su correo y/o contraseña")
            return redirect("home.html")
    
    return render(request, 'login.html', {'form' : form})