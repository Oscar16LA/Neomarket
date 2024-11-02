from django.urls import path
from . import views 
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', TemplateView.as_view(template_name='listado.html'), name='listado'),


]
