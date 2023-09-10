from django.shortcuts import render

# Create your views here.


def inicio(req):
    return render(req, "inicio.html")


def ligas(req):
    return render(req, "ligas.html")


def equipos(req):
    return render(req, "equipos.html")


def jugadores(req):
    return render(req, "jugadores.html")


def contacto(req):
    return render(req, "contacto.html")
