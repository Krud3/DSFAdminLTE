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

def forgot_password_view(request):
    return render(request, 'adminlte/gestion_login/recover_password.html')

def recover_password_view(request):
    if request.method == 'POST':
        return render(request, 'adminlte/gestion_login/recover_password.html')
    return render(request, 'login')

def recover_password(request):
    if request.method == 'POST':
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        gerente = Gerente.objects.get(id_gerente="GER0001")
        
        if new_password == confirm_password:
            gerente.pass_field = new_password
            gerente.save()
            return redirect('login')
        else:
            return render(request, 'adminlte/gestion_login/recover_password.html', {'error': 'Las contraseñas no coinciden'})

    return render(request, 'adminlte/gestion_login/recover_password.html')

def add_automovil(request):
    return render(request, 'adminlte/gerente/automoviles/project_add.html')

def vis_eli_mod_aut(request):
    return render(request, 'adminlte/gerente/automoviles/vis_eli_mod_aut.html')

def add_cliente(request):
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_clientes/project_add.html')

def edit_cliente(request):
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_clientes/project_edit.html')

def vis_eli_cliente(request):
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_clientes/vis_eli_cliente.html')

def gra_repuestos(request):
    return render(request, 'adminlte/gerente/reportes_graficos/gra_repuestos.html')

def add_vendedor(request):
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_vendedores/project_add.html')

def edit_vendedor(request):
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_vendedores/project_edit.html')   

def vis_eli_vendedor(request):
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_vendedores/vis_eli_vendedor.html')

def sucursal_add(request):
    return render(request, 'adminlte/gerente/sucursales/sucursal_add.html')

def vis_eli_mod_suc(request):
    return render(request, 'adminlte/gerente/sucursales/vis_eli_mod_suc.html')

def repuestos_add(request):
    return render(request, 'adminlte/gerente/repuestos/repuestos_add.html')

def vis_eli_mod(request):
    return render(request, 'adminlte/gerente/repuestos/vis_eli_mod.html')

def jefe_taller_add(request):
    return render(request, 'adminlte/jefe_taller/jefe_taller_add.html')

def vis_eli_mod_jefe(request):
    return render(request, 'adminlte/jefe_taller/vis_eli_mod_jefe.html')

def reporte_text(request):
    return render(request, 'adminlte/gerente/reportes_texto/reporte_text.html')

def reporte_add(request):
    return render(request, 'adminlte/gerente/reportes_texto/reporte_add.html')

def reporte_repu_add(request):
    return render(request, 'adminlte/gerente/reportes_texto/reporte_repu_add.html')

def reporte_inve(request):
    return render(request, 'adminlte/gerente/reportes_texto/reporte_inve.html')

def gra_rep_add(request):
    return render(request, 'adminlte/gerente/reportes_graficos/gra_rep_add.html')












