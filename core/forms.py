from django import forms
from django.forms import ModelForm
from .models import *

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

