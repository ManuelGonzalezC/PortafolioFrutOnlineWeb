from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import Order

#class OrderForm(ModelForm):
#    class Meta:
#        model = Order
#        fields = '__all__'

class SubastaForm(ModelForm):

    class Meta:
        model = Subasta
        fields = ['id_subasta','costo_transporte','rut_transportista']

class ClienteInternoForm(forms.ModelForm):
    class Meta:
        model = ClienteInterno
        fields = ['rut_clii', 'nombre_clii', 'apellido_clii', 'telefono', 'email', 'direccion', 'id_comuna']
       

class ClienteExternoForm(forms.ModelForm):
    class Meta:
        model = ClienteExterno
        fields = ['nie', 'nombre_cliex', 'apellido_cliex','telefono','email', 'id_pais']


class ProductorForm(forms.ModelForm):
    class Meta:
        model = Productor
        fields = ['rut_productor', 'nombre_productor', 'apellido_productor', 'telefono', 'email']

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre', 'precio', 'calidad', 'id_fruta', 'rut_productor']

class TransportistaForm(forms.ModelForm):
    class Meta:
        model = Transportista
        fields = ['rut_transportista', 'nombre_transportista', 'apellido_transportista', 'telefono', 'email']

class RegistroClienteEx(UserCreationForm):
    #nombre_cliex = forms.CharField(max_length=30, required=False, help_text='Ingrese su nombre')
    #apellido_cliex = forms.CharField(max_length=30, required=False, help_text='Ingrese su apellido')
    #telefono_cliex = forms.CharField(max_length=10, required=False, validators=[telefono_int], help_text='Ingrese su número de contacto')
    #correo_cliex = forms.EmailField(max_length=254, help_text='Ingrese un correo válido')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class RegistroClienteIn(UserCreationForm):
    #nombre_clii = forms.CharField(max_length=30, required=False, help_text='Ingrese su nombre')
    #apellido_clii = forms.CharField(max_length=30, required=False, help_text='Ingrese su apellido')
    #telefono_clii = forms.CharField(max_length=10, required=False, validators=[telefono_int], help_text='Ingrese su número de contacto')
    #correo_clii = forms.EmailField(max_length=254, help_text='Ingrese un correo válido')
    #direccion_clii = forms.CharField(max_length=300, required=False, help_text='Ingrese su dirección')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class RegistroProductor(UserCreationForm):
    #rut_productor = forms.CharField(max_length=9, required=False, validators=[rut_int], help_text= 'Ingrese su RUT')
    #nombre_productor = forms.CharField(max_length=30, required=False, help_text='Ingrese su nombre')
    #apellido_productor = forms.CharField(max_length=30, required=False, help_text='Ingrese su apellido')
    #telefono_productor = forms.CharField(max_length=10, required=False, validators=[telefono_int], help_text='Ingrese su número de contacto')
    #correo_productor = forms.EmailField(max_length=254, help_text='Ingrese un correo válido')
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class RegistroTransportista(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class SolicitudExtForm(ModelForm):
    class Meta:
        model = SolicitudCompraExt
        fields = ['id_solicitud', 'presupuesto', 'id_producto', 'nie', 'id_fruta']

class ProcesoLocalForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProcesoLocalForm, self).__init__(*args, **kwargs)
        self.fields['costo_transporte'].widget.attrs['readonly'] = True
        self.fields['comision_empresa'].widget.attrs['readonly'] = True

    class Meta:
        model = ProcesoVentaLocal
        fields = ['id_vental', 'costo_transporte', 'comision_empresa', 'rut_clii', 'id_produs', 'id_estado']

class PagoInternoForm(ModelForm):

    class Meta:
        model = PagoI
        fields = ['id_pagoi', 'fecha_pago', 'id_metodo_pago', 'id_vental']

