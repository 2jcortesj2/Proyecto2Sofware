from django.db import models

class Laboratorista(models.Model):
    codigo_interno = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    especialidad = models.CharField(max_length=100)

    class Meta:
        db_table = 'laboratorista'

    def __str__(self):
        return f"{self.nombre} - {self.titulo}"