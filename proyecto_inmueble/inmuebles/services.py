from .models import Inmueble, Usuario, Comuna, Region
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

def consultar_inmuebles_comuna(nombre_documento):
    """
    Consulta y guarda en un archivo de texto el listado de inmuebles para arriendo
    separado por comunas, utilizando solo los campos "nombre" y "descripción".

    Args:
        nombre_documento (str): El nombre del archivo de texto donde se guardarán los resultados.

    Returns:
        bool: True si se completó la operación correctamente, False si ocurrió un error.
    """
    try:
        #abrir el archivo en modo escritura
        with open(nombre_documento, 'w') as archivo:
            #recorrer todos los inmuebles en la base de datos
            for inmueble in Inmueble.objects.all():
                #Escribir el nombre y la descripcion del inmueble
                archivo.write(f"Nombre:{inmueble.nombre}\n")
                archivo.write(f"Descripción:{inmueble.descripcion}\n")
        return True
    except Exception as e:
        print(f"Error al consultar y guardar inmuebles: {e}")
        return False


def consultar_inmuebles_regiones(inmuebles_regiones):
    """
    Consulta y guarda en un archivo de texto el listado de inmuebles para arriendo
    separado por regiones

    Args:
        inmuebles_regiones (str): El nombre del archivo de texto donde se guardarán los resultados.

    Returns:
        bool: True si se completó la operación correctamente, False si ocurrió un error.
    """
    try:
        with open(inmuebles_regiones, 'w') as archivo:
            # Obtener todas las regiones disponibles en la base de datos
            regiones = set(Comuna.objects.values_list('region__nombre', flat=True))
            for region in regiones:
                archivo.write(f'Región: {region}\n')
                
                # Consultar las comunas de la región actual
                comunas_region = Comuna.objects.filter(region__nombre=region)
                
                # Consultar los inmuebles disponibles para cada comuna de la región actual
                for comuna in comunas_region:
                    inmuebles_comuna = Inmueble.objects.filter(comuna=comuna)
                    for inmueble in inmuebles_comuna:
                        archivo.write(f'Inmueble: {inmueble.nombre}\n')
                
                # Separador entre regiones
                archivo.write('\n')
        return True
    except Exception as e:
        print(f"Error al consultar y guardar inmuebles por región: {e}")
        return False


                
