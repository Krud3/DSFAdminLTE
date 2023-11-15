from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from .models import Gerente

# Create your views here.
def index(request):
    return render(request, 'adminlte/gerente/index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        
        password = request.POST.get('password')
        try:
            gerente = Gerente.objects.get(id_gerente=username)
            if check_password(password, gerente.pass_field):
                #request.session['user'] = gerente.id_gerente
                return redirect(reverse('index'))
            else:
                return render(request, 'adminlte/gestion_login/login.html', {'error': 'Contraseña incorrecta'})
            
        except Gerente.DoesNotExist:
            return render(request, 'adminlte/gestion_login/login.html', {'error': 'Usuario no existe'})
        
    return render(request, 'adminlte/gestion_login/login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
