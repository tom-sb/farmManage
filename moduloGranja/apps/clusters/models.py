from django.db import models
from apps.personal.models import Personal
from apps.cerdos.models import Cerdo

# Create your models here.
class Cluster(models.Model):
        personal = models.ManyToManyField(Personal)
        nombre = models.CharField(max_length=15)
        capacidad = models.PositiveIntegerField(default=20)
        nro_cerdos = models.PositiveIntegerField(default=0)
        nro_galpon = models.PositiveIntegerField(default=0,primary_key=True)
        fecha = models.DateField(auto_now_add=True)

        def __str__(self):
                return self.nombre

class CerdoCluster(models.Model):
    cerdo = models.ForeignKey(Cerdo,on_delete=models.CASCADE)
    galpon = models.ForeignKey(Cluster,on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.cerdo.nombre+'->'+self.galpon.nombre

