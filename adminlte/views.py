from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'adminlte/index.html')
def login(request):
    if request.method == 'POST':
        #logica de autenticacion va aqui
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        return redirect(reverse('index'))
    return render(request, 'adminlte/gestion_login/login.html')

