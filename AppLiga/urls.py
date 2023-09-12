from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("ligas/", ligas, name="Ligas"),
    path("listaLigas/", listarLigas, name="listarLigas"),
    path("equipos/", equipos, name="Equipos"),
    path("jugadores/", jugadores, name="Jugadores"),
    path("ligasFormulario/", ligasFormulario, name="LigasFormulario"),
    path("equiposFormulario/", equiposFormulario, name="EquiposFormulario"),
    path("jugadoresFormulario/", jugadoresFormulario, name="JugadoresFormulario"),
    path("busquedaPosicion/", busquedaPosicion, name="busquedaPosicion"),
    path("buscarPosicion/", buscarPosicion, name="buscarPosicion"),
    path("busquedaLiga/", busquedaLiga, name="busquedaLiga"),
    path("buscarLiga/", buscarLiga, name="buscarLiga"),
]
