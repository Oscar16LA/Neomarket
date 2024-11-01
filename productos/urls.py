from django.urls import path
from . import views 

# Definimos las rutas URL de la aplicación
urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.listado, name='listado')

]
