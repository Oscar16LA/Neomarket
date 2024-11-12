from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm): # Define la clase `ProductoForm`, un formulario basado en el modelo `Producto`.
    class Meta:
        model = Producto  # Define el modelo en el que se basa el formulario. 
        fields = ['nombre_tienda', 'nombre_producto', 'descripcion', 'precio'] # Define los campos del modelo `Producto` que se incluirán en el formulario.
