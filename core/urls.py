from django.urls import path , include
from .views import ProductoViewSet
from rest_framework import routers

rourter = routers.DefaultRouter()
rourter.register('productos',ProductoViewSet)

urlpatterns = [
    path('api/', include(rourter.urls)),
]