from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

def home(request):
    return render(request, 'home.html')


def listado(request):
    productos = Producto.objects.all()
    search_peticion = request.GET.get('search', '')
    
    if search_peticion:
        # Filtrar productos por nombre que contengan el término de búsqueda
        productos = productos.filter(nombre_producto__icontains=search_peticion)
    
    # Pasar los productos y la consulta de búsqueda a la plantilla
    return render(request, 'listado.html', {'productos': productos, 'search_query': search_peticion})


# Crear (agregar un nuevo producto)
def producto_nuevo(request):
    if request.method == "POST":
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


















