from django.db import models
from apps.personal.models import Personal

# Create your models here.
class Cluster(models.Model):
        personal = models.ManyToManyField(Personal)
        nombre_cluster = models.CharField(max_length = 50)
        capacidad = models.PositiveIntegerField(default=20)
        nro_cerdos = models.PositiveIntegerField(default=0)
        nro_galpon = models.PositiveIntegerField(default=0)     

        def __str__(self):
                return self.nombre_cluster
