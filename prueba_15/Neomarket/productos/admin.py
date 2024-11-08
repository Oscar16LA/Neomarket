from django.contrib import admin
from .models import Producto

# Clase de configuración para personalizar la visualización del modelo Producto en el panel de administración

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'nombre_tienda', 'precio')
    search_fields = ('nombre_producto', 'nombre_tienda')


admin.site.register(Producto, ProductoAdmin)
