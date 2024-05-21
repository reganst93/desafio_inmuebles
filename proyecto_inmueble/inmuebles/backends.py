from django.contrib.auth.backends import BaseBackend
from .models import Usuario

class UsuarioBackend(BaseBackend):
    def authenticate(self, request, rut=None, password=None):
        """
        Autentica un usuario basado en el RUT y la contraseña.

        Args:
            request: Objeto de la solicitud HTTP.
            rut: El RUT ingresado por el usuario.
            password: La contraseña ingresada por el usuario.

        Returns:
            Usuario: El usuario autenticado si las credenciales son correctas.
            None: Si las credenciales son incorrectas o el usuario no existe.
        """
        try:
            user = Usuario.objects.get(rut=rut)
            if user.check_password(password):
                return user
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Obtiene un usuario basado en su ID.

        Args:
            user_id: El ID del usuario.

        Returns:
            Usuario: El usuario con el ID dado.
            None: Si el usuario no existe.
        """
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None