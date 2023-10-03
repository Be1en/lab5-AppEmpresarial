from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_dare = models.DateTimeField('date published')
    def __str__(self):
        return self.nombre
    

class Clientes(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    dni = models.DecimalField(max_digits=8, decimal_places=0)
    telefono = models.DecimalField(max_digits=6, decimal_places=0)
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fecha_nac = models.DateTimeField('Fecha Nacimiento')
    fecha_public = models.DateTimeField('Fecha Publicación')
    
    def __str__(self):
        return self.nombres
    