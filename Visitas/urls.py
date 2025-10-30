from django.urls import path
from . import views
urlpatterns = [
    path("",views.lista_visitas, name="lista_visitas"),
    path("visitas/<int:id>/", views.detalle_visita, name="detalle_visita"),
    path("nueva_visita/", views.nueva_visita, name="nueva_visita"),
    path("editar_visita/<int:id>/", views.editar_visita, name="editar_visita"),
    path("eliminar_visita/<int:id>/", views.eliminar_visita, name="eliminar_visita"),
]
