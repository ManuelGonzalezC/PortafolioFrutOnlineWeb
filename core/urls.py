from django.urls import path , include
<<<<<<< HEAD
from .views import ProductoViewSet , home, productos,ClientesLocales, ClientesExternos
=======
from .views import ProductoViewSet , base, productos
>>>>>>> master
from rest_framework import routers

rourter = routers.DefaultRouter()
rourter.register('productos',ProductoViewSet)

urlpatterns = [
    path('', base, name="base"),
    path('api/', include(rourter.urls)),
    path('productos/',productos ,name = "productos"),
    path('ClientesLocales/',ClientesLocales,name= "ClientesLocales"),
    path('ClientesExternos/', ClientesExternos,name= "ClientesExternos"),
    
]