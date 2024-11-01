from django.db import models

class Producto(models.Model):

    
    # Modelo 'Producto' que representa un producto en la tienda.
    # Contiene información sobre el nombre de la tienda, el nombre del producto, 
    # una descripción y el precio.
   
    nombre_tienda = models.CharField(max_length=100)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre_producto} - {self.nombre_tienda}"
    
    # Nota: Los demás modelos se agregarán según las necesidades del proyecto.
    # Modelos futuros: Pedido, Pago etc.
