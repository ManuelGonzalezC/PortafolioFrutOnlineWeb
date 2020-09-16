from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import ProductoSerializer
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def base(request):
    return render(request,'core/base.html')

def productos(request):
    return render(request,'core/productos.html' )


class ProductoViewSet(viewsets.ModelViewSet):
    queryset =Producto.objects.all()
    serializer_class = ProductoSerializer