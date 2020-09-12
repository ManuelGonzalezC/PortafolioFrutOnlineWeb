# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    rut_admin = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=25)
    apellido_p = models.CharField(max_length=25)
    apellido_m = models.CharField(max_length=25)
    telefono = models.BigIntegerField()
    email = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'admin'


class Bodega(models.Model):
    id_bodega = models.BigIntegerField(primary_key=True)
    revision_refrigerado = models.CharField(max_length=1)
    revision_envasado = models.CharField(max_length=1)
    embalaje = models.CharField(max_length=1)
    conteo = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'bodega'


class Boleta(models.Model):
    id_boleta = models.BigIntegerField(primary_key=True)
    fecha_hora = models.DateField()
    detalle_compra = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'boleta'


class Buque(models.Model):
    id_buque = models.BigIntegerField(primary_key=True)
    nombre_buque = models.CharField(max_length=10)
    puerto_asignado = models.CharField(max_length=10)
    seguro_id_seguro = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'buque'


class Cliente(models.Model):
    id_cliente = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    apellido_p = models.CharField(max_length=25)
    apellido_m = models.CharField(max_length=25)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=25)
    nombre_empresa = models.CharField(max_length=25, blank=True, null=True)
    tipo = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cliente'


class ClienteExterno(models.Model):
    id_cli = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='id_cli', primary_key=True)
    nie = models.CharField(unique=True, max_length=25)
    demanda = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cliente_externo'


class ClienteLocal(models.Model):
    id_cli = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='id_cli', primary_key=True)
    rut_cliente = models.CharField(unique=True, max_length=25)
    presupuesto = models.CharField(max_length=25)
    producto_sobrante_id_sobras = models.ForeignKey('ProductoSobrante', models.DO_NOTHING, db_column='producto_sobrante_id_sobras',related_name='sobrante_fk')

    class Meta:
        managed = False
        db_table = 'cliente_local'


class Comuna(models.Model):
    id_comuna = models.BigIntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=30)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region',related_name='region_fk')

    class Meta:
        managed = False
        db_table = 'comuna'


class Consultor(models.Model):
    rut_consul = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=25)
    apellido_p = models.CharField(max_length=25)
    apellido_m = models.CharField(max_length=25)
    telefono = models.BigIntegerField()
    email = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'consultor'


class Contrato(models.Model):
    id_contrato = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    tipo = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=50)
    estado = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'contrato'


class ContratoCliente(models.Model):
    id_contrato_cli = models.BigIntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    productoridfk = models.ForeignKey('Productor', models.DO_NOTHING, db_column='productoridfk')
    contratoidfk = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='contratoidfk')
    clienteextniefk = models.ForeignKey(ClienteExterno, models.DO_NOTHING, db_column='clienteextniefk')
    id_prodtor = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'contrato_cliente'


class Direccion(models.Model):
    id_direccion = models.BigIntegerField(primary_key=True)
    nombre_direccion = models.CharField(max_length=50)
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')

    class Meta:
        managed = False
        db_table = 'direccion'


class Fruta(models.Model):
    id_fruta = models.BigIntegerField(primary_key=True)
    tipo_fruta = models.CharField(max_length=30)
    producto_id_produ = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_produ', related_name='produidfk')

    class Meta:
        managed = False
        db_table = 'fruta'
        unique_together = (('id_fruta', 'producto_id_produ'),)


class Ganancia(models.Model):
    id_ganancias = models.BigIntegerField(primary_key=True)
    ganancia_global = models.CharField(max_length=10)
    reporte_id_reporte = models.ForeignKey('Reporte', models.DO_NOTHING, db_column='reporte_id_reporte', related_name='reportefk')
    venta_id_venta = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ganancia'


class Pago(models.Model):
    id_pago = models.BigIntegerField(primary_key=True)
    monto = models.BigIntegerField()
    fecha_pago = models.DateField()
    tipo_pago = models.CharField(max_length=20)
    conformidad = models.CharField(max_length=1)
    cliente_externo_nie = models.ForeignKey(ClienteExterno, models.DO_NOTHING, db_column='cliente_externo_nie' , related_name='cliefk')
    proce_venta_id_procventa = models.ForeignKey('ProceVenta', models.DO_NOTHING, db_column='proce_venta_id_procventa',related_name='proceventafk')
    proce_venta_admin_rut_admin = models.ForeignKey('ProceVenta', models.DO_NOTHING, db_column='proce_venta_admin_rut_admin', related_name='procerutfk')
    proce_venta_buque_id_buque = models.ForeignKey('ProceVenta', models.DO_NOTHING, db_column='proce_venta_buque_id_buque',related_name='procebuque')
    boleta_id_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='boleta_id_boleta', related_name='boletafk')

    class Meta:
        managed = False
        db_table = 'pago'
        unique_together = (('id_pago', 'cliente_externo_nie'),)


class Pais(models.Model):
    id_pais = models.BigIntegerField(primary_key=True)
    nombre_pais = models.CharField(max_length=30)
    cliente_externo_nie = models.ForeignKey(ClienteExterno, models.DO_NOTHING, db_column='cliente_externo_nie' , related_name='clieid')

    class Meta:
        managed = False
        db_table = 'pais'
        unique_together = (('id_pais', 'nombre_pais'),)


class ProceVenta(models.Model):
    id_procventa = models.BigIntegerField(primary_key=True)
    costo_transpo = models.BigIntegerField()
    impuesto_aduana = models.BigIntegerField()
    pago_servicio = models.BigIntegerField()
    comision_emp = models.BigIntegerField()
    admin_rut_admin = models.ForeignKey(Admin, models.DO_NOTHING, db_column='admin_rut_admin', related_name='adminrut')
    buque_id_buque = models.ForeignKey(Buque, models.DO_NOTHING, db_column='buque_id_buque',related_name='buqueid')
    iva = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'proce_venta'
        unique_together = (('id_procventa', 'admin_rut_admin', 'buque_id_buque'),)


class Producto(models.Model):
    id_produ = models.BigIntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=20)
    precio = models.BigIntegerField()
    id_procventa = models.CharField(max_length=10)
    bodega_id_bodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='bodega_id_bodega', related_name='bodegafk')

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoDisp(models.Model):
    id_prod_dispo = models.BigIntegerField(primary_key=True)
    precio = models.BigIntegerField()
    cantidad = models.CharField(max_length=3)
    fecha_venci = models.DateField()
    producto_id_produ = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto_id_produ', related_name='produfk')
    grado_calidad = models.CharField(max_length=25)
    total_valor = models.BigIntegerField()
    productor_id_productor = models.ForeignKey('Productor', models.DO_NOTHING, db_column='productor_id_productor', related_name='productorfk')
    id_prodtor = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'producto_disp'


class ProductoSobrante(models.Model):
    id_sobras = models.BigIntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=20)
    cantidad_sobra = models.FloatField()
    proceventa = models.ForeignKey(ProceVenta, models.DO_NOTHING, db_column='proceventa', related_name='proce_fk')
    procevenrutadmin = models.ForeignKey(ProceVenta, models.DO_NOTHING, db_column='procevenrutadmin',related_name='proceafk')
    procevenbuq = models.ForeignKey(ProceVenta, models.DO_NOTHING, db_column='procevenbuq',related_name='procebuquefk')

    class Meta:
        managed = False
        db_table = 'producto_sobrante'


class Productodispserv(models.Model):
    produ_dispo_id_prod_dispo = models.OneToOneField(ProductoDisp, models.DO_NOTHING, db_column='produ_dispo_id_prod_dispo', primary_key=True , related_name='produfk')
    servicio_id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='servicio_id_servicio', related_name='serviciofk')

    class Meta:
        managed = False
        db_table = 'productodispserv'
        unique_together = (('produ_dispo_id_prod_dispo', 'servicio_id_servicio'),)


class Productor(models.Model):
    id_prodtor = models.BigIntegerField(primary_key=True)
    rut_pro = models.CharField(max_length=15)
    nombre_pro = models.CharField(max_length=25)
    apell_p_pro = models.CharField(max_length=25)
    apell_m_pro = models.CharField(max_length=25)
    fono_pro = models.BigIntegerField()
    email_pro = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'productor'


class Region(models.Model):
    id_region = models.BigIntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=25)
    pais_id_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='pais_id_pais',related_name='paisidfk')
    pais_nombre_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='pais_nombre_pais',related_name='paisnfk')

    class Meta:
        managed = False
        db_table = 'region'


class Reporte(models.Model):
    id_reporte = models.BigIntegerField(primary_key=True)
    totalidad_reportes = models.BigIntegerField()
    resumen_info = models.CharField(max_length=100)
    estadisticas_reporte = models.CharField(max_length=100)
    consultor_rut_consul = models.ForeignKey(Consultor, models.DO_NOTHING, db_column='consultor_rut_consul',related_name='conrut')

    class Meta:
        managed = False
        db_table = 'reporte'


class Seguro(models.Model):
    id_seguro = models.BigIntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    gastos = models.BigIntegerField()
    buque_id_buque = models.CharField(max_length=10)
    buque_id_buque1 = models.ForeignKey(Buque, models.DO_NOTHING, db_column='buque_id_buque1',related_name='buquefk')

    class Meta:
        managed = False
        db_table = 'seguro'


class Servicio(models.Model):
    id_servicio = models.BigIntegerField(primary_key=True)
    nombre_servi = models.CharField(max_length=25)
    costo_servicio = models.BigIntegerField()
    descripcion = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'servicio'


class SolicitudCompra(models.Model):
    id_solicitud = models.BigIntegerField(primary_key=True)
    cantidad = models.FloatField()
    fruta = models.CharField(max_length=15)
    presupuesto = models.BigIntegerField()
    adminrut = models.ForeignKey(Admin, models.DO_NOTHING, db_column='adminrut')
    clienteextnie = models.ForeignKey(ClienteExterno, models.DO_NOTHING, db_column='clienteextnie')

    class Meta:
        managed = False
        db_table = 'solicitud_compra'


class Transpor(models.Model):
    rut_transport = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=25)
    apell_p = models.CharField(max_length=25)
    apel_m = models.CharField(max_length=25)
    fono = models.BigIntegerField()
    mail = models.CharField(max_length=25)
    productor_id_productor = models.ForeignKey(Productor, models.DO_NOTHING, db_column='productor_id_productor',related_name='produidfk')
    transporte_patente = models.CharField(max_length=6)
    transporte_patente2 = models.CharField(max_length=1)
    id_prodtor = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'transpor'


class Transporte(models.Model):
    patente = models.CharField(primary_key=True, max_length=6)
    capacidacarga = models.FloatField()
    refrigeracion = models.CharField(max_length=1)
    tipo = models.CharField(max_length=25)
    tamanio = models.CharField(max_length=25)
    transta_rut_transta = models.CharField(max_length=10)
    transta_rut_transta2 = models.CharField(max_length=10)
    transpor_rut_transport = models.ForeignKey(Transpor, models.DO_NOTHING, db_column='transpor_rut_transport', related_name='transrutfk')

    class Meta:
        managed = False
        db_table = 'transporte'


class Venta(models.Model):
    id_venta = models.BigIntegerField(primary_key=True)
    tipo_venta = models.CharField(max_length=30)
    fecha_venta = models.DateField()
    total_a_cobrar = models.BigIntegerField()
    ganancia_id_ganancias = models.ForeignKey(Ganancia, models.DO_NOTHING, db_column='ganancia_id_ganancias',related_name='gananciafk')
    proce_venta_id_procventa = models.ForeignKey(ProceVenta, models.DO_NOTHING, db_column='proce_venta_id_procventa',related_name='procevfk')
    proce_venta_admin_rut_admin = models.ForeignKey(ProceVenta, models.DO_NOTHING, db_column='proce_venta_admin_rut_admin',related_name='adminrutfk')
    proce_venta_buque_id_buque = models.ForeignKey(ProceVenta, models.DO_NOTHING, db_column='proce_venta_buque_id_buque',related_name='proce_buquefk')

    class Meta:
        managed = False
        db_table = 'venta'
