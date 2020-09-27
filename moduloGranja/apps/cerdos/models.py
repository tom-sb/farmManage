from django.db import models
from apps.clusters.models import Cluster
from datetime import date
# Create your models here.
class Cerdo(models.Model):
    cluster = models.ForeignKey(Cluster,null=True,blank=True, on_delete=models.CASCADE)
    nombre_cerdo = models.CharField(max_length =25)
    raza = models.CharField(max_length =25)
    fecha_nac = models.DateField(default=date.today)
    peso = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre_cerdo
    def edad(self):
        return date.today().year-self.fecha_nac.year

    def reporte(self):
        edad = self.edad()
        if edad==0:
            edad=0.5
        medida = self.peso/edad
        if medida>10:
            return str('warning')
        elif medida<10:
            return str('danger')
        else:
            return str('success')

    def tipo(self):
        repH = Reproductora.objects.filter(cerdo=self)
        if repH :
            return self.reproductora
        repM = Reproductor.objects.filter(cerdo=self)
        if repM :
            return self.reproductor
        engorde = Engorde.objects.filter(cerdo=self)
        if engorde :
            return self.engorde
        nacido = Nacido.objects.filter(cerdo=self)
        if nacido :
            return self.nacido
        else:
            return 'indefinido'


    class Meta:
        abstract = False

class Reproductora(models.Model):
    cerdo = models.OneToOneField(Cerdo,on_delete=models.CASCADE,primary_key=True)
    nro_inseminaciones = models.PositiveIntegerField() 
    nro_partos = models.PositiveIntegerField() 
    fecha_gestacion = models.DateField(default=(date.today().month+8))
    embarazo = models.BooleanField(default = False)
    riesgo = models.BooleanField(default = False)
    def __str__(self):
        return 'Reproductora'

class Engorde(models.Model):
    cerdo = models.OneToOneField(Cerdo,on_delete=models.CASCADE,primary_key=True)
    apto = models.BooleanField()
    score = models.PositiveSmallIntegerField()
    def __str__(self):
        return 'Engorde'

class Reproductor(models.Model):
    cerdo = models.OneToOneField(Cerdo,on_delete=models.CASCADE,primary_key=True)
    nro_muestras = models.IntegerField()
    nro_hijos = models.PositiveIntegerField()
    def __str__(self):
        return 'Reproductor'

class Nacido(models.Model):
    cerdo = models.OneToOneField(Cerdo,on_delete=models.CASCADE,primary_key=True)
    apto = models.BooleanField()
    def __str__(self):
        return 'Nacido'

