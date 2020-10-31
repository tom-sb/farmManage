from django.db import models
from datetime import date

# Create your models here.
class Personal(models.Model):
        nombre = models.CharField(max_length=25)
        dni = models.IntegerField()
        fecha_salida = models.DateField(default=date.today)
        fecha_ingreso = models.DateField(default=date.today)
        def __str__(self):
                return self.nombre
