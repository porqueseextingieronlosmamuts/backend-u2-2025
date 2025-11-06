from django.urls import include, path
from . import views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)


urlpatterns = [
    path("",views.lista_visitas, name="lista_visitas"),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("visitas/<int:id>/", views.detalle_visita, name="detalle_visita"),
    path("nueva_visita/", views.nueva_visita, name="nueva_visita"),
    path("editar_visita/<int:id>/", views.editar_visita, name="editar_visita"),
    path("eliminar_visita/<int:id>/", views.eliminar_visita, name="eliminar_visita"),
]
