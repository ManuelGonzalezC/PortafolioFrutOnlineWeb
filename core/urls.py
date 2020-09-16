from django.urls import path , include
from .views import ProductoViewSet , home, productos,ClientesLocales, ClientesExternos
from rest_framework import routers

rourter = routers.DefaultRouter()
rourter.register('productos',ProductoViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('api/', include(rourter.urls)),
    path('productos/',productos ,name = "productos"),
    path('ClientesLocales/',ClientesLocales,name= "ClientesLocales"),
    path('ClientesExternos/', ClientesExternos,name= "ClientesExternos"),
    
]