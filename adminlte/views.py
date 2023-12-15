from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from .models import Vehiculo, Gerente, Sucursal, Factura, Cotizacion, Vendedor, JefeTaller, Cliente
from django.contrib import messages
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    return render(request, 'adminlte/gerente/index.html')


def index_vendedor(request):
    return render(request, 'adminlte/vendedor/index_vendedor.html')

def vis_eli_mod_jefe(request):
    return render(request, 'adminlte/jefe_taller/vis_eli_mod_jefe.html')

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
    sucursales = Sucursal.objects.all()
    gerentes = Gerente.objects.all()
    facturas = Factura.objects.all()
    cotizaciones = Cotizacion.objects.all()

    context = {
        'sucursales': sucursales,
        'gerentes': gerentes,
        'facturas': facturas,
        'cotizaciones': cotizaciones,
    }
    return render(request, 'adminlte/gerente/automoviles/project_add.html', context)

def edit_automovil(request):
    vehiculos = Vehiculo.objects.all()
    gerentes = Gerente.objects.all()
    sucursales = Sucursal.objects.all()
    facturas = Factura.objects.all()
    cotizaciones = Cotizacion.objects.all()

    context = {
        'vehiculos': vehiculos,
        'gerentes': gerentes,
        'sucursales': sucursales,
        'facturas': facturas,
        'cotizaciones': cotizaciones,
    }

    return render(request, 'adminlte/gerente/automoviles/project_edit.html', context)

def vis_eli(request):
    vehiculos = Vehiculo.objects.all()
    print(vehiculos)
    return render(request, 'adminlte/gerente/automoviles/vis_eli.html', {'vehiculos': vehiculos})

def add_cliente(request):
    gerentes = Gerente.objects.all()
    vendedores = Vendedor.objects.all()
    jefes = JefeTaller.objects.all()
    context = {
        'gerentes': gerentes,
        'vendedores': vendedores,
        'jefes': jefes,
    }
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_clientes/project_add.html',context)

def edit_cliente(request):
    clientes = Cliente.objects.all()
    gerentes = Gerente.objects.all()
    vendedores = Vendedor.objects.all()
    jefes = JefeTaller.objects.all()

    context = {
        'clientes': clientes,
        'gerentes': gerentes,
        'vendedores': vendedores,
        'jefes': jefes,
    }
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_clientes/project_edit.html', context)

def vis_eli_cliente(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}    
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_clientes/vis_eli_cliente.html', context)

def gra_repuestos(request):
    return render(request, 'adminlte/gerente/reportes_graficos/gra_repuestos.html')

def add_vendedor(request):
    vehiculos = Vehiculo.objects.all()
    gerentes = Gerente.objects.all()
    sucursales = Sucursal.objects.all()
    facturas = Factura.objects.all()
    cotizaciones = Cotizacion.objects.all()

    context = {
        'vehiculos': vehiculos,
        'gerentes': gerentes,
        'sucursales': sucursales,
        'facturas': facturas,
        'cotizaciones': cotizaciones,
    }
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_vendedores/project_add.html', context)

def edit_vendedor(request):
    vehiculos = Vehiculo.objects.all()
    gerentes = Gerente.objects.all()
    sucursales = Sucursal.objects.all()
    facturas = Factura.objects.all()
    cotizaciones = Cotizacion.objects.all()
    vendedores = Vendedor.objects.all()

    context = {
        'vendedores': vendedores,
        'vehiculos': vehiculos,
        'gerentes': gerentes,
        'sucursales': sucursales,
        'facturas': facturas,
        'cotizaciones': cotizaciones,
    }
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_vendedores/project_edit.html', context)   

def vis_eli_vendedor(request):
    vendedores = Vendedor.objects.all()
    context = {'vendedores': vendedores}
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_vendedores/vis_eli_vendedor.html', context)

def agregar_vehiculo(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        id_gerente = request.POST.get('id_gerente')
        codigo_sucursal = request.POST.get('codigo_sucursal')
        numero_factura = request.POST.get('numero_factura')
        numero_cotizacion = request.POST.get('numero_cotizacion')
        modelo = request.POST.get('modelo')
        color = request.POST.get('color')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')

        nuevo_vehiculo = Vehiculo(
            codigo_vehiculo=codigo,
            id_gerente=Gerente.objects.get(id_gerente=id_gerente),
            codigo_sucursal=Sucursal.objects.get(codigo_sucursal=codigo_sucursal),
            numero_factura=Factura.objects.get(numero_factura=numero_factura),
            numero_cotizacion=Cotizacion.objects.get(numero_cotizacion=numero_cotizacion),
            modelo_vehiculo=modelo,
            color_vehiculo=color,
            precio_vehiculo=precio,
            descripcion_vehiculo=descripcion
        )
        nuevo_vehiculo.save()
        messages.success(request, 'Vehículo agregado exitosamente')
        return redirect('add_automovil')

    return render(request, 'adminlte/gerente/automoviles/project_add.html')

def editar_vehiculo(request):
    

    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        id_gerente = request.POST.get('id_gerente')
        codigo_sucursal = request.POST.get('codigo_sucursal')
        numero_factura = request.POST.get('numero_factura')
        numero_cotizacion = request.POST.get('numero_cotizacion')
        modelo = request.POST.get('modelo')
        color = request.POST.get('color')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')

        vehiculo = Vehiculo.objects.get(codigo_vehiculo=codigo)
        vehiculo.id_gerente = Gerente.objects.get(id_gerente=id_gerente)
        vehiculo.codigo_sucursal = Sucursal.objects.get(codigo_sucursal=codigo_sucursal)
        vehiculo.numero_factura = Factura.objects.get(numero_factura=numero_factura)
        vehiculo.numero_cotizacion = Cotizacion.objects.get(numero_cotizacion=numero_cotizacion)
        vehiculo.modelo_vehiculo = modelo
        vehiculo.color_vehiculo = color
        vehiculo.precio_vehiculo = precio
        vehiculo.descripcion_vehiculo = descripcion

        vehiculo.save()
        messages.success(request, 'Vehículo actualizado exitosamente')
        return redirect('edit_automovil')  

    return render(request, 'adminlte/gerente/automoviles/project_edit.html')  

@require_POST
def eliminar_vehiculo(request):
    codigo_vehiculo = request.POST.get('codigo_vehiculo')
    vehiculo = get_object_or_404(Vehiculo, codigo_vehiculo=codigo_vehiculo)
    vehiculo.delete()
    messages.success(request, "Vehículo eliminado con éxito.")
    return redirect('vis_eli')

@require_POST
def eliminar_vendedor(request):
    id_vendedor = request.POST.get('id_vendedor')
    vendedor = get_object_or_404(Vendedor, id_vendedor=id_vendedor)
    vendedor.delete()
    messages.success(request, "Vendedor eliminado con éxito.")
    return redirect('vis_eli_vendedor')

def agregar_vendedor(request):
    if request.method == 'POST':
        id_vendedor = request.POST.get('id_vendedor')
        id_gerente = request.POST.get('id_gerente')
        codigo_sucursal = request.POST.get('codigo_sucursal')
        nombre_vendedor = request.POST.get('nombre_vendedor')
        telefono_vendedor = request.POST.get('telefono_vendedor')
        direccion_vendedor = request.POST.get('direccion_vendedor')
        email_vendedor = request.POST.get('email_vendedor')
        pass_field = request.POST.get('pass_field')

        nuevo_vendedor = Vendedor(
            id_vendedor=id_vendedor,
            id_gerente=Gerente.objects.get(id_gerente=id_gerente),
            codigo_sucursal=Sucursal.objects.get(codigo_sucursal=codigo_sucursal),
            nombre_vendedor=nombre_vendedor,
            telefono_vendedor=telefono_vendedor,
            direccion_vendedor=direccion_vendedor,
            email_vendedor=email_vendedor,
            pass_field=pass_field
        )
        nuevo_vendedor.save()
        messages.success(request, 'Vendedor agregado exitosamente')
        return redirect('add_vendedor')

    return render(request, 'adminlte/gerente/gestion_usuarios/crud_vendedores/project_add.html')

def editar_vendedor(request):
    if request.method == 'POST':
        id_vendedor = request.POST.get('id_vendedor')
        id_gerente = request.POST.get('id_gerente')
        codigo_sucursal = request.POST.get('codigo_sucursal')
        nombre_vendedor = request.POST.get('nombre_vendedor')
        telefono_vendedor = request.POST.get('telefono_vendedor')
        direccion_vendedor = request.POST.get('direccion_vendedor')
        email_vendedor = request.POST.get('email_vendedor')
        pass_field = request.POST.get('pass_field')

        vendedor = Vendedor.objects.get(id_vendedor=id_vendedor)
        vendedor.id_gerente = Gerente.objects.get(id_gerente=id_gerente)
        vendedor.codigo_sucursal = Sucursal.objects.get(codigo_sucursal=codigo_sucursal)
        vendedor.nombre_vendedor = nombre_vendedor
        vendedor.telefono_vendedor = telefono_vendedor
        vendedor.direccion_vendedor = direccion_vendedor
        vendedor.email_vendedor = email_vendedor
        vendedor.pass_field = pass_field

        vendedor.save()
        messages.success(request, 'Vendedor actualizado exitosamente')
        return redirect('edit_vendedor')  

    return render(request, 'adminlte/gerente/gestion_usuarios/crud_vendedores/project_edit.html')

def agregar_cliente(request):
    if request.method == 'POST':
        id_cliente = request.POST.get('id_cliente')
        id_gerente = request.POST.get('id_gerente')
        id_vendedor = request.POST.get('id_vendedor')
        id_jefe_taller = request.POST.get('id_jefe_taller')
        nombre_cliente = request.POST.get('nombre_cliente')
        telefono_cliente = request.POST.get('telefono_cliente')
        direccion_cliente = request.POST.get('direccion_cliente')
        email_cliente = request.POST.get('email_cliente')

        nuevo_cliente = Cliente(
            id_cliente=id_cliente,
            id_gerente=Gerente.objects.get(id_gerente=id_gerente),
            id_vendedor=Vendedor.objects.get(id_vendedor=id_vendedor),
            id_jefe_taller=JefeTaller.objects.get(id_jefe_taller=id_jefe_taller),
            nombre_cliente=nombre_cliente,
            telefono_cliente=telefono_cliente,
            direccion_cliente=direccion_cliente,
            email_cliente=email_cliente

        )
        nuevo_cliente.save()
        messages.success(request, 'Cliente agregado exitosamente')
        return redirect('add_cliente')
    
def editar_cliente(request):
    if request.method == 'POST':
        id_cliente = request.POST.get('id_cliente')
        id_gerente = request.POST.get('id_gerente')
        id_vendedor = request.POST.get('id_vendedor')
        id_jefe_taller = request.POST.get('id_jefe_taller')
        nombre_cliente = request.POST.get('nombre_cliente')
        telefono_cliente = request.POST.get('telefono_cliente')
        direccion_cliente = request.POST.get('direccion_cliente')
        email_cliente = request.POST.get('email_cliente')

        cliente = Cliente.objects.get(id_cliente=id_cliente)
        cliente.id_gerente = Gerente.objects.get(id_gerente=id_gerente)
        cliente.id_vendedor = Vendedor.objects.get(id_vendedor=id_vendedor)
        cliente.id_jefe_taller = JefeTaller.objects.get(id_jefe_taller=id_jefe_taller)
        cliente.nombre_cliente = nombre_cliente
        cliente.telefono_cliente = telefono_cliente
        cliente.direccion_cliente = direccion_cliente
        cliente.email_cliente = email_cliente

        cliente.save()
        messages.success(request, 'Cliente actualizado exitosamente')
        return redirect('edit_cliente')  

    return render(request, 'adminlte/gerente/gestion_usuarios/crud_clientes/project_edit.html')

@require_POST
def eliminar_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    cliente.delete()
    messages.success(request, "Cliente eliminado con éxito.")
    return redirect('vis_eli_cliente')

@require_POST
def eliminar_sucursal(request):
    codigo_sucursal = request.POST.get('codigo_sucursal')
    sucursal = get_object_or_404(Sucursal, codigo_sucursal=codigo_sucursal)
    sucursal.delete()
    messages.success(request, "Sucursal eliminada con éxito.")
    return redirect('vis_eli_sucursal')

def vis_eli_sucursal(request):
    sucursales = Sucursal.objects.all()
    context = {'sucursales': sucursales}
    return render(request, 'adminlte/gerente/sucursales/vis_eli_sucursal.html', context)

def edit_sucursal(request):
    sucursales = Sucursal.objects.all()
    gerentes = Gerente.objects.all()

    context = {
        'sucursales': sucursales,
        'gerentes': gerentes,
    }
    return render(request, 'adminlte/gerente/sucursales/sucursal_edit.html', context)

def add_sucursal(request):
    gerentes = Gerente.objects.all()
    context = {
        'gerentes': gerentes,
    }
    return render(request, 'adminlte/gerente/sucursales/sucursal_add.html', context)

def gra_rep_add(request):
    return render(request, 'adminlte/gerente/reportes_graficos/gra_rep_add.html')



def vis_eli_mod_jefe(request):
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_jefes_taller/vis_eli_mod_jefe.html')

def clientes(request):
    
      if request.method == 'POST':
        id_cliente = request.POST.get('id_cliente')
        id_gerente = request.POST.get('id_gerente')
        id_vendedor = request.POST.get('id_vendedor')
        id_jefe_taller = request.POST.get('id_jefe_taller')
        nombre_cliente = request.POST.get('nombre_cliente')
        telefono_cliente = request.POST.get('telefono_cliente')
        direccion_cliente = request.POST.get('direccion_cliente')
        email_cliente = request.POST.get('email_cliente')

        nuevo_cliente = Cliente(
            id_cliente=id_cliente,
            id_gerente=Gerente.objects.get(id_gerente=id_gerente),
            id_vendedor=Vendedor.objects.get(id_vendedor=id_vendedor),
            id_jefe_taller=JefeTaller.objects.get(id_jefe_taller=id_jefe_taller),
            nombre_cliente=nombre_cliente,
            telefono_cliente=telefono_cliente,
            direccion_cliente=direccion_cliente,
            email_cliente=email_cliente

       
            
         )
        nuevo_cliente.save()
        messages.success(request, 'cliente agregado exitosamente')
    
   
        return render(request, 'adminlte/vendedor/crud_clientes/clientes.html')
  
      cliente = Cliente.objects.all()
      context = {
          'cliente': cliente,
        }

      return render(request, 'adminlte/vendedor/crud_clientes/clientes.html', context)
       
def vis_mod_eli_cliente(request):
    @require_POST
    def eliminar_cliente(request):
     id_cliente = request.POST.get('id_cliente')
     cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
     cliente.delete()
     messages.success(request, "Cliente eliminado con éxito.")
    return redirect('vis_mod_eli_cliente')

def vis_mod_eli_cliente(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}    
   
    return render(request, 'adminlte/vendedor/crud_clientes/vis_mod_eli_cliente.html', context)




def add_cotizacion(request):
    
 return render(request, 'adminlte/vendedor/crud_cotizaciones/add_cotizacion.html')

def vis_mod_eli_cotizacion(request):
    
    return render(request, 'adminlte/vendedor/crud_cotizaciones/vis_mod_eli_cotizacion.html')







def add_factura(request):
    return render(request, 'adminlte/vendedor/crud_facturas/add_factura.html')


   


def vis_eli_factura(request):
   
    return render(request, 'adminlte/vendedor/crud_facturas/vis_eli_factura.html')

    

def add_cotizaciones(request):
    return render(request, 'adminlte/vendedor/reportes_texto/add_cotizaciones.html')

def vis_vehiculos(request):
    
    return render(request, 'adminlte/vendedor/automoviles/vis_vehiculos.html')

def jefe_taller_add(request):
    
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_jefes_taller/jefe_taller_add.html')

def cotizaciones(request):
    
    return render(request, 'adminlte/vendedor/reportes_graficos/cotizaciones.html')

def ventas(request):
    
    return render(request, 'adminlte/vendedor/reportes_graficos/ventas.html')

def add_ventas(request):
    
    return render(request, 'adminlte/vendedor/reportes_texto/add_ventas')

