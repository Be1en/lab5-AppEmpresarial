from django.contrib import admin
from django.http import JsonResponse
from django.shortcuts import render
from .models import Categoria, Producto, Clientes

class ProductoAdmin(admin.ModelAdmin):
    actions = ['actualizar_stock_varios', 'actualizar_precio_varios', 'cambiar_stock_varios']

    # ... tus otras acciones personalizadas ...

    def cambiar_stock_varios(self, request, queryset):
        if request.method == 'POST':
            nuevo_stock = request.POST.get('nuevo_stock')
            if nuevo_stock is not None:
                # Actualiza el stock de los productos seleccionados
                queryset.update(stock=nuevo_stock)
                self.message_user(request, f'Se ha actualizado el stock de {queryset.count()} productos.')
                return

        context = {
            'action': 'cambiar_stock',
            'productos': queryset
        }
        return render(request, 'cambiar_stock.html', context)

    cambiar_stock_varios.short_description = "Cambiar Stock Varios"

    def obtener_productos(request):
        productos_queryset = Producto.objects.all().values()  # Convierte QuerySet a lista de diccionarios
        productos_lista = list(productos_queryset)  # Convierte QuerySet a lista
        return JsonResponse({'productos': productos_lista})  # Serializa la lista a JSON y envía como respuesta

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Clientes)
