from django.contrib import admin
from .models import Visita 

# Register your models here.
@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
 list_display = ('nombre', 'rut', 'motivo_de_visita', 'hora_de_entrada_y_salida')
 search_fields = ("nombre", "rut") # texto rápido
 list_filter = ("hora_de_entrada_y_salida",) # filtros laterales
 ordering = ("nombre",)
 list_per_page = 25

