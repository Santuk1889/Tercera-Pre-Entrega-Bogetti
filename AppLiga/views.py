from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Liga, Equipo, Jugador
from .forms import LigaFormulario, EquipoFormulario, JugadorFormulario


# Create your views here.
def liga(req, nombre, division):
    liga = Liga(nombre=nombre, division=division)
    liga.save()
    return HttpResponse(
        f"""<p>Liga: {liga.nombre} - División: {liga.division} fue creado exitosamente.</p>"""
    )


def listarLigas(req):
    lista = Liga.objects.all()
    return render(req, "listaLigas.html", {"listarLigas": lista})


def inicio(req):
    return render(req, "inicio.html")


def ligas(req):
    return render(req, "ligas.html")


def equipos(req):
    return render(req, "equipos.html")


def jugadores(req):
    return render(req, "jugadores.html")


def ligasFormulario(req):
    if req.method == "POST":
        miFormulario = LigaFormulario(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            liga = Liga(nombre=data["nombre"], division=data["division"])
            liga.save()

            return render(req, "inicio.html")
    else:
        miFormulario = LigaFormulario()
        return render(req, "ligasFormulario.html", {"miFormulario": miFormulario})


def equiposFormulario(req):
    if req.method == "POST":
        miFormulario = EquipoFormulario(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            equipo = Equipo(nombre=data["nombre"], liga=data["liga"])
            equipo.save()

            return render(req, "inicio.html")
    else:
        miFormulario = EquipoFormulario()
        return render(req, "equiposFormulario.html", {"miFormulario": miFormulario})


def jugadoresFormulario(req):
    if req.method == "POST":
        miFormulario = JugadorFormulario(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            jugador = Jugador(
                nombre=data["nombre"],
                posicion=data["posicion"],
                edad=data["edad"],
                equipo=data["equipo"],
            )
            jugador.save()

            return render(req, "inicio.html")
    else:
        miFormulario = JugadorFormulario()
        return render(req, "jugadoresFormulario.html", {"miFormulario": miFormulario})


def busquedaPosicion(req):
    return render(req, "busquedaPosicion.html")


def buscarPosicion(req: HttpRequest):
    if req.GET["posicion"]:
        posicion = req.GET["posicion"]
        jugadores = Jugador.objects.filter(posicion=posicion)
        return render(req, "ResultadobusquedaPosicion.html", {"jugadores": jugadores})
    return HttpResponse(
        f"Debe agregar una posición ( ejemplo: Arquero, Defensor, Volante, Delantero )"
    )


def busquedaLiga(req):
    return render(req, "busquedaLiga.html")


def buscarLiga(req: HttpRequest):
    if req.GET["liga"]:
        liga = req.GET["liga"]
        equipos = Equipo.objects.filter(liga__nombre__icontains=liga)
        return render(req, "ResultadobusquedaLiga.html", {"equipos": equipos})
    return HttpResponse(
        f"Debe agregar una liga ( ejemplo: Liga A, Liga B, Liga C, Liga D )"
    )
