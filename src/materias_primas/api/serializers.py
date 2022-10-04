from materias_primas.models import MateriaPrima, Unidad
from rest_framework import serializers


class MateriaPrimaSerializer(serializers.ModelSerializer):
    unidad_abreviada = serializers.ReadOnlyField()

    class Meta:
        model = MateriaPrima
        fields = serializers.ALL_FIELDS


class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = serializers.ALL_FIELDS
