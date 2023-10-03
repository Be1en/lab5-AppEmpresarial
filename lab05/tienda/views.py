from django.shortcuts import render
from .models import Producto

def cambiar_stock(request):
    if request.method == 'POST':
        nuevo_stock = request.POST.get('nuevo_stock')
        productos_ids = request.POST.getlist('productos_ids[]')
        
        # Actualizar el stock de los productos seleccionados
        Producto.objects.filter(id__in=productos_ids).update(stock=nuevo_stock)
        
    productos = Producto.objects.all()
    return render(request, 'cambiar_stock.html', {'productos': productos})
