# Generated by Django 3.1.1 on 2020-09-13 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteExterno',
            fields=[
                ('nie', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre_cliex', models.CharField(max_length=25)),
                ('apellido_cliex', models.CharField(max_length=25)),
                ('telefono', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cliente_externo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClienteInterno',
            fields=[
                ('rut_clii', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_clii', models.CharField(max_length=25)),
                ('apellido_clii', models.CharField(max_length=25)),
                ('telefono', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cliente_interno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ComunaLocal',
            fields=[
                ('id_comuna', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_comuna', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'comuna_local',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id_contrato', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
            options={
                'db_table': 'contrato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DireccionLocal',
            fields=[
                ('id_direccion', models.BigAutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'direccion_local',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fruta',
            fields=[
                ('id_fruta', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'fruta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MetodoPagoE',
            fields=[
                ('id_metodo_pago', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_metodo_pago', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'metodo_pago_e',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MetodoPagoL',
            fields=[
                ('id_metodo_pago', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_metodo_pago', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'metodo_pago_l',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PagoEx',
            fields=[
                ('id_pagoex', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_pagoex', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pago_ex',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PagoI',
            fields=[
                ('id_pagoi', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_pago', models.DateField()),
            ],
            options={
                'db_table': 'pago_i',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'pais',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProcesoVentaEx',
            fields=[
                ('id_proceso_ex', models.BigAutoField(primary_key=True, serialize=False)),
                ('impuesto_aduana', models.BigIntegerField()),
                ('comision_empresa', models.BigIntegerField()),
            ],
            options={
                'db_table': 'proceso_venta_ex',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProcesoVentaLocal',
            fields=[
                ('id_vental', models.BigAutoField(primary_key=True, serialize=False)),
                ('costo_transporte', models.BigIntegerField()),
                ('comision_empresa', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'proceso_venta_local',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('precio', models.BigIntegerField()),
                ('calidad', models.BigIntegerField()),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productor',
            fields=[
                ('rut_productor', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_productor', models.CharField(max_length=25)),
                ('apellido_productor', models.CharField(max_length=25)),
                ('telefono', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'productor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductoSobrante',
            fields=[
                ('id_produs', models.BigAutoField(primary_key=True, serialize=False)),
                ('precio_kilo', models.BigIntegerField()),
                ('stock', models.BigIntegerField()),
            ],
            options={
                'db_table': 'producto_sobrante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegionLocal',
            fields=[
                ('id_region', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_region', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'region_local',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReporteEx',
            fields=[
                ('id_reporte', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=1000)),
                ('id_pagoe', models.BigIntegerField()),
            ],
            options={
                'db_table': 'reporte_ex',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReporteLocal',
            fields=[
                ('id_reporte', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'reporte_local',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SolicitudCompraExt',
            fields=[
                ('id_solicitud', models.BigAutoField(primary_key=True, serialize=False)),
                ('presupuesto', models.BigIntegerField()),
                ('id_producto', models.BigIntegerField()),
            ],
            options={
                'db_table': 'solicitud_compra_ext',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subasta',
            fields=[
                ('id_subasta', models.BigAutoField(primary_key=True, serialize=False)),
                ('costo_transporte', models.BigIntegerField()),
            ],
            options={
                'db_table': 'subasta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TransporteFinal',
            fields=[
                ('id_transf', models.BigAutoField(primary_key=True, serialize=False)),
                ('seguro', models.CharField(max_length=2)),
                ('coste_seguro', models.BigIntegerField()),
            ],
            options={
                'db_table': 'transporte_final',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transportista',
            fields=[
                ('rut_transportista', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_transportista', models.CharField(max_length=25)),
                ('apellido_transportista', models.CharField(max_length=25)),
                ('telefono', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'transportista',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('capacidad', models.BigIntegerField()),
                ('refigeracion', models.CharField(max_length=2)),
                ('tamanio', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'vehiculo',
                'managed': False,
            },
        ),
    ]
