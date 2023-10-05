from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def inicio(request):
    return render(request, 'inicio/inicio.html')


def peliculas(request):
    return render(request, 'inicio/peliculas.html')

def login(request):
    return render(request, 'login/login.html')
