from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'adminlte/index.html')
def index3(request):
    return render(request, 'adminlte/index3.html')
def login(request):
    return render(request, 'adminlte/login_Example/login.html')
    
