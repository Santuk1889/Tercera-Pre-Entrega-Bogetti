from django.urls import path

from AppLiga import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("ligas/", views.ligas, name="ligas"),
    path("equipos/", views.equipos, name="equipos"),
    path("jugadores/", views.jugadores, name="jugadores"),
    path("contacto/", views.contacto, name="contacto"),
]
