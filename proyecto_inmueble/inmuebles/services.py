from .models import Inmueble, Usuario
from django.core.exceptions import ObjectDoesNotExist

def crear_usuario(nombre, apellido, rut, direccion, telefono,correo, tipo_usuario):
     """ 
    Crea un nuevo usuario en la base de datos.

    Args: 
        nombre (str): Nombres del usuario.
        apellido (str): Apellidos del usuario.
        rut (str): RUT del usuario.
        direccion (str): Dirección del usuario.
        telefono (int): Número de teléfono del usuario.
        correo (str): Correo electrónico del usuario.
        tipo_usuario (str): Tipo de usuario (arrendatario o arrendador).
        
    Returns:
        Usuario: Objeto de usuario recién creado.
    """
    usuario = Usuario.objects.create(nombre=nombre, apellido=apellido, rut=rut, direccion=direccion, telefono=telefono, correo=correo, tipo_usuario=tipo_usuario)
    return usuario

def obtener_usuario(rut):
    """
    Obtiene un usuario de la base de datos 

    Args:
        rut(str): El rut del usuario que queremos obtener 

    Returns:
        usuario: objeto Usuario correspondiente al rut que proporcionamos    
    """
    try:
        usuario = Usuario.objects.get(rut=rut)
        return usuario
    except ObjectDoesNotExist:
        return None


def editar_usuario(rut, nombre=None, apellido=None, direccion=None, telefono=None, correo=None, tipo_usuario=None):
    """
    Edita los datos de un usuario en la base de datos.
    (Se coloca none porque los datos son opcionales)

    Args:
        rut (str): El rut del usuario que queremos editar.
        nombre (str): Nuevo nombre del usuario (opcional).
        apellido (str): Nuevo apellido del usuario (opcional).
        direccion (str): Nueva dirección del usuario (opcional).
        telefono (int): Nuevo número de teléfono del usuario (opcional).
        correo (str): Nuevo correo electrónico del usuario (opcional).
        tipo_usuario (str): Nuevo tipo de usuario del usuario (opcional).

    Returns:
        bool: True si el usuario se editó correctamente, False si no se encontró el usuario.
    """
    try:
        usuario = Usuario.objects.get(rut=rut)
        if nombre:
            usuario.nombre = nombre
        if apellido:
            usuario.apellido = apellido
        if direccion:
            usuario.direccion = direccion
        if telefono:
            usuario.telefono = telefono
        if correo:
            usuario.correo = correo
        if tipo_usuario:
            usuario.tipo_usuario = tipo_usuario
        usuario.save()
        return True
    except ObjectDoesNotExist:
        return False

def eliminar_usuario(rut):
    """
    Elimina un usuario de la base de datos.

    Args:
        rut (str): El rut del usuario que queremos eliminar.

    Returns:
        bool: True si el usuario se eliminó correctamente, False si no se encontró el usuario.
    """ 
    try:
        usuario = Usuario.objects.get(rut=rut)
        usuario.delete()
        return True
    except ObjectDoesNotExist:
        return False