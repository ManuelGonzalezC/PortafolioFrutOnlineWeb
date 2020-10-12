from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SubastaForm(ModelForm):

    class Meta:
        model = Subasta
        fields = ['id_subasta','costo_transporte','rut_transportista']

class ClienteInternoForm(ModelForm):

    class Meta:
        model = ClienteInterno
        fields = ['rut_clii', 'nombre_clii', 'apellido_clii', 'telefono', 'email', 'direccion', 'id_comuna']

class ClienteExternoForm(ModelForm):
    class Meta:
        model = ClienteExterno
        fields = ['nie', 'nombre_cliex', 'apellido_cliex','telefono','email', 'id_pais']

class ProductorForm(ModelForm):
    class Meta:
        model = Productor
        fields = ['rut_productor', 'nombre_productor', 'apellido_productor', 'telefono', 'email']

class RegistroClienteEx(UserCreationForm):
    nombre_cliex = forms.CharField(max_length=30, required=False, help_text='Ingrese su nombre')
    apellido_cliex = forms.CharField(max_length=30, required=False, help_text='Ingrese su apellido')
    telefono_cliex = forms.CharField(max_length=10, required=False, validators=[telefono_int], help_text='Ingrese su número de contacto')
    correo_cliex = forms.EmailField(max_length=254, help_text='Ingrese un correo válido')

    class Meta:
        model = User
        fields = ['username', 'nombre_cliex', 'apellido_cliex', 'telefono_cliex', 'correo_cliex', 'password1', 'password2']

class RegistroClienteIn(UserCreationForm):
    nombre_clii = forms.CharField(max_length=30, required=False, help_text='Ingrese su nombre')
    apellido_clii = forms.CharField(max_length=30, required=False, help_text='Ingrese su apellido')
    telefono_clii = forms.CharField(max_length=10, required=False, validators=[telefono_int], help_text='Ingrese su número de contacto')
    correo_clii = forms.EmailField(max_length=254, help_text='Ingrese un correo válido')
    direccion_clii = forms.CharField(max_length=300, required=False, help_text='Ingrese su dirección')

    class Meta:
        model = User
        fields = ['username', 'nombre_clii', 'apellido_clii', 'telefono_clii', 'correo_clii', 'direccion_clii', 'password1', 'password2']

class RegistroProductor(UserCreationForm):
    rut_productor = forms.CharField(max_length=9, required=False, validators=[rut_int], help_text= 'Ingrese su RUT')
    nombre_productor = forms.CharField(max_length=30, required=False, help_text='Ingrese su nombre')
    apellido_productor = forms.CharField(max_length=30, required=False, help_text='Ingrese su apellido')
    telefono_productor = forms.CharField(max_length=10, required=False, validators=[telefono_int], help_text='Ingrese su número de contacto')
    correo_productor = forms.EmailField(max_length=254, help_text='Ingrese un correo válido')
    
    class Meta:
        model = User
        fields = ['username', 'rut_productor', 'nombre_productor', 'apellido_productor', 'telefono_productor', 'correo_productor', 'password1', 'password2']