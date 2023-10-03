# Generated by Django 4.2.5 on 2023-09-29 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('dni', models.DecimalField(decimal_places=0, max_digits=8)),
                ('telefono', models.DecimalField(decimal_places=0, max_digits=6)),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('fecha_nac', models.DateTimeField(verbose_name='Fecha Nacimiento')),
                ('fecha_public', models.DateTimeField(verbose_name='Fecha Publicación')),
            ],
        ),
    ]