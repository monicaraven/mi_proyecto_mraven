
from django import forms
from .models import Cliente, Producto, vendedor

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion']


class vendedorForm(forms.ModelForm):
    class Meta:
        model = vendedor
        fields = ['nombre', 'legajo']
