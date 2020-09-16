from django.urls import path , include
from .views import *
from rest_framework import routers

rourter = routers.DefaultRouter()
rourter.register('productos',ProductoViewSet)

urlpatterns = [

    path('', base, name="home"),
    path('list_subastas/', list_subastas, name = "list_subastas"),
    path('ingresar_subasta/', ingresar_subasta, name = "ingresar_subasta"),
    path('mod_subastas/<id>/', mod_subasta, name = "mod_subastas"),
    path('eliminar_subasta/<id>/', eliminar_subasta, name = "eliminar_subasta"),
    path('api/', include(rourter.urls)),
    path('productos/',productos ,name = "productos"),
    path('ClientesExternos/', ClientesExternos,name= "ClientesExternos"),
    path('ClientesInternos/', ClientesInternos, name= "ClientesInternos"),
    path('modificarClienteI/<id>/', modificarClienteI,name="modificarClienteI"),
    path('modificarClienteE/<id>/', modificarClienteE, name="modificarClienteE"),
    path('eliminarClienteE/<id>/', eliminarClienteE, name= "eliminarClienteE"),
    path('eliminarClienteI/<id>/', eliminarClienteI, name="eliminarClienteI"),
    path('listado-productores/', listado_productores, name="listado_productores"),
    path('nuevos-productores/', nuevos_productores, name="nuevos_productores"),
    path('modificar-productores/<id>/', modificar_productores, name="modificar_productores"),
    path('eliminar-productores/<id>/', eliminar_productores, name="eliminar_productores"),
]