from django.urls import path , include
from .views import ProductoViewSet , base, productos
from rest_framework import routers

rourter = routers.DefaultRouter()
rourter.register('productos',ProductoViewSet)

urlpatterns = [
    path('', base, name="base"),
    path('api/', include(rourter.urls)),
    path('productos/',productos ,name = "productos"),
]