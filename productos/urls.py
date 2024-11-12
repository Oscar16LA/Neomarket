from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página principal llamda home. 
    path('listado/', views.listado, name='listado'),  # Ruta para listar los productos.
    path('productos/nuevo/', views.producto_nuevo, name='producto_nuevo'), # Ruta para crear un nuevo producto.
    path('productos/<int:id>/', views.producto_detalle, name='producto_detalle'),  # Ruta para ver los detalles de un producto específico.
    path('productos/<int:id>/editar/', views.producto_editar, name='producto_editar'),  # Ruta para editar un producto específico.
    path('productos/<int:id>/eliminar/', views.producto_eliminar, name='producto_eliminar'),   # Ruta para eliminar un producto específico.
]
