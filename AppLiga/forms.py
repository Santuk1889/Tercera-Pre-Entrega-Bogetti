from django import forms
from .models import Liga, Equipo, Jugador


class LigaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    division = forms.IntegerField()


class EquipoFormulario(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ["nombre", "liga"]


class JugadorFormulario(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ["nombre", "posicion", "edad", "equipo"]
