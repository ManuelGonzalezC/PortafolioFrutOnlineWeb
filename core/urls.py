from django.urls import path , include
from .views import ProductoViewSet , base, productos, ClientesExternos, ClientesInternos, modificarClienteE, eliminarClienteE, modificarClienteI, eliminarClienteI
from rest_framework import routers

rourter = routers.DefaultRouter()
rourter.register('productos',ProductoViewSet)

urlpatterns = [
    path('', base, name="base"),
    path('api/', include(rourter.urls)),
    path('productos/',productos ,name = "productos"),
    path('ClientesExternos/', ClientesExternos,name= "ClientesExternos"),
    path('ClientesInternos/', ClientesInternos, name= "ClientesInternos"),
    path('modificarClienteI/<id>/', modificarClienteI,name="modificarClienteI"),
    path('modificarClienteE/<id>/', modificarClienteE, name="modificarClienteE"),
    path('eliminarClienteE/<id>/', eliminarClienteE, name= "eliminarClienteE"),
    path('eliminarClienteI/<id>/', eliminarClienteI, name="eliminarClienteI"),
    
]