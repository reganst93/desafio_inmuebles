from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

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
        User = get_user_model()
        try:
            user = User.objects.get(rut=rut)
            if user.check_password(password):
                # Set the backend attribute on the user
                user.backend = f'{user._meta.app_label}.{user._meta.model_name}'
                return user
        except User.DoesNotExist:
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
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
