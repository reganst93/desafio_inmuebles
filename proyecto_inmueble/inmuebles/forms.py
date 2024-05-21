from django import forms
from .models import Usuario

class UsuarioCreationForm(forms.ModelForm):
    """
    Formulario para la creación de nuevos usuarios. Incluye campos adicionales
    para la contraseña y su confirmación.
    """
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        """
        Metadatos para el formulario que indican qué modelo usar y qué campos incluir.
        """
        model = Usuario
        fields = ['nombre', 'apellido', 'rut', 'direccion', 'telefono', 'correo', 'tipo_usuario']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre aquí'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Ingresa tu apellido aquí'}),
            'rut': forms.TextInput(attrs={'placeholder': 'Ingresa tu RUT aquí sin punto con guion'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ingresa tu dirección aquí'}),
            'telefono': forms.NumberInput(attrs={'placeholder': 'Ingresa tu teléfono aquí'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ingresa tu correo aquí'}),
            'tipo_usuario': forms.Select(attrs={'placeholder': 'Selecciona tu tipo de usuario'}),
        }

    def clean_password2(self):
        """
        Verifica que las dos contraseñas ingresadas coincidan.
        Lanza un ValidationError si no coinciden.
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        """
        Guarda el usuario con la contraseña encriptada.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UsuarioLoginForm(forms.Form):
    """
    Formulario para la autenticación de usuarios. Incluye campos para el RUT
    y la contraseña.
    """

    rut = forms.CharField(label='RUT')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'rut', 'direccion', 'telefono', 'correo', 'tipo_usuario']