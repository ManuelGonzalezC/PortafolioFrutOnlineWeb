from django.urls import path , include
from .views import *
from rest_framework import routers

rourter = routers.DefaultRouter()
rourter.register('productos',ProductoViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('api/', include(rourter.urls)),
    path('productos/',productos ,name = "productos"),
    path('eliminar-producto/<id>',eliminar_producto,name="eliminar_producto" )
]