from rest_framework import viewsets
from proveedores.api.serializers import ProveedorSerializer
from proveedores.models import Proveedor

class ProveedorViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.all()
