from rest_framework import serializers
from .models import *

class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = ['nombre','precio', 'calidad','id_fruta','rut_productor']

class ProductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productor
        fields = ['rut_productor', 'nombre_productor', 'apellido_productor', 'telefono', 'email']