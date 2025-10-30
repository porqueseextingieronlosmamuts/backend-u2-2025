from django import forms
from .models import Visita
class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ['nombre', 'rut', 'motivo_de_visita',]

def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data['hora_de_entrada'] and self.cleaned_data['hora_de_salida']:
            instance.hora_de_entrada_y_salida = f"{self.cleaned_data['hora_de_entrada']} - {self.cleaned_data['hora_de_salida']}"
        if commit:
            instance.save()
        return instance

