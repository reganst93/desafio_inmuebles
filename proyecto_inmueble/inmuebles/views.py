from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UsuarioCreationForm, UsuarioLoginForm, UsuarioUpdateForm
from .models import Usuario

def home(request):
    """
    Renderiza la pagina de inicio
    """
    return render(request, 'home.html')

def user_login(request):
    """
    Vista para manejar el inicio de sesión del usuario.

    Si la solicitud es POST, se valida el formulario de inicio de sesión.
    Si las credenciales son correctas, se autentica y se inicia sesión en el usuario,
    y se redirige al perfil del usuario.

    Si la solicitud no es POST, se muestra el formulario de inicio de sesión vacío.
    """
    if request.method == 'POST':
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data.get('rut')
            password = form.cleaned_data.get('password')
            user = authenticate(request, rut=rut, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = UsuarioLoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    """
    Vista para manejar el registro de nuevos usuarios.

    Si la solicitud es POST, se valida el formulario de creación de usuario.
    Si el formulario es válido, se guarda el nuevo usuario y se redirige a la página de inicio de sesión.

    Si la solicitud no es POST, se muestra el formulario de registro vacío.
    """
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UsuarioCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    """
    Vista para mostrar y actualizar el perfil de usuario.

    Si la solicitud es POST, se procesa el formulario de modificación de datos.
    Si el formulario es válido, se guardan los cambios y se redirige a la página de perfil actualizada.

    Si la solicitud no es POST, se muestra el formulario de modificación de datos con los datos actuales del usuario.
    """
    if request.method == 'POST':
        # Si la solicitud es POST, se crea una instancia del formulario
        # con los datos proporcionados por el usuario y la instancia
        # actual del usuario.
        form = UsuarioUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            # Si el formulario es válido, se guardan los cambios
            # y se redirige a la página de perfil actualizada.
            form.save()
            return redirect('profile')
    else:
        # Si la solicitud no es POST, se crea una instancia del formulario
        # con los datos actuales del usuario.
        form = UsuarioUpdateForm(instance=request.user)
    # Se renderiza la página de perfil con el formulario.
    return render(request, 'profile.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')