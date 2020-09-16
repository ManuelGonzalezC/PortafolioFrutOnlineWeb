from django import forms
from django.forms import ModelForm
from .models import *

class ClienteInternoForm(ModelForm):

    class Meta:
        model = ClienteInterno
        fields = ['rut_clii', 'nombre_clii', 'apellido_clii', 'telefono', 'email', 'direccion', 'id_comuna']

class ClienteExternoForm(ModelForm):
    class Meta:
        model = ClienteExterno
        fields = ['nie', 'nombre_cliex', 'apellido_cliex','telefono','email', 'id_pais']