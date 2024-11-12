from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_tienda', 'nombre_producto', 'descripcion', 'precio']
