from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Visita


class VisitaForm(forms.ModelForm):
    """Formulario para crear/editar Visita.

    Expone `fecha_de_salida` (opcional). Valida que la salida no sea anterior
    a la hora de entrada registrada en la instancia.
    """

    class Meta:
        model = Visita
        fields = ['nombre', 'rut', 'motivo_de_visita', 'fecha_de_salida']
        widgets = {
            # Usa input de tipo datetime-local para navegadores modernos
            'fecha_de_salida': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si la instancia ya tiene fecha_de_salida, ponerla en formato compatible con datetime-local
        if self.instance and getattr(self.instance, 'fecha_de_salida', None):
            self.initial.setdefault('fecha_de_salida', self.instance.fecha_de_salida.strftime('%Y-%m-%dT%H:%M'))

    def clean_fecha_de_salida(self):
        fecha = self.cleaned_data.get('fecha_de_salida')
        # Si la instancia existe y tiene hora de entrada, evitar que la salida sea anterior
        entrada = getattr(self.instance, 'hora_de_entrada_y_salida', None)
        if fecha and entrada and fecha < entrada:
            raise ValidationError('La fecha de salida no puede ser anterior a la fecha de entrada.')
        return fecha

    def save(self, commit=True):
        instance = super().save(commit=False)
        # La fecha_de_salida ya fue asignada por el campo del formulario.
        if commit:
            instance.save()
        return instance

