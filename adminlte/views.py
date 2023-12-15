from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from .models import Vehiculo, Gerente, Sucursal, Factura, Cotizacion, Vendedor, JefeTaller, Cliente,Repuesto,OrdenTrabajo
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
from django.db.models import Sum
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'adminlte/gerente/index.html')
def index2(request):
    return render(request, 'adminlte/jefe_taller/index_jefe_taller.html')   



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
    vehiculos = Vehiculo.objects.all()
    sucursales = Sucursal.objects.all()
    gerentes = Gerente.objects.all()
    facturas = Factura.objects.all()
    cotizaciones = Cotizacion.objects.all()

    context = {
        'sucursales': sucursales,
        'gerentes': gerentes,
        'facturas': facturas,
        'cotizaciones': cotizaciones,
        'vehiculos': vehiculos,
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

    # Supongamos que estás trabajando con el primer cliente en la lista
    cliente = clientes.first()

    context = {
        'clientes': clientes,
        'gerentes': gerentes,
        'vendedores': vendedores,
        'jefes': jefes,
        'cliente': cliente,  # Asegúrate de obtener el cliente correcto aquí
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
    vendedor= Vendedor.objects.all()
    context = {
        'vehiculos': vehiculos,
        'gerentes': gerentes,
        'sucursales': sucursales,
        'facturas': facturas,
        'cotizaciones': cotizaciones,
         'vendedor': vendedor,
    }
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_vendedores/project_add.html', context)

def edit_vendedor(request):
    vehiculos = Vehiculo.objects.all()
    gerentes = Gerente.objects.all()
    sucursales = Sucursal.objects.all()
    facturas = Factura.objects.all()
    cotizaciones = Cotizacion.objects.all()
    vendedores = Vendedor.objects.all()
    
    vendedor = vendedores.first()

    context = {
        'vendedores': vendedores,
        'vehiculos': vehiculos,
        'gerentes': gerentes,
        'sucursales': sucursales,
        'facturas': facturas,
        'cotizaciones': cotizaciones,
        'vendedor': vendedor
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

def editar_vehiculo(request, codigo_vehiculo):
    # Obtiene el objeto del vehículo basado en el codigo_vehiculo proporcionado
    vehiculo = Vehiculo.objects.get(codigo_vehiculo=codigo_vehiculo)

    context = {
        'vehiculo': vehiculo,
    }

    if request.method == 'POST':
        # Maneja los datos del formulario desde la solicitud POST
        color = request.POST.get('color_vehiculo', '')
        precio = request.POST.get('precio_vehiculo', '')
        descripcion = request.POST.get('descripcion_vehiculo', '')
        modelo = request.POST.get('modelo_vehiculo', '')

        # Actualiza solo los campos proporcionados en el formulario
        if color:
            vehiculo.color_vehiculo = color
        if precio:
            vehiculo.precio_vehiculo = precio
        if descripcion:
            vehiculo.descripcion_vehiculo = descripcion
        if modelo:
            vehiculo.modelo_vehiculo = modelo

        vehiculo.save()
        # Puedes agregar un mensaje de éxito si lo deseas
        return redirect('vis_eli')

    # Renderiza el formulario para la edición si la solicitud no es POST
    return render(request, 'adminlte/gerente/automoviles/project_edit.html', context)
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

def editar_vendedor(request, id_vendedor):
    # Obtener el objeto del vendedor basado en el id_vendedor proporcionado
    vendedor = Vendedor.objects.get(id_vendedor=id_vendedor)

    context = {
        'vendedor': vendedor,
    }

    if request.method == 'POST':
        # Manejar los datos del formulario desde la solicitud POST
        nombre_vendedor = request.POST.get('nombre_vendedor', '')
        direccion_vendedor = request.POST.get('direccion_vendedor', '')
        email_vendedor = request.POST.get('email_vendedor', '')
        telefono_vendedor = request.POST.get('telefono_vendedor', '')

        # Actualizar solo los campos proporcionados en el formulario
        if nombre_vendedor:
            vendedor.nombre_vendedor = nombre_vendedor
        if direccion_vendedor:
            vendedor.direccion_vendedor = direccion_vendedor
        if email_vendedor:
            vendedor.email_vendedor = email_vendedor
        if telefono_vendedor:
            vendedor.telefono_vendedor = telefono_vendedor

        vendedor.save()

        # Redirigir a la vista deseada después de la edición
        return redirect('vis_eli_vendedor') 

    return render(request, 'adminlte/gerente/gestion_usuarios/crud_vendedores/project_edit.html', context)
     

    

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
    
def editar_cliente(request, id_cliente):
    # Obtener el objeto del cliente basado en el id_cliente proporcionado
    cliente = Cliente.objects.get(id_cliente=id_cliente)

    context = {
        'cliente': cliente,
    }

    if request.method == 'POST':
        # Manejar los datos del formulario desde la solicitud POST
        nombre_cliente = request.POST.get('nombre_cliente', '')
        direccion_cliente = request.POST.get('direccion_cliente', '')
        email_cliente = request.POST.get('email_cliente', '')
        telefono_cliente = request.POST.get('telefono_cliente', '')

        # Actualizar solo los campos proporcionados en el formulario
        if nombre_cliente:
            cliente.nombre_cliente = nombre_cliente
        if direccion_cliente:
            cliente.direccion_cliente = direccion_cliente
        if email_cliente:
            cliente.email_cliente = email_cliente
        if telefono_cliente:
            cliente.telefono_cliente = telefono_cliente

        cliente.save()
       
        return redirect('vis_eli_cliente')  

    return render(request, 'adminlte/gerente/gestion_usuarios/crud_clientes/project_edit.html',context)

@require_POST
def eliminar_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    cliente.delete()
    messages.success(request, "Cliente eliminado con éxito.")
    return redirect('vis_eli_cliente')




def gra_rep_add(request):
    return render(request, 'adminlte/gerente/reportes_graficos/gra_rep_add.html')




def add_sucursal(request):
  
    sucursales = Sucursal.objects.all()
    gerentes = Gerente.objects.all()
   
    context = {
        
        'sucursales': sucursales,
        'gerentes': gerentes,
     }
    return render(request, 'adminlte/gerente/sucursales/sucursal_add.html', context)

def vis_eli_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'adminlte/gerente/sucursales/visualizar_editar_eliminar_sucursal.html', {'sucursales': sucursales})



def agregar_sucursal(request):
    if request.method == 'POST':
        codigo_sucursal = request.POST.get('codigo_sucursal')  # Corregir el espacio extra
        id_gerente = request.POST.get('id_gerente')
        nombre_sucursal = request.POST.get('nombre_sucursal')
        ciudad_sucursal = request.POST.get('ciudad_sucursal')
        telefono_sucursal = request.POST.get('telefono_sucursal')

        nuevo_sucursal = Sucursal(
            codigo_sucursal=codigo_sucursal,
            id_gerente=Gerente.objects.get(id_gerente=id_gerente),
            nombre_sucursal=nombre_sucursal,
            ciudad_sucursal=ciudad_sucursal,
            telefono_sucursal=telefono_sucursal,
        )
        nuevo_sucursal.save()
        messages.success(request, 'Sucursal agregada exitosamente')
        return redirect('add_sucursal')  # Ajusta esto según tus necesidades

    sucursales = Sucursal.objects.all()
    context = {
        'sucursales': sucursales,
    }
    print(sucursales)  # Corregir aquí
    return render(request, 'adminlte/gerente/sucursales/visualizar_editar_eliminar_sucursal.html', context)

@require_POST
def eliminar_sucursal(request):
    codigo_sucursal = request.POST.get('codigo_sucursal')
    sucursal = get_object_or_404(Sucursal, codigo_sucursal= codigo_sucursal)
    sucursal.delete()
    messages.success(request, "Sucursal eliminado con éxito.")
    return redirect('vis_eli_sucursal')


def add_cliente_jefe_taller(request):
    gerentes = Gerente.objects.all()
    vendedores = Vendedor.objects.all()
    jefes = JefeTaller.objects.all()
    context = {
        'gerentes': gerentes,
        'vendedores': vendedores,
        'jefes': jefes,
    }
    return render(request, 'adminlte/jefe_taller/Clientes/add_jefe_taller.html',context)


def agregar_jefe_taller_cliente(request):
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
        return redirect('add_jefetaller_cliente')  # Adjust this according to your needs

    cliente = Cliente.objects.all()
    context = {
        'cliente': cliente,
    }

    return render(request, 'adminlte/jefe_taller/Clientes/edit_delete_jefetaller.html', context)


@require_POST
def eliminar_cliente_jefe_taller(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    cliente.delete()
    messages.success(request, "Cliente eliminado con éxito.")
    return redirect('vis_eli_cliente_jefe_taller')

def vis_eli_jefe_taller_cliente(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}    
    return render(request, 'adminlte/jefe_taller/Clientes/edit_delete_jefetaller.html', context)


def consultar_repuesto_jefe_taller(request):
    if request.method == 'POST':
        codigo_repuesto = request.POST.get('codigo_repuesto')
        id_gerente = request.POST.get('id_gerente')
        codigo_sucursal = request.POST.get('codigo_sucursal')
        numero_factura = request.POST.get('numero_factura')
        numero_cotizacion = request.POST.get('numero_cotizacion')
        nombre_repuesto = request.POST.get('nombre_repuesto')
        tipo_repuesto = request.POST.get('tipo_repuesto')
        precio_repuesto = request.POST.get('precio_repuesto')
        descripcion_repuesto = request.POST.get('descripcion_repuesto')

        
        nuevo_repuesto = Repuesto(
                codigo_repuesto=codigo_repuesto,
                id_gerente=Gerente.objects.get(id_gerente=id_gerente),
                codigo_sucursal=Sucursal.objects.get(codigo_sucursal=codigo_sucursal),
                numero_factura=Factura.objects.get(numero_factura=numero_factura),
                numero_cotizacion=Cotizacion.objects.get( numero_cotizacion=numero_cotizacion),
                nombre_repuesto=nombre_repuesto,
                tipo_repuesto=tipo_repuesto,
                precio_repuesto=precio_repuesto,
                descripcion_repuesto=descripcion_repuesto
            )
        nuevo_repuesto.save()
        messages.success(request, 'Repuesto agregado exitosamente')
        return redirect('add_repuesto')  # Ajusta esto según tus necesidades
       
        
    repuestos = Repuesto.objects.all()
    context = {
        'repuestos': repuestos,
    }
    print(Repuesto)
    return render(request, 'adminlte/jefe_taller/Repuestos/consultar_repuestos.html', context)


# View for rendering the form to add orders of work
def add_ordenes_trabajo(request):
    jefes = JefeTaller.objects.all()
    clientes = Cliente.objects.all()
    vehiculos = Vehiculo.objects.all()
    facturas = Factura.objects.all()
  
    context = {
        'jefes': jefes,
        'clientes': clientes,
        'vehiculos': vehiculos,
        'facturas': facturas,
    }
    return render(request, 'adminlte/jefe_taller/Ordenes_trabajo/add_ordenes_trabajo.html', context)

def agregar_ordenes_trabajo(request):
    if request.method == 'POST':
        # Extracting data from the POST request
        numero_orden_trabajo = request.POST.get('numero_orden_trabajo')
        id_jefe_taller = request.POST.get('id_jefe_taller')
        id_cliente = request.POST.get('id_cliente')
        codigo_vehiculo = request.POST.get('codigo_vehiculo')
        numero_factura = request.POST.get('numero_factura')
        fecha_inicio_orden_trabajo = request.POST.get('fecha_inicio_orden_trabajo')
        fecha_final_orden_trabajo = request.POST.get('fecha_final_orden_trabajo')
        estado_orden_trabajo = request.POST.get('estado_orden_trabajo')
        descripcion_orden_trabajo = request.POST.get('descripcion_orden_trabajo')

        # Creating a new OrdenTrabajo object
        nueva_orden_trabajo = OrdenTrabajo(
            numero_orden_trabajo=numero_orden_trabajo,
            id_jefe_taller = JefeTaller.objects.get(id_jefe_taller=id_jefe_taller),
            id_cliente=Cliente.objects.get(id_cliente=id_cliente),
            codigo_vehiculo=Vehiculo.objects.get(codigo_vehiculo=codigo_vehiculo),
            numero_factura=Factura.objects.get(numero_factura=numero_factura),
            fecha_inicio_orden_trabajo=fecha_inicio_orden_trabajo,
            fecha_final_orden_trabajo=fecha_final_orden_trabajo,
            estado_orden_trabajo=estado_orden_trabajo,
            descripcion_orden_trabajo=descripcion_orden_trabajo
        )

        # Saving the new OrdenTrabajo object to the database
        nueva_orden_trabajo.save()

        # Displaying a success message
        messages.success(request, 'Orden de trabajo agregada exitosamente')

        # Redirecting to a specified URL (adjust this based on your needs)
        return redirect('add_ordenes_trabajo')

    # If the request method is not POST, retrieve existing OrdenTrabajo objects
    orden_trabajo = OrdenTrabajo.objects.all()
    jefes = JefeTaller.objects.all()
    clientes = Cliente.objects.all()
    vehiculos = Vehiculo.objects.all()
    facturas = Factura.objects.all()
    
    # Creating a context dictionary for rendering the template
    context = {
        
        'jefes': jefes,
        'clientes': clientes,
        'vehiculos': vehiculos,
        'facturas': facturas,
    
       'orden_trabajo': orden_trabajo
    }

    # Rendering the template with the context
    return render(request, 'adminlte/jefe_taller/Ordenes_trabajo/edit_delete_ordenes_trabajo.html', context)

# View for deleting an order of work
@require_POST
def eliminar_ordenes_trabajo(request):
    numero_orden_trabajo = request.POST.get('numero_orden_trabajo')
    orden_trabajo = get_object_or_404(OrdenTrabajo, numero_orden_trabajo=numero_orden_trabajo)
    orden_trabajo.delete()
    messages.success(request, "Orden de trabajo eliminada con éxito.")
    return redirect('vis_eli_ordenes_trabajo')

# View for displaying and deleting orders of work
def vis_eli_ordenes_trabajo(request):
    ordenes_trabajo = OrdenTrabajo.objects.all()
    print(ordenes_trabajo)
    return render(request, 'adminlte/jefe_taller/Ordenes_trabajo/edit_delete_ordenes_trabajo.html', {'ordenes_trabajo': ordenes_trabajo})

def inventario_ordenes_trabajo(request):
    ordenes = OrdenTrabajo.objects.all()

    data_for_chart = OrdenTrabajo.objects.annotate(
        month=TruncMonth('fecha_inicio_orden_trabajo')
    ).values('month', 'estado_orden_trabajo').annotate(
        count=Count('numero_orden_trabajo')
    ).order_by('month', 'estado_orden_trabajo')

    context = {
        'ordenes': ordenes,
        'data_for_chart': list(data_for_chart),
    }

    return render(request, 'adminlte/jefe_taller/reportes_graficos/reporte_grafico_jefe_taller.html', context)

# Vista para alimentar la gráfica con datos JSON
def datos_grafico(request):
    data_for_chart = OrdenTrabajo.objects.annotate(
        month=TruncMonth('fecha_inicio_orden_trabajo')
    ).values('month', 'estado_orden_trabajo').annotate(
        count=Count('numero_orden_trabajo')
    ).order_by('month', 'estado_orden_trabajo')

    # Convertir queryset a una lista de diccionarios
    data = [
        {
            'month': entry['month'],
            'estado_orden_trabajo': entry['estado_orden_trabajo'],
            'count': entry['count'],
        }
        for entry in data_for_chart
    ]

    # Ordenar los datos por mes y estado
    data = sorted(data, key=lambda x: (x['month'], x['estado_orden_trabajo']))

    return JsonResponse(data, safe=False)

def gra_repuestos(request):
    return render(request, 'adminlte/gerente/reportes_graficos/gra_repuestos.html')

def gra_rep_add(request):
    repuestos = Repuesto.objects.all()

    data_for_chart = Repuesto.objects.values(
        'tipo_repuesto'
    ).annotate(
        total_precio=Sum('precio_repuesto'),
        cantidad_unidades=Count('tipo_repuesto')
    ).order_by('tipo_repuesto')

    context = {
        'repuestos': repuestos,
        'data_for_chart': list(data_for_chart),
    }

    return render(request, 'adminlte/gerente/reportes_graficos/gra_rep_add.html', context)

# Vista para alimentar la gráfica con datos JSON
def datos_grafico_rep(request):
    data_for_chart = Repuesto.objects.values(
        'tipo_repuesto'
    ).annotate(
        total_precio=Sum('precio_repuesto'),
        cantidad_unidades=Count('tipo_repuesto')
    ).order_by('tipo_repuesto')

    # Convertir queryset a una lista de diccionarios
    data = [
        {
            'tipo_repuesto': entry['tipo_repuesto'],
            'total_precio': entry['total_precio'],
            'cantidad_unidades': entry['cantidad_unidades'],
        }
        for entry in data_for_chart
    ]

    # Ordenar los datos por tipo_repuesto
    data = sorted(data, key=lambda x: x['tipo_repuesto'])

    return JsonResponse(data, safe=False)

def gra_autos(request):
    return render(request, 'adminlte/gerente/reportes_graficos/gra_autos.html')


def gra_autos_add(request):
    vehiculos = Vehiculo.objects.all()

    data_for_chart = Vehiculo.objects.values(
        'modelo_vehiculo'
    ).annotate(
        total_precio=Sum('precio_vehiculo'),
        cantidad_unidades=Count('modelo_vehiculo')
    ).order_by('modelo_vehiculo')

    context = {
        'vehiculos': vehiculos,
        'data_for_chart': list(data_for_chart),
    }

    return render(request, 'adminlte/gerente/reportes_graficos/gra_autos.html', context)

# Vista para alimentar la gráfica con datos JSON
def datos_grafico_autos(request):
    data_for_chart = Vehiculo.objects.values(
        'modelo_vehiculo'
    ).annotate(
        total_precio=Sum('precio_vehiculo'),
        cantidad_unidades=Count('modelo_vehiculo')
    ).order_by('modelo_vehiculo')

    # Convertir queryset a una lista de diccionarios
    data = [
        {
            'modelo_vehiculo': entry['modelo_vehiculo'],
            'total_precio': entry['total_precio'],
            'cantidad_unidades': entry['cantidad_unidades'],
        }
        for entry in data_for_chart
    ]

    # Ordenar los datos por modelo_vehiculo
    data = sorted(data, key=lambda x: x['modelo_vehiculo'])

    return JsonResponse(data, safe=False)



def agregar_ordenes_trabajo2(request):
  ordenes_trabajo = OrdenTrabajo.objects.all()
  print(ordenes_trabajo)
  return render(request, 'adminlte/jefe_taller/reportes_texto/reporte_texto_ordenes_trabajo.html', {'ordenes_trabajo': ordenes_trabajo})

def render_pdf(html_content):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="orden_trabajo.pdf"'
    pisa.CreatePDF(html_content, dest=response)
    return response

def generar_pdf_orden_trabajo(request, numero_orden_trabajo):
    orden_trabajo = get_object_or_404(OrdenTrabajo, numero_orden_trabajo=numero_orden_trabajo)
    
    context = {'orden_trabajo': orden_trabajo}
    template = get_template('orden_trabajo_pdf.html')
    html_content = template.render(context)

    return render_pdf(html_content)

def render_pdf(html_content):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="orden_trabajo.pdf"'
    pisa.CreatePDF(html_content, dest=response)
    return response

def generar_pdf_orden_trabajo(request, numero_orden_trabajo):
    orden_trabajo = get_object_or_404(OrdenTrabajo, numero_orden_trabajo=numero_orden_trabajo)
    
    context = {'orden_trabajo': orden_trabajo}
    template = get_template('adminlte/jefe_taller/reportes_texto/orden_trabajo_pdf.html')
    html_content = template.render(context)

    return render_pdf(html_content)




def add_jefe_taller(request):
    jefes_taller = JefeTaller.objects.all()
    gerentes = Gerente.objects.all()
    sucursales = Sucursal.objects.all()

    context = {
        
        'gerentes': gerentes,
        'sucursales': sucursales,
        'jefes_taller': jefes_taller,
    }

    return render(request, 'adminlte/gerente/gestion_usuarios/crud_jefes_taller/project_add_jefe_taller.html', context)

def edit_jefe_taller(request):
   jefes_taller = JefeTaller.objects.all()
   gerentes = Gerente.objects.all()
   sucursales = Sucursal.objects.all()
    
   jefe_taller = jefes_taller.first()

   context = {
        'jefes_taller': jefes_taller,
        'jefe_taller': jefe_taller,
        'gerentes': gerentes,
        'sucursales': sucursales,
        
    }
   return render(request, 'adminlte/gerente/gestion_usuarios/crud_jefes_taller/project_edit_jefe_taller.html', context)   

def vis_eli_jefe_taller(request):
    jefes_taller = JefeTaller.objects.all()
    return render(request, 'adminlte/gerente/gestion_usuarios/crud_jefes_taller/vis_eli_jefe_taller.html', {'jefes_taller': jefes_taller})

def agregar_jefe_taller(request):
    if request.method == 'POST':
        id_jefe_taller = request.POST.get('id_jefe_taller')
        id_gerente = request.POST.get('id_gerente')
        codigo_sucursal = request.POST.get('codigo_sucursal')
        nombre = request.POST.get('nombre_jefe_taller')
        telefono = request.POST.get('telefono_jefe_taller')
        direccion = request.POST.get('direccion_jefe_taller')
        email = request.POST.get('email_jefe_taller')
        

        nuevo_jefe_taller = JefeTaller(
            id_jefe_taller=id_jefe_taller,
            id_gerente=Gerente.objects.get(id_gerente=id_gerente),
            codigo_sucursal=Sucursal.objects.get(codigo_sucursal=codigo_sucursal),
            nombre_jefe_taller=nombre,
            telefono_jefe_taller=telefono,
            direccion_jefe_taller=direccion,
            email_jefe_taller=email,
            
        )
        nuevo_jefe_taller.save()
        messages.success(request, 'Jefe de taller agregado exitosamente')
        return redirect('add_jefe_taller')

    return render(request, 'adminlte/gerente/gestion_usuarios/crud_jefes_taller/project_add_jefe_taller.html')

@require_POST
def eliminar_jefe_taller(request):
    id_jefe_taller = request.POST.get('id_jefe_taller')
    jefe_taller = get_object_or_404(JefeTaller, id_jefe_taller=id_jefe_taller)
    jefe_taller.delete()
    messages.success(request, "Jefe de taller eliminado con éxito.")
    return redirect('vis_eli_jefe_taller')

def editar_jefe_taller(request, id_jefe_taller):
    jefe_taller = JefeTaller.objects.get(id_jefe_taller=id_jefe_taller)

    context = {
        'jefe_taller': jefe_taller,
    }

    if request.method == 'POST':
        nombre = request.POST.get('nombre_jefe_taller', '')
        telefono = request.POST.get('telefono_jefe_taller', '')
        direccion = request.POST.get('direccion_jefe_taller', '')
        email = request.POST.get('email_jefe_taller', '')

        # Actualiza solo los campos proporcionados en el formulario
        if nombre:
            jefe_taller.nombre_jefe_taller = nombre
        if telefono:
            jefe_taller.telefono_jefe_taller = telefono
        if direccion:
            jefe_taller.direccion_jefe_taller = direccion
        if email:
            jefe_taller.email_jefe_taller = email

        jefe_taller.save()
        messages.success(request, 'Información del Jefe de Taller actualizada exitosamente')
        return redirect('vis_eli_jefe_taller')

    return render(request, 'adminlte/gerente/gestion_usuarios/crud_jefes_taller/project_edit_jefe_taller.html', context)





def add_repuesto(request):
    repuestos = Repuesto.objects.all()
    sucursales = Sucursal.objects.all()
    gerentes = Gerente.objects.all()
    facturas = Factura.objects.all()
    cotizaciones = Cotizacion.objects.all()
    
    context = {
        'repuestos': repuestos,
        'sucursales': sucursales,
        'gerentes': gerentes,
        'facturas': facturas,
        'cotizaciones': cotizaciones,
        
    }
    return render(request, 'adminlte/gerente/repuestos/repuesto_add.html', context)

def vis_eli_repuesto(request):
    repuestos = Repuesto.objects.all()
    print(repuestos)
    return render(request, 'adminlte/gerente/repuestos/visualizar_editar_eliminar_reporte.html', {'repuestos': repuestos})

def eliminar_repuesto(request):
    codigo_repuesto = request.POST.get('codigo_repuesto')
    repuesto = get_object_or_404(Repuesto, codigo_repuesto=codigo_repuesto)
    repuesto.delete()
    messages.success(request, "Repuesto eliminado con éxito.")
    return redirect('vis_eli_repuesto')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Repuesto, Gerente, Sucursal, Factura, Cotizacion

def agregar_repuesto(request):
    if request.method == 'POST':
        try:
            codigo_repuesto = request.POST.get('codigo_repuesto')
            id_gerente = request.POST.get('id_gerente')
            codigo_sucursal = request.POST.get('codigo_sucursal')
            numero_factura = request.POST.get('numero_factura')
            numero_cotizacion = request.POST.get('numero_cotizacion')
            nombre_repuesto = request.POST.get('nombre_repuesto')
            tipo_repuesto = request.POST.get('tipo_repuesto')
            precio_repuesto = request.POST.get('precio_repuesto')
            descripcion_repuesto = request.POST.get('descripcion_repuesto')

            nuevo_repuesto = Repuesto(
                codigo_repuesto=codigo_repuesto,
                id_gerente=Gerente.objects.get(id_gerente=id_gerente),
                codigo_sucursal=Sucursal.objects.get(codigo_sucursal=codigo_sucursal),
                numero_factura=Factura.objects.get(numero_factura=numero_factura),
                numero_cotizacion=Cotizacion.objects.get(numero_cotizacion=numero_cotizacion),
                nombre_repuesto=nombre_repuesto,
                tipo_repuesto=tipo_repuesto,
                precio_repuesto=precio_repuesto,
                descripcion_repuesto=descripcion_repuesto
            )
            nuevo_repuesto.save()
            messages.success(request, 'Repuesto agregado exitosamente')
            return redirect('vis_eli_repuesto')

        except Exception as e:
            messages.error(request, f'Error al agregar repuesto: {str(e)}')
            return redirect('vis_eli_repuesto')  # O ajusta según tu necesidad

    repuestos = Repuesto.objects.all()
    context = {'repuestos': repuestos}
    return render(request, 'adminlte/gerente/repuestos/visualizar_editar_eliminar_reporte.html', context)


def edit_repuesto(request):
    repuestos = Repuesto.objects.all()
    sucursales = Sucursal.objects.all()
    gerentes = Gerente.objects.all()
    facturas = Factura.objects.all()
    cotizaciones = Cotizacion.objects.all()
    
    repuesto = repuestos.first()

   
    context = {
        'repuesto': repuesto,
        'repuestos': repuestos,
        'sucursales': sucursales,
        'gerentes': gerentes,
        'facturas': facturas,
        'cotizaciones':cotizaciones,
    }

    return render(request, 'adminlte/gerente/repuestos/project_edit_repuesto.html', context)


def editar_repuesto(request, codigo_repuesto):
    repuesto = get_object_or_404(Repuesto, codigo_repuesto=codigo_repuesto)

    context = {
        'repuesto': repuesto,
    }

    if request.method == 'POST':
        nombre_repuesto = request.POST.get('nombre_repuesto', '')
        tipo_repuesto = request.POST.get('tipo_repuesto', '')
        precio_repuesto = request.POST.get('precio_repuesto', '')
        descripcion_repuesto = request.POST.get('descripcion_repuesto', '')

        # Actualiza solo los campos proporcionados en el formulario
        if nombre_repuesto:
            repuesto.nombre_repuesto = nombre_repuesto
        if tipo_repuesto:
            repuesto.tipo_repuesto = tipo_repuesto
        if precio_repuesto:
            repuesto.precio_repuesto = precio_repuesto
        if descripcion_repuesto:
            repuesto.descripcion_repuesto = descripcion_repuesto

        repuesto.save()
        messages.success(request, 'Información del Repuesto actualizada exitosamente')

        # Mensaje de depuración para verificar la redirección
        print("Redirigiendo a:", 'vis_eli_repuesto')

        return redirect('vis_eli_repuesto')

    return render(request, 'adminlte/gerente/repuestos/project_edit_repuesto.html', context)

def edit_sucursal(request):
    sucursales = Sucursal.objects.all()
    gerentes = Gerente.objects.all() 

  
    sucursal = sucursales.first()

    context = {
        'sucursal': sucursal,
        'sucursales': sucursales,
        'gerentes': gerentes,
        
    }

    return render(request, 'adminlte/gerente/sucursales/project_edit_sucursal.html', context)

def editar_sucursal(request, codigo_sucursal):
    # Obtiene el objeto de la sucursal basado en el codigo_sucursal proporcionado
    sucursal = get_object_or_404(Sucursal, codigo_sucursal=codigo_sucursal)

    context = {
        'sucursal': sucursal,
    }

    if request.method == 'POST':
        # Maneja los datos del formulario desde la solicitud POST
        nombre_sucursal = request.POST.get('nombre_sucursal', '')
        ciudad_sucursal = request.POST.get('ciudad_sucursal', '')
        telefono_sucursal = request.POST.get('telefono_sucursal', '')

        # Actualiza solo los campos proporcionados en el formulario
        if nombre_sucursal:
            sucursal.nombre_sucursal = nombre_sucursal
        if ciudad_sucursal:
            sucursal.ciudad_sucursal = ciudad_sucursal
        if telefono_sucursal:
            sucursal.telefono_sucursal = telefono_sucursal

        sucursal.save()
        # Puedes agregar un mensaje de éxito si lo deseas
        return redirect('vis_eli_sucursal')

    # Renderiza el formulario para la edición si la solicitud no es POST
    return render(request, 'adminlte/gerente/sucursales/project_edit_sucursal.html', context)
    



def render_pdf(html_content):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="reporte_autos.pdf"'
    pisa.CreatePDF(html_content, dest=response)
    return response

def generar_pdf_sucursal(request, codigo_sucursal):
    sucursal = get_object_or_404(Sucursal, codigo_sucursal=codigo_sucursal)
    vehiculos = Vehiculo.objects.filter(codigo_sucursal=sucursal)

    context = {'sucursal': sucursal, 'vehiculos': vehiculos}
    template = get_template('adminlte/gerente/reportes_texto/reporte_texto_autos/reporte_autos_pdf.html')
    html_content = template.render(context)

    return render_pdf(html_content)

def agregar_sucursales2(request):
    sucursales = Sucursal.objects.all()
    print(sucursales)
    return render(request, 'adminlte/gerente/reportes_texto/reporte_texto_autos/reporte_autos.html', {'sucursales': sucursales})



def render_pdf(html_content):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="reporte_repuestos.pdf"'
    pisa.CreatePDF(html_content, dest=response)
    return response

def generar_pdf_repuesto(request, codigo_sucursal):
    sucursal = get_object_or_404(Sucursal, codigo_sucursal=codigo_sucursal)
    repuestos = Repuesto.objects.filter(codigo_sucursal=sucursal)

    context = {'sucursal': sucursal, 'repuestos': repuestos}
    template = get_template('adminlte/gerente/reportes_texto/reporte_texto_repuestos/reporte_repuestos_pdf.html')
    html_content = template.render(context)

    return render_pdf(html_content)

def agregar_repuestos2(request):
    sucursales = Sucursal.objects.all()
    print(sucursales)
    return render(request, 'adminlte/gerente/reportes_texto/reporte_texto_repuestos/reporte_repuestos.html', {'sucursales': sucursales})