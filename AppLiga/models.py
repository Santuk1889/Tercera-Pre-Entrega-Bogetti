from django.db import models

# Create your models here.


class Liga(models.Model):
    nombre = models.CharField(max_length=40)
    division = models.IntegerField()


class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)


class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    posicion = models.CharField(max_length=40)
    edad = models.IntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
