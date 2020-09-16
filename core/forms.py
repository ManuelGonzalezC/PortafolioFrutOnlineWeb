from django import forms
from django.forms import ModelForm
from .models import Subasta

class SubastaForm(ModelForm):

    class Meta:
        model = Subasta
        fields = ['id_subasta','costo_transporte','rut_transportista']