from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    rut = models.CharField(max_length=9, unique=True,null=False, blank=False)
    direccion = models.CharField(max_length=200, null=False, blank=False)
    telefono = models.IntegerField(null=False, blank=False,
        validators=[
            MaxValueValidator(999999999),
            MinValueValidator(100000000)
        ])
    correo = models.EmailField(unique=True,null=False, blank=False)
    tipo_usuario_choices = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    )
    tipo_usuario = models.CharField(max_length=20, choices = tipo_usuario_choices, null=False, blank=False,)

class Inmueble(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False,)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    cantidad_estacionamentos = models.IntegerField(
        validators=[
            MaxValueValidator(100),  
            MinValueValidator(0) 
        ]
    )
    cantidad_habitaciones = models.IntegerField(
        validators=[
            MaxValueValidator(100),  
            MinValueValidator(0) 
        ]
    )
    cantidad_banos = models.IntegerField(
        validators=[
            MaxValueValidator(50),  
            MinValueValidator(0) 
        ]
    )
    direccion = models.CharField(max_length=200, null=False, blank=False)
    comuna = models.CharField(max_length=100)
    tipo_inmueble_choices = (
        ('casa', 'Casa'),
        ('departamento','Departamento'),
        ('parcela','Parcela'),
    )
    tipo_inmueble = models.CharField(max_length=20, choices = tipo_inmueble_choices)
    precio_arriendo_mensual = models.IntegerField( null=False, blank=False)

