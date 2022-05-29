from rest_framework.routers import DefaultRouter
from servicios.api.views.servicio_views import *
from servicios.api.views.horario_views import *

router=DefaultRouter()

router.register(r'servicio',ServicioViewSet, basename='servicio')
router.register(r'horario',HorarioViewSet, basename='horario')
urlpatterns=router.urls