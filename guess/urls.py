from django.urls import path
from . import views

urlpatterns = [
    path("", views.guess, name="home"),
    path("guess/", views.guess, name="guess"),
]
