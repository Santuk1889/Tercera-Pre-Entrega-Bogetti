from django.contrib import admin
from .models import Liga, Equipo, Jugador

# Register your models here.

admin.site.register(Liga)
admin.site.register(Equipo)
admin.site.register(Jugador)


class LigaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "division")


class EquipoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "liga")


class JugadorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "posicion", "edad", "equipo")
