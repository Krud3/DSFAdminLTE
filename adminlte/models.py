# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.hashers import make_password


class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=10)
    id_gerente = models.ForeignKey('Gerente', models.DO_NOTHING, db_column='id_gerente')
    id_vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='id_vendedor')
    id_jefe_taller = models.ForeignKey('JefeTaller', models.DO_NOTHING, db_column='id_jefe_taller')
    nombre_cliente = models.CharField(max_length=50)
    telefono_cliente = models.CharField(max_length=20, blank=True, null=True)
    direccion_cliente = models.CharField(max_length=100, blank=True, null=True)
    email_cliente = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cliente'


class Cotizacion(models.Model):
    numero_cotizacion = models.CharField(primary_key=True, max_length=10)
    id_vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='id_vendedor')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    fecha_cotizacion = models.DateField()
    precio_total_cotizacion = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'cotizacion'


class Factura(models.Model):
    numero_factura = models.CharField(primary_key=True, max_length=10)
    id_vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='id_vendedor')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    fecha_factura = models.DateField()
    precio_total_factura = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'factura'


class Gerente(models.Model):
    id_gerente = models.CharField(primary_key=True, max_length=10)
    nombre_gerente = models.CharField(max_length=50)
    telefono_gerente = models.CharField(max_length=20, blank=True, null=True)
    direccion_gerente = models.CharField(max_length=100, blank=True, null=True)
    email_gerente = models.CharField(max_length=50, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=200, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = True
        db_table = 'gerente'

    def save(self, *args, **kwargs):
        if self.pass_field:
            self.pass_field = make_password(self.pass_field)
        super(Gerente, self).save(*args, **kwargs)


class JefeTaller(models.Model):
    id_jefe_taller = models.CharField(primary_key=True, max_length=10)
    id_gerente = models.ForeignKey(Gerente, models.DO_NOTHING, db_column='id_gerente')
    codigo_sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='codigo_sucursal')
    nombre_jefe_taller = models.CharField(max_length=50)
    telefono_jefe_taller = models.CharField(max_length=20, blank=True, null=True)
    direccion_jefe_taller = models.CharField(max_length=100, blank=True, null=True)
    email_jefe_taller = models.CharField(max_length=50, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=200, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = True
        db_table = 'jefe_taller'
    def save(self, *args, **kwargs):
        if self.pass_field:
            self.pass_field = make_password(self.pass_field)
        super(JefeTaller, self).save(*args, **kwargs)


class OrdenTrabajo(models.Model):
    numero_orden_trabajo = models.CharField(primary_key=True, max_length=10)
    id_jefe_taller = models.ForeignKey(JefeTaller, models.DO_NOTHING, db_column='id_jefe_taller')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    codigo_vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='codigo_vehiculo')
    numero_factura = models.ForeignKey(Factura, models.DO_NOTHING, db_column='numero_factura')
    fecha_inicio_orden_trabajo = models.DateField()
    fecha_final_orden_trabajo = models.DateField()
    estado_orden_trabajo = models.TextField(blank=True, null=True)  # This field type is a guess.
    descripcion_orden_trabajo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'orden_trabajo'


class Repuesto(models.Model):
    codigo_repuesto = models.CharField(primary_key=True, max_length=10)
    id_gerente = models.ForeignKey(Gerente, models.DO_NOTHING, db_column='id_gerente')
    codigo_sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='codigo_sucursal')
    numero_factura = models.ForeignKey(Factura, models.DO_NOTHING, db_column='numero_factura')
    numero_cotizacion = models.ForeignKey(Cotizacion, models.DO_NOTHING, db_column='numero_cotizacion')
    nombre_repuesto = models.CharField(max_length=50)
    tipo_repuesto = models.CharField(max_length=50)
    precio_repuesto = models.IntegerField()
    descripcion_repuesto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'repuesto'

 


class Sucursal(models.Model):
    codigo_sucursal = models.CharField(primary_key=True, max_length=10)
    id_gerente = models.ForeignKey(Gerente, models.DO_NOTHING, db_column='id_gerente')
    nombre_sucursal = models.CharField(max_length=100)
    ciudad_sucursal = models.CharField(max_length=50, blank=True, null=True)
    telefono_sucursal = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sucursal'


class Vehiculo(models.Model):
    codigo_vehiculo = models.CharField(primary_key=True, max_length=10)
    id_gerente = models.ForeignKey(Gerente, models.DO_NOTHING, db_column='id_gerente')
    codigo_sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='codigo_sucursal')
    numero_factura = models.ForeignKey(Factura, models.DO_NOTHING, db_column='numero_factura')
    numero_cotizacion = models.ForeignKey(Cotizacion, models.DO_NOTHING, db_column='numero_cotizacion')
    modelo_vehiculo = models.CharField(max_length=50)
    color_vehiculo = models.CharField(max_length=50, blank=True, null=True)
    precio_vehiculo = models.IntegerField()
    descripcion_vehiculo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vehiculo'


class Vendedor(models.Model):
    id_vendedor = models.CharField(primary_key=True, max_length=10)
    id_gerente = models.ForeignKey(Gerente, models.DO_NOTHING, db_column='id_gerente')
    codigo_sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='codigo_sucursal')
    nombre_vendedor = models.CharField(max_length=50)
    telefono_vendedor = models.CharField(max_length=20, blank=True, null=True)
    direccion_vendedor = models.CharField(max_length=100, blank=True, null=True)
    email_vendedor = models.CharField(max_length=50, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=200, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = True
        db_table = 'vendedor'
    def save(self, *args, **kwargs):
        if self.pass_field:
            self.pass_field = make_password(self.pass_field)
        super(Vendedor, self).save(*args, **kwargs)