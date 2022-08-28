from django.db import models

class Unidad(models.Model):
    nombre = models.CharField("Nombre", blank=False, null=False, max_length=50, unique=True, db_index=True)
    nombre_abreviado = models.CharField("Nombre abreviado", null=False, blank=False, max_length=5, unique=True)

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"

    def __str__(self) -> str:
        return f"{self.nombre} - {self.nombre_abreviado}"

class MateriaPrima(models.Model):
    nombre = models.CharField("Nombre", blank=False, null=False, max_length=150, unique=True)
    unidad = models.ForeignKey(Unidad, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Materia Prima"
        verbose_name_plural = "Materias Primas"
    
    def __str__(self) -> str:
        return self.nombre
    
    @property
    def unidad_abreviada(self):
        return self.unidad.nombre_abreviado