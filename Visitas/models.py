from django.db import models

# Create your models here.
from datetime import timedelta

class Visita(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    motivo_de_visita = models.TextField()
    hora_de_entrada_y_salida = models.DateTimeField(auto_now_add=True)

    @property
    def hora_entrada_y_salida_str(self):
        entrada = self.hora_de_entrada_y_salida
        salida = entrada + timedelta(hours=2) if entrada else None
        if entrada and salida:
            return f"{entrada.strftime('%Y-%m-%d %H:%M:%S')} - {salida.strftime('%Y-%m-%d %H:%M:%S')}"
        return ""