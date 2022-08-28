from django.db import models

class Proveedor(models.Model):

    razon_social = models.CharField("Razon Social", blank=False, null=False, max_length=300)
    cuil_cuit = models.IntegerField("CUIL/CUIT", blank=False, null=False, db_index=True)
    direccion = models.CharField("Direccion", blank=False, null=False, max_length=150)
    cbu = models.CharField("CBU/CVU", blank=False, null=False, max_length=20)
    horario_retiro = models.TimeField("Horario de retiro")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ["razon_social"]

    def __str__(self) -> str:
        return f"{self.razon_social}"