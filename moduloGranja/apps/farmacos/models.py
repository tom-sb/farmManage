from django.db import models
from datetime import date
from apps.cerdos.models import Cerdo


# Create your models here.
class Vacuna(models.Model):
    nombre_vacuna = models.CharField(max_length =25)
    marca = models.CharField(max_length=25)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return  self.nombre_vacuna

class Vitamina(models.Model):
    nombre_vit = models.CharField(max_length =25)
    marca = models.CharField(max_length=25)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return  self.nombre_vit

class Medicina(models.Model):
    nombre_med = models.CharField(max_length =25)
    marca = models.CharField(max_length=25)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return  self.nombre_med
    
class FichaVet(models.Model):
    nombre_fichavet = models.CharField(max_length = 25)
    dias_tratamiento = models.PositiveSmallIntegerField()
    frecuencia_xdia = models.PositiveSmallIntegerField()
    dosis_xtoma = models.PositiveSmallIntegerField()
    fecha_inicio = models.DateField(default = date.today)
    cerdo = models.ForeignKey(Cerdo, on_delete=models.CASCADE)

    class Meta:
        abstract = True
    def __str__(self):
        return  self.nombre_fichavet

class FichaMedicina(FichaVet):
    medicina = models.ForeignKey(Medicina, on_delete=models.CASCADE)

class FichaVitamina(FichaVet):
    vitamina = models.ForeignKey(Vitamina, on_delete=models.CASCADE)

class FichaVacuna(FichaVet):
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)

