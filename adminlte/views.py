from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'adminlte/index.html')
def login(request):
    if request.method == 'POST':
        #logica de autenticacion va aqui
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        return redirect('index')
    return render(request, 'adminlte/login.html')

