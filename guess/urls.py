from django.urls import path
from . import views  # Tenemos que importar las vistas que están enlazadas a las urls.

urlpatterns = [
    path(
        "", views.home, name="home"
    ),  # Con la url por defecto (127.0.0.1) nos lleva a esta vista (home), le he puesto el nombre name para usarlo más adelante
    path("guess/", views.guess, name="guess"),
]
