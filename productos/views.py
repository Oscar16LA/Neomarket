from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

def home(request): # Filtra los productos cuyo precio es menor a 10.00 y los almacena en productos_promocion
    productos_promocion = Producto.objects.filter(precio__lt=10.00)
      # Filtra los productos cuyo precio es mayor o igual a 10.00 y los almacena en productos_no_promocion
    productos_no_promocion = Producto.objects.filter(precio__gte=10.00)
    return render(request, 'home.html', {
        'productos_promocion': productos_promocion, # Enviamos los productos en promoción al template
        'productos_no_promocion': productos_no_promocion # Enviamos los productos no en promoción al template
    })


def listado(request):
    productos = Producto.objects.all()
    search_peticion = request.GET.get('search', '')
    
    if search_peticion:
        # Filtrar productos por nombre que contengan el término de búsqueda
        productos = productos.filter(nombre_producto__icontains=search_peticion)
    
    # Pasar los productos y la consulta de búsqueda a la plantilla
    return render(request, 'listado.html', {'productos': productos, 'search_peticion': search_peticion})


# Crear (agregar un nuevo producto)
def producto_nuevo(request):
     # Verifica si la solicitud es de tipo POST (enviado por el formulario para crear un producto)
    if request.method == "POST":
        # Se crea una instancia de ProductoForm, cargando los datos enviados por POST
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado')  # Redirige a la lista de productos
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})

# Leer (detalles del producto)
def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'producto_detalle.html', {'producto': producto})

# Actualizar (editar un producto existente)
def producto_editar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_detalle', id=producto.id)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_form.html', {'form': form})

# Eliminar (eliminar un producto)
def producto_eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
        return redirect('listado')
    return render(request, 'producto_confirmar_eliminar.html', {'producto': producto})


















