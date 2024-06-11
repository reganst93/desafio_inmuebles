"""
URL configuration for proyecto_inmueble project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inmuebles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('agregar_inmueble/', views.agregar_inmueble, name='agregar_inmueble'),
    path('editar_inmueble/<int:inmueble_id>/', views.editar_inmueble, name='editar_inmueble'),
    path('borrar_inmueble/<int:inmueble_id>/', views.borrar_inmueble, name='borrar_inmueble'),
    path('lista_inmuebles/', views.lista_inmuebles, name='lista_inmuebles'),
]
