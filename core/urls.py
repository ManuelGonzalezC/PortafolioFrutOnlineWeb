from django.urls import path , include
from .views import ProductoViewSet , base, productos, list_subastas, ingresar_subasta, mod_subasta, eliminar_subasta
from rest_framework import routers

rourter = routers.DefaultRouter()
rourter.register('productos',ProductoViewSet)

urlpatterns = [
    path('', base, name="home"),
    path('api/', include(rourter.urls)),
    path('productos/',productos ,name = "productos"),
    path('list_subastas/', list_subastas, name = "list_subastas"),
    path('ingresar_subasta/', ingresar_subasta, name = "ingresar_subasta"),
    path('mod_subastas/<id>/', mod_subasta, name = "mod_subastas"),
    path('eliminar_subasta/<id>/', eliminar_subasta, name = "eliminar_subasta"),
]