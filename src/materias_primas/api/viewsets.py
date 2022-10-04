from materias_primas.api.serializers import MateriaPrimaSerializer, UnidadSerializer
from rest_framework import viewsets


class MateriaPrimaViewSet(viewsets.ModelViewSet):
    serializer_class = MateriaPrimaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()


class UnidadViewSet(viewsets.ModelViewSet):
    serializer_class = UnidadSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()
