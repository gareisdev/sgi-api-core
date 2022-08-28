from rest_framework import routers
from proveedores.api.viewsets import ProveedorViewSet

router = routers.DefaultRouter()

router.register("", ProveedorViewSet, basename="proveedores")

urlpatterns = router.urls
