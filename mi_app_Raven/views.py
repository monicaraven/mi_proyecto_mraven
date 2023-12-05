from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import ClienteForm, ProductoForm, vendedorForm

def Agregrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Agregrar_cliente')
    else:
        form = ClienteForm()
    return render(request, 'Agregrar_cliente.html', {'form': form})

def Agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_producto')
    else:
        form = ProductoForm()
    return render(request, 'Agregar_producto.html', {'form': form})

def Buscar(request):
    if request.method == 'POST':
        term = request.POST.get('termino_busqueda')
        productos = Producto.objects.filter(nombre__icontains=term)
        return render(request, 'buscar.html', {'productos': productos})
    return render(request, 'buscar.html')

def Agregar_vendedor(request):
    if request.method == 'POST':
        form = vendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Agregar_vendedor')
    else:
        form = vendedorForm()
    return render(request, 'Agregar_vendedor.html', {'form': form})