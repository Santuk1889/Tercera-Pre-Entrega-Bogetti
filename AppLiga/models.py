from django.db import models

# Create your models here.


class Liga(models.Model):
    nombre = models.CharField(max_length=40)
    division = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.division}"


class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.liga} división"

    class Meta:
        ordering = ("nombre",)
        unique_together = ("nombre", "liga")


class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    posicion = models.CharField(max_length=40)
    edad = models.IntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.posicion} - {self.edad} años - {self.equipo}"

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
