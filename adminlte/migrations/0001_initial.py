# Generated by Django 4.2.7 on 2023-11-15 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('telefono_cliente', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion_cliente', models.CharField(blank=True, max_length=100, null=True)),
                ('email_cliente', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('numero_cotizacion', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fecha_cotizacion', models.DateField()),
                ('precio_total_cotizacion', models.IntegerField()),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.cliente')),
            ],
            options={
                'db_table': 'cotizacion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('numero_factura', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fecha_factura', models.DateField()),
                ('precio_total_factura', models.IntegerField()),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.cliente')),
            ],
            options={
                'db_table': 'factura',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('id_gerente', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_gerente', models.CharField(max_length=50)),
                ('telefono_gerente', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion_gerente', models.CharField(blank=True, max_length=100, null=True)),
                ('email_gerente', models.CharField(blank=True, max_length=50, null=True)),
                ('pass_field', models.CharField(blank=True, db_column='pass', max_length=200, null=True)),
            ],
            options={
                'db_table': 'gerente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='JefeTaller',
            fields=[
                ('id_jefe_taller', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_jefe_taller', models.CharField(max_length=50)),
                ('telefono_jefe_taller', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion_jefe_taller', models.CharField(blank=True, max_length=100, null=True)),
                ('email_jefe_taller', models.CharField(blank=True, max_length=50, null=True)),
                ('pass_field', models.CharField(blank=True, db_column='pass', max_length=200, null=True)),
            ],
            options={
                'db_table': 'jefe_taller',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('codigo_sucursal', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_sucursal', models.CharField(max_length=100)),
                ('ciudad_sucursal', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono_sucursal', models.CharField(blank=True, max_length=20, null=True)),
                ('id_gerente', models.ForeignKey(db_column='id_gerente', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.gerente')),
            ],
            options={
                'db_table': 'sucursal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id_vendedor', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_vendedor', models.CharField(max_length=50)),
                ('telefono_vendedor', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion_vendedor', models.CharField(blank=True, max_length=100, null=True)),
                ('email_vendedor', models.CharField(blank=True, max_length=50, null=True)),
                ('pass_field', models.CharField(blank=True, db_column='pass', max_length=200, null=True)),
                ('codigo_sucursal', models.ForeignKey(db_column='codigo_sucursal', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.sucursal')),
                ('id_gerente', models.ForeignKey(db_column='id_gerente', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.gerente')),
            ],
            options={
                'db_table': 'vendedor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('codigo_vehiculo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('modelo_vehiculo', models.CharField(max_length=50)),
                ('color_vehiculo', models.CharField(blank=True, max_length=50, null=True)),
                ('precio_vehiculo', models.IntegerField()),
                ('descripcion_vehiculo', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo_sucursal', models.ForeignKey(db_column='codigo_sucursal', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.sucursal')),
                ('id_gerente', models.ForeignKey(db_column='id_gerente', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.gerente')),
                ('numero_cotizacion', models.ForeignKey(db_column='numero_cotizacion', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.cotizacion')),
                ('numero_factura', models.ForeignKey(db_column='numero_factura', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.factura')),
            ],
            options={
                'db_table': 'vehiculo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('codigo_repuesto', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_repuesto', models.CharField(max_length=50)),
                ('tipo_repuesto', models.CharField(max_length=50)),
                ('precio_repuesto', models.IntegerField()),
                ('descripcion_repuesto', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo_sucursal', models.ForeignKey(db_column='codigo_sucursal', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.sucursal')),
                ('id_gerente', models.ForeignKey(db_column='id_gerente', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.gerente')),
                ('numero_cotizacion', models.ForeignKey(db_column='numero_cotizacion', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.cotizacion')),
                ('numero_factura', models.ForeignKey(db_column='numero_factura', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.factura')),
            ],
            options={
                'db_table': 'repuesto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrdenTrabajo',
            fields=[
                ('numero_orden_trabajo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fecha_inicio_orden_trabajo', models.DateField()),
                ('fecha_final_orden_trabajo', models.DateField()),
                ('estado_orden_trabajo', models.TextField(blank=True, null=True)),
                ('descripcion_orden_trabajo', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo_vehiculo', models.ForeignKey(db_column='codigo_vehiculo', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.vehiculo')),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.cliente')),
                ('id_jefe_taller', models.ForeignKey(db_column='id_jefe_taller', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.jefetaller')),
                ('numero_factura', models.ForeignKey(db_column='numero_factura', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.factura')),
            ],
            options={
                'db_table': 'orden_trabajo',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='jefetaller',
            name='codigo_sucursal',
            field=models.ForeignKey(db_column='codigo_sucursal', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.sucursal'),
        ),
        migrations.AddField(
            model_name='jefetaller',
            name='id_gerente',
            field=models.ForeignKey(db_column='id_gerente', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.gerente'),
        ),
        migrations.AddField(
            model_name='factura',
            name='id_vendedor',
            field=models.ForeignKey(db_column='id_vendedor', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.vendedor'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='id_vendedor',
            field=models.ForeignKey(db_column='id_vendedor', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.vendedor'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_gerente',
            field=models.ForeignKey(db_column='id_gerente', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.gerente'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_jefe_taller',
            field=models.ForeignKey(db_column='id_jefe_taller', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.jefetaller'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_vendedor',
            field=models.ForeignKey(db_column='id_vendedor', on_delete=django.db.models.deletion.DO_NOTHING, to='adminlte.vendedor'),
        ),
    ]
