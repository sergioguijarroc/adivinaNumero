from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request, "guess/home.html")


def guess(request):
    numeroRandom = random.randint(1, 10)
    respuestaUsuario = int(request.POST["numero"])
    message = "Respuesta errónea"
    if numeroRandom == respuestaUsuario:
        message = "Has acertado!"
    elif respuestaUsuario > numeroRandom:
        message = "El número es más pequeño"
    elif respuestaUsuario < numeroRandom:
        message = "El número es más grande"
    return render(request, "guess/guess.html", {"message": message})
