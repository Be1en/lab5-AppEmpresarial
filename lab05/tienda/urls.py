from django.urls import path
from . import views

urlpatterns = [
    # Otras URL de la aplicación
    path('cambiar-stock/', views.cambiar_stock, name='cambiar_stock'),
]
