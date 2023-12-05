from django.urls import path
from .views import Agregrar_cliente, Agregar_producto, Buscar, Agregar_vendedor

urlpatterns = [
    path('agregar-cliente/', Agregrar_cliente, name='Agregrar_cliente'),
    path('agregar-producto/', Agregar_producto, name='agregar_producto'),
    path('buscar/', Buscar, name='buscar'),
    path('agregar_vendedor/', Agregar_vendedor, name='Agregar_vendedor'),
]
