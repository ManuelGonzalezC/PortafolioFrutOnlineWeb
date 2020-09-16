from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import *
from .serializers import ProductoSerializer
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db import connection
import cx_Oracle
from .forms import SubastaForm


# Create your views here.

@login_required
def base(request):
    return render(request,'core/base.html')

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
    queryset = Producto.objects.all()
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

def list_subastas(request):
    subasta = Subasta.objects.all()
    data_sub = {
        'subasta':subasta
    }
    return render(request,'core/list_subastas.html', data_sub)

def ingresar_subasta(request):
    data_sf = {
        'form':SubastaForm
    }
    if request.method == "POST":
        formulario = SubastaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data_sf['mensaje'] = "Subasta creada exitosamente"

    return render(request, 'core/ingresar_subasta.html', data_sf)

def mod_subasta(request, id):
    subasta = Subasta.objects.get(id_subasta=id)
    data_mod = {
        'form':SubastaForm(instance=subasta)
    }

    if request.method == 'POST':
        formulario = SubastaForm(data=request.POST, instance=subasta)
        if formulario.is_valid():
            formulario.save()
            data_mod['mensaje'] = "Subasta modificada exitosamente"
            data_mod['form'] = formulario

    return render(request, 'core/mod_subastas.html', data_mod)

def eliminar_subasta(request, id):
    subasta = Subasta.objects.get(id_subasta=id)
    subasta.delete()
    return redirect(to="list_subastas")