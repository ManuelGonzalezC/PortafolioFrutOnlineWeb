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
    correo_cliex = forms.EmailField(max_length=254, help_text='Ingrese un correo válido')

    class Meta:
        model = User
        fields = ['username', 'nombre_cliex', 'apellido_cliex', 'correo_cliex', 'password1', 'password2']

