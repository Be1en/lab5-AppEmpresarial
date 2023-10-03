
from django import forms

class ActualizarStockForm(forms.Form):
    nuevo_stock = forms.IntegerField(label='Nuevo Stock')

class ActualizarPrecioForm(forms.Form):
    nuevo_precio = forms.DecimalField(label='Nuevo Precio')