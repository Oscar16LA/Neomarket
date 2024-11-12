from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listado/', views.listado, name='listado'),
    path('productos/nuevo/', views.producto_nuevo, name='producto_nuevo'),
    path('productos/<int:id>/', views.producto_detalle, name='producto_detalle'),
    path('productos/<int:id>/editar/', views.producto_editar, name='producto_editar'),
    path('productos/<int:id>/eliminar/', views.producto_eliminar, name='producto_eliminar'),
]
