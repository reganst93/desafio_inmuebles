# Generated by Django 4.2.11 on 2024-05-13 22:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('m2_construidos', models.FloatField()),
                ('m2_totales', models.FloatField()),
                ('cantidad_estacionamentos', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('cantidad_habitaciones', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('cantidad_banos', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(0)])),
                ('direccion', models.CharField(max_length=200)),
                ('comuna', models.CharField(max_length=100)),
                ('tipo_inmueble', models.CharField(choices=[('casa', 'Casa'), ('departamento', 'Departamento'), ('parcela', 'Parcela')], max_length=20)),
                ('precio_arriendo_mensual', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=9, unique=True)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999), django.core.validators.MinValueValidator(100000000)])),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('tipo_usuario', models.CharField(choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador')], max_length=20)),
            ],
        ),
    ]