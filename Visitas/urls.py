from django.urls import include, path
from . import views

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"visitas", views.VisitaViewSet)


urlpatterns = [
    path("",views.lista_visitas, name="lista_visitas"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    
    # Rutas JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path("visitas/<int:id>/", views.detalle_visita, name="detalle_visita"),
    path("nueva_visita/", views.nueva_visita, name="nueva_visita"),
    path("editar_visita/<int:id>/", views.editar_visita, name="editar_visita"),
    path("eliminar_visita/<int:id>/", views.eliminar_visita, name="eliminar_visita"),
]
