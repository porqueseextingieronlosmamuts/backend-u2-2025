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
 
@admin.action(description="Exportar ventas a CSV")
def marcar_salida_csv(modeladmin, request, queryset):
 response = HttpResponse(content_type='text/csv')
 response['Content-Disposition'] = 'attachment; filename="visitas.csv"'
 writer = csv.writer(response)
 writer.writerow(["nombre", "rut", "motivo de visita", "hora de entrada y salida",])
 for v in queryset.select_related('visita').prefetch_related('lista_visitas'):
    writer.writerow([v.nombre, v.rut, v.motivo_de_visita, v.hora_de_entrada_y_salida,])
 return response
@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
 # ... (resto)
 actions = [marcar_salidas, marcar_salida_csv]



