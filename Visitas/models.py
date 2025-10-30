from django.db import models
from datetime import timedelta


class Visita(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    motivo_de_visita = models.TextField()
    hora_de_entrada_y_salida = models.DateTimeField(auto_now_add=True)
    # Nuevo campo para registrar la hora de salida cuando se marque desde el admin
    fecha_de_salida = models.DateTimeField(null=True, blank=True)

    @property
    def hora_entrada_y_salida_str(self):
        entrada = self.hora_de_entrada_y_salida
        # Si existe fecha_de_salida en la base, la usamos; si no, calculamos entrada + 2h como valor por defecto
        salida = self.fecha_de_salida if self.fecha_de_salida else (entrada + timedelta(hours=2) if entrada else None)
        if entrada and salida:
            return f"{entrada.strftime('%Y-%m-%d %H:%M:%S')} - {salida.strftime('%Y-%m-%d %H:%M:%S')}"
        return ""