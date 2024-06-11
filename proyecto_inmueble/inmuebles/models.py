from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group




# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, rut, password=None, **extra_fields):
        if not rut:
            raise ValueError('El campo RUT es obligatorio')
        user = self.model(rut=rut, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        if user.tipo_usuario == 'arrendador':
            group = Group.objects.get(name='Arrendador')
        else:
            group = Group.objects.get(name='Arrendatario')
        user.groups.add(group)

        return user

    def create_superuser(self, rut, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(rut, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    rut = models.CharField(max_length=10, unique=True,null=False, blank=False)
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
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    password = models.CharField(max_length=128, default='default_password_value')
    objects = UsuarioManager()

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'correo', 'direccion', 'telefono', 'tipo_usuario']

    def __str__(self):
        return self.rut

class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

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
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    tipo_inmueble_choices = (
        ('casa', 'Casa'),
        ('departamento','Departamento'),
        ('parcela','Parcela'),
    )
    tipo_inmueble = models.CharField(max_length=20, choices = tipo_inmueble_choices)
    precio_arriendo_mensual = models.IntegerField( null=False, blank=False)

