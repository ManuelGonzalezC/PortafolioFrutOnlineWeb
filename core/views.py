from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import *
from .forms import *
from .serializers import ProductoSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .decorators import *
from django.db import connection
import cx_Oracle
from .forms import SubastaForm, RegistroClienteEx
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group




def base(request):
    return render(request,'core/base.html')



@allowed_users(allowed_roles=['admin','Cliente_Externo'])
def eliminarClienteE(request, id):
    clienteE = ClienteExterno.objects.get(nie=id)
    clienteE.delete()
    
    return redirect(to= "ClientesExternos")


@allowed_users(allowed_roles=['admin','Cliente_Externo'])
def modificarClienteE(request,id):
    clienteE = ClienteExterno.objects.get(nie=id)
    data = {
        'form': ClienteExternoForm(instance=clienteE)
    }
    if request.method == 'POST':
        formulario = ClienteExternoForm(request.POST, instance=clienteE)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
            data['form'] = formulario
    return render(request, 'core/modificarClienteE.html', data)

@allowed_users(allowed_roles=['admin','Cliente_Externo'])
def ClientesExternos(request): #Agregar y listar
    clientesE = ClienteExterno.objects.all()
    data = {
        'form': ClienteExternoForm(),
        'ClientesE': clientesE
    }
    if request.method == 'POST':
        formulario = ClienteExternoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Guardado Correctamente'
    return render(request, 'core/ClientesExternos.html', data)


@allowed_users(allowed_roles=['admin','Cliente_Interno'])
def eliminarClienteI(request,id):
    ClientesI = ClienteInterno.objects.get(rut_clii=id)
    ClientesI.delete()
    return redirect(to = 'ClientesInternos')

@allowed_users(allowed_roles=['admin','Cliente_Interno'])
def modificarClienteI(request, id):
    ClientesI = ClienteInterno.objects.get(rut_clii=id)
    data = {
        'form': ClienteInternoForm(instance= ClientesI)
    }

    if request.method == 'POST':
        formulario= ClienteInternoForm(data=request.POST, instance= ClientesI)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario

    return render(request, 'core/modificarClienteI.html', data)


@allowed_users(allowed_roles=['admin','Cliente_Interno'])
def ClientesInternos(request): #Agregar y listar
    ClientesI =ClienteInterno.objects.all()
    data = {
        'form': ClienteInternoForm(),
        'ClientesI': ClientesI
    }
    if request.method == 'POST':
        formulario = ClienteInternoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Guardado Correctamente'

    return render(request, 'core/ClientesInternos.html', data)

@permission_required('core.view_producto')
@allowed_users(allowed_roles=['admin','Productor_grupo'])
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

@permission_required('core.view_producto')
@allowed_users(allowed_roles=['admin','Productor_grupo'])
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

@allowed_users(allowed_roles=['admin','Productor_grupo'])
def listado_categorias_fruta():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_TIPOFRUTA_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

@allowed_users(allowed_roles=['admin','Productor_grupo'])
def listado_idproductor_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_IDPRODUCTOR_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

@permission_required('core.add_producto')
@allowed_users(allowed_roles=['admin','Productor_grupo'])
def agregar_producto(nombre,id_fruta,precio,calidad,rut_productor):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_PRODUCTO",[nombre,id_fruta,precio,calidad,rut_productor, salida])
    return salida.getvalue()

@permission_required('core.view_subasta')
@allowed_users(allowed_roles=['admin','Transportista_grupo'])
def list_subastas(request):
    subasta = Subasta.objects.all()
    data_sub = {
        'subasta':subasta
    }
    return render(request,'core/list_subastas.html', data_sub)

@permission_required('core.add_subasta')
@allowed_users(allowed_roles=['admin','Transportista_grupo'])
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

@permission_required('core.change_subasta')
@allowed_users(allowed_roles=['admin','Transportista_grupo'])
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

@permission_required('core.delete_subasta')
@allowed_users(allowed_roles=['admin','Transportista_grupo'])
def eliminar_subasta(request, id):
    subasta = Subasta.objects.get(id_subasta=id)
    subasta.delete()
    return redirect(to="list_subastas")

def listado_productores(request):
    productores = Productor.objects.all()
    data = {
        'Productores': productores # la variable 'Peliculas ' definida en el diccionario python "data" es como debo llamar el listado de productores desde el template
    }
    return render(request, 'core/listado_productores.html', data)

def nuevos_productores(request):
    data = {
        'form': ProductorForm()
    }

    if request.method == "POST":
        formulario = ProductorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Guardado correctamente"

    return render(request, 'core/nuevos_productores.html', data)

def modificar_productores(request, id):
    productores = Productor.objects.get(rut_productor=id)
    data = {
        'form': ProductorForm(instance=productores)
    }

    if request.method == "POST":
        formulario = ProductorForm(data=request.POST, instance=productores)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario 
    return render(request, 'core/modificar_productores.html', data)

def eliminar_productores(request, id):
     productor = Productor.objects.get(rut_productor=id)
     productor.delete()

     return redirect(to="listado_productores")



def registroClienteEx(request):
    if request.method == 'POST':
        form = RegistroClienteEx(request.POST)
        profile_form = ClienteExternoForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = profile_form.save()
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            group = Group.objects.get(name='Cliente_Externo')
            user.groups.add(group)
            login(request, user)
            return redirect('home')
    else:
        form = RegistroClienteEx()
        profile_form = ClienteExternoForm()
    return render(request, 'registration/registroClienteEx.html', {'form': form, 'profile_form': profile_form})

def registroClienteIn(request):
    if request.method == 'POST':
        form = RegistroClienteIn(request.POST)
        profile_form = ClienteInternoForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = profile_form.save()
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            group = Group.objects.get(name='Cliente_Interno')
            user.groups.add(group)
            login(request, user)
            return redirect('home')
    else:
        form = RegistroClienteIn()
        profile_form = ClienteInternoForm()
    return render(request, 'registration/registroClienteI.html', {'form': form, 'profile_form': profile_form})

def registroProductor(request):
    if request.method == 'POST':
        form = RegistroProductor(request.POST)
        profile_form = ProductorForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            group = Group.objects.get(name='Productor_grupo')
            user.groups.add(group)
            login(request, user)
            return redirect('productos')
    else:
        form = RegistroProductor()
        profile_form = ProductorForm()
    return render(request, 'registration/registroProductor.html', {'form': form, 'profile_form': profile_form})

def list_solicitud_ext(request):
    solicitud_ext = SolicitudCompraExt.objects.all()
    data = {'solicitud_ext': solicitud_ext}
    return render(request, 'core/list_solicitudes_ext.html', data)

def ingresar_solicitud_ext(request):
    data = {
        'form': SolicitudExtForm()
    }
    if request.method == 'POST':
        formulario = SolicitudExtForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Solicitud guardada correctamente"
    return render(request, 'core/ingresar_solicitud_ext.html', data)

