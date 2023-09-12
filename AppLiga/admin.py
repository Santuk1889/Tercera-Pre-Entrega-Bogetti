from django.contrib import admin
from .models import Liga, Equipo, Jugador

# Registro las clases para que se muestren en columnas en el admin


class LigaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "division"]


class EquipoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "liga"]


class JugadorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "posicion", "edad", "equipo"]
    search_fields = ["nombre", "posicion", "edad", "equipo"]
    list_filter = ["nombre", "posicion", "edad", "equipo"]


# Register your models here.

admin.site.register(Liga, LigaAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
