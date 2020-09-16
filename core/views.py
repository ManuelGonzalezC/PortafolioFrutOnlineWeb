from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import *
from .serializers import ProductoSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db import connection
import cx_Oracle


# Create your views here.

def home(request):
    return render(request,'core/base.html')

def ClientesExternos(request):
    clientesE = ClienteExterno.objects.all()
    data = {
        'ClienteExterno': clientesE
    }
    return render(request, 'core/ClientesExternos.html', data)

def ClientesLocales(request):
    clientesL =ClienteInterno.objects.all()
    data = {
        'ClienteLocal': clientesL
    }

    if request.method == 'POST':
        rut = request.POST.get('rutLocal')
        nombre = request.POST.get('nombreLocal')
        apellido = request.POST.get('apellidoLocal')
        telefono = request.POST.get('telefonoLocal')
        email = request.POST.get('emailLocal')
        direccion = request.POST.get('direccion')
        comuna = request.POST.get(id_comuna)
        agregar_ClienteLocal = agregar_ClienteLocal(rut, nombre, apellido, telefono, email, direccion, id_comuna)
        if agregar_ClienteLocal == 1:
            data['mensaje'] = 'Agregado Correctamente'
        else:
            data['mensaje'] = 'no se pudo agregar'
    return render(request, 'core/ClientesLocales.html', data)

def productos(request):
    data = {
        'productos':listado_productos(),
        'tipo_fruta':listado_categorias_fruta(),
        'id_productor':listado_idproductor_productos(),
    }

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        id_fruta = request.POST.get('tipofruta')
        precio = request.POST.get('precio')
        calidad = request.POST.get('calidad')
        rut_productor = request('id_productor')
        salida = agregar_producto(nombre,id_fruta,precio,calidad,rut_productor)
        if salida == 1:
            data['mensaje'] = 'Agregado Correctamente'
        else:
            data['mensaje'] = 'no se pudo agregar'

    return render(request,'core/productos.html',data)


class ProductoViewSet(viewsets.ModelViewSet):
    queryset =Producto.objects.all()
    serializer_class = ProductoSerializer

## Procedimientos Almacenados
def listado_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_categorias_fruta():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_TIPOFRUTA_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_idproductor_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_IDPRODUCTOR_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def agregar_producto(nombre,id_fruta,precio,calidad,rut_productor):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_PRODUCTO",[nombre,id_fruta,precio,calidad,rut_productor, salida])
    return salida.getvalue()
