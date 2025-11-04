from django.db import models

class Paciente(models.Model):
    paciente_id = models.CharField(max_length=50, unique=True, primary_key=True)
    codigo_ingreso = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    insurance = models.CharField(max_length=100)  # EPS
    fecha_registro = models.DateField()

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"