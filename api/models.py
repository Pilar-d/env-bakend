from django.db import models
from django.contrib.auth.models import User


class Programmer(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nickname} ({self.language})"


class Proyecto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Proyecto")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Tarea")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    completada = models.BooleanField(default=False, verbose_name="¿Completada?")
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="tareas")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.proyecto.nombre}"
