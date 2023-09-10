from django.db import models

# Create your models here.


class ligas(models.Model):
    nombre = models.CharField(max_length=40)
    division = models.IntegerField()


class equipos(models.Model):
    nombre = models.CharField(max_length=40)
    division = models.IntegerField()


class jugadores(models.Model):
    nombre = models.CharField(max_length=40)
    posicion = models.CharField(max_length=40)
    numero = models.IntegerField()
    edad = models.IntegerField()
