from rest_framework.routers import DefaultRouter
from .viewsets import MateriaPrimaViewSet, UnidadViewSet

router = DefaultRouter()

router.register('materia-prima', MateriaPrimaViewSet, basename='materia_prima')
router.register('unidad', UnidadViewSet, basename='unidad')


urlpatterns = router.urls