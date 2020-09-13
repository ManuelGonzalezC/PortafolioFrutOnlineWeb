from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import ProductoSerializer

# Create your views here.


def productos(request):
    return render(request,'core/productos.html' )


class ProductoViewSet(viewsets.ModelViewSet):
    queryset =Producto.objects.all()
    serializer_class = ProductoSerializer