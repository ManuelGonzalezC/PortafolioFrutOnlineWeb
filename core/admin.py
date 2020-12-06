from django.contrib import admin
from .models import *
from django.conf import settings

# Register your models here.
admin.site.register(Vehiculo)
admin.site.register(Transportista)
admin.site.register(Producto)
admin.site.register(ClienteInterno)
admin.site.register(Fruta)
admin.site.register(Subasta)
admin.site.register(ClienteExterno)
admin.site.register(Productor)
admin.site.register(SolicitudCompraExt)
admin.site.register(ProductoSobrante)


