from django.shortcuts import render

# Definimos la vista de la página principal  que es home.html

def home(request):
    return render(request, 'home.html')


from .models import Producto # Importamos el modelo producto desde la aplicación.

def listado(request):
    productos = Producto.objects.all() # Le pedimos que nos muestre todos los productos.
    return render(request, 'listado.html', {'productos': productos})













