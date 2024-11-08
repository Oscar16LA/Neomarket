from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    USUARIO_TIPO_CHOICES = [
        ('cliente', 'Cliente'),
        ('tienda', 'Tienda'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=USUARIO_TIPO_CHOICES)

    def __str__(self):
        return f'{self.usuario.username} - {self.tipo}'


class Producto(models.Model):
    tienda = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        limit_choices_to={'tipo': 'tienda'},
        related_name='productos'
    )
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    cliente = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        limit_choices_to={'tipo': 'cliente'},
        related_name='carritos'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField(Producto, through='CarritoProducto')

    def __str__(self):
        return f'Carrito de {self.cliente.usuario.username} - {self.fecha_creacion.strftime("%Y-%m-%d")}'


class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre} en {self.carrito}'


class Pago(models.Model):
    cliente = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        limit_choices_to={'tipo': 'cliente'},
        related_name='pagos'
    )
    estado = models.CharField(max_length=50, default='pendiente')
    fecha_pago = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Pago de {self.cliente.usuario.username} - Estado: {self.estado}'


class Pedido(models.Model):
    cliente = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        limit_choices_to={'tipo': 'cliente'},
        related_name='pedidos'
    )
    productos = models.ManyToManyField(Producto, through='PedidoProducto')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='pendiente')

    def __str__(self):
        return f'Pedido {self.id} de {self.cliente.usuario.username}'


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre} en Pedido {self.pedido.id}'


class Venta(models.Model):
    tienda = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        limit_choices_to={'tipo': 'tienda'},
        related_name='ventas'
    )
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='ventas')
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Venta de {self.tienda.usuario.username} - Pedido {self.pedido.id}'
