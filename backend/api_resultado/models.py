from django.db import models
from api_paciente.models import Paciente
from api_laboratorista.models import Laboratorista

class ResultadoPerfilLipidico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='paciente_id')
    laboratorista = models.ForeignKey(Laboratorista, on_delete=models.CASCADE, db_column='laboratorista_id')
    colesterol_total = models.FloatField()
    colesterol_hdl = models.FloatField()
    colesterol_ldl = models.FloatField()
    trigliceridos = models.FloatField()
    fecha_analisis = models.DateField()
    observaciones = models.TextField()

    class Meta:
        db_table = 'resultado_perfil_lipidico'

    def __str__(self):
        return f"Resultado {self.id} - Paciente: {self.paciente.nombre}"