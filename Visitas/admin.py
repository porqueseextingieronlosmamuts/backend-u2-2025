from django.contrib import admin
from django.utils import timezone
from .models import Visita


@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'rut', 'motivo_de_visita', 'hora_de_entrada_y_salida', 'fecha_de_salida')
	search_fields = ("nombre", "rut")  # texto rápido
	list_filter = ("hora_de_entrada_y_salida", "fecha_de_salida")  # filtros laterales
	ordering = ("nombre",)
	list_per_page = 25
	actions = ['marcar_salida']

	@admin.action(description="Marcar salida para las visitas seleccionadas que no tengan salida")
	def marcar_salida(self, request, queryset):
		pendientes = queryset.filter(fecha_de_salida__isnull=True)
		updated = pendientes.update(fecha_de_salida=timezone.now())
		self.message_user(request, f"{updated} visita(s) marcadas como salida.")
 
 



 




