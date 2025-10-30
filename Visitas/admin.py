from django.contrib import admin
from .models import Visita
from django.http import HttpResponse
import csv

# Register your models here.
@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
 list_display = ('nombre', 'rut', 'motivo_de_visita', 'hora_de_entrada_y_salida')
 search_fields = ("nombre", "rut") # texto rápido
 list_filter = ("hora_de_entrada_y_salida",) # filtros laterales
 ordering = ("nombre",)
 list_per_page = 25
 
 
@admin.action(description="Marcar salidas")
def marcar_salidas(modeladmin, request, queryset):
    updated = queryset.update(marcar_salidas=True)
    modeladmin.message_user(request, f"{updated} ventas anuladas.")
 




