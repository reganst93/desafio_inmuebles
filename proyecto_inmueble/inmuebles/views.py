from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UsuarioCreationForm, UsuarioLoginForm, UsuarioUpdateForm, InmuebleForm, InmuebleUpdateForm
from .models import Usuario, Inmueble

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
            form.save()
            return redirect('login')
        else:
            print(form.errors)
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
        form = UsuarioUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UsuarioUpdateForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

def agregar_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = InmuebleForm()
    return render(request, 'agregar_inmueble.html', {'form': form})

def editar_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
    if request.method == 'POST':
        form = InmuebleUpdateForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('lista_inmuebles')
        else:
            print(form.errors)  
    else:
        form = InmuebleUpdateForm(instance=inmueble)
    return render(request, 'editar_inmueble.html', {'form': form})


def borrar_inmueble(request, inmueble_id):
    """
    Vista para borrar un inmueble existente.
    """
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    
    if request.method == 'POST':
        if 'confirmar' in request.POST:
            inmueble.delete()
            # Redirigir a la lista de inmuebles después de eliminar el inmueble
            return redirect('lista_inmuebles')
        elif 'cancelar' in request.POST:
            return redirect('home')  

    return render(request, 'borrar_inmueble.html', {'inmueble': inmueble})

def lista_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'lista_inmuebles.html', {'inmuebles': inmuebles})
