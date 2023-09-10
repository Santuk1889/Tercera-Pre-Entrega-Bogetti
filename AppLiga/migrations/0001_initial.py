# Generated by Django 4.2.4 on 2023-09-10 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="equipos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=40)),
                ("division", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="jugadores",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=40)),
                ("posicion", models.CharField(max_length=40)),
                ("numero", models.IntegerField()),
                ("edad", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ligas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=40)),
                ("division", models.IntegerField()),
            ],
        ),
    ]
