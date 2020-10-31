from django.db import models
#from apps.clusters.models import Cluster
from datetime import date
# Create your models here.

class Raza(models.Model):
    nombre = models.CharField(max_length=25,primary_key=True)
    edad_ideal = models.PositiveIntegerField()
    peso_ideal = models.PositiveIntegerField()

    class Meta:
        abstract=False
    def peso_promedio(self):
        return self.peso_ideal/self.edad_ideal

    def __str__(self):
        return self.nombre


class Cerdo(models.Model):
    GEN = (('M','Macho'), ('H','Hembra'))
    nombre = models.CharField(verbose_name="nombre_cerdo",primary_key=True,unique=True,max_length =25)
    raza = models.ForeignKey(Raza,on_delete=models.CASCADE)
    genero = models.CharField(verbose_name="genero",choices=GEN,max_length=10)
    peso = models.PositiveSmallIntegerField()
    fecha_nacimiento = models.DateField(default=date.today)

    def __str__(self):
        return self.nombre
    def edad(self):
        return date.today().year-self.fecha_nacimiento.year
    def viabilidad(self):
        raza = Raza.objects.get(pk=self.raza)
        
        edad = self.edad()
        if edad==0: edad=1
        pr = (raza.peso_promedio()*edad)
        probabilidad = self.peso/pr
        return probabilidad

    def reporte(self):
        prob = self.viabilidad() 
        if 0.85 < prob < 1.1:
            return str('success')
        elif prob <= 0.85:
            return str('danger')
        else:
            return str('warning')
    def tipo(self):
        rol = cerdoRol.objects.get(cerdo=self.pk)
        return rol
    def cluster(self):
        return 1

    #class Meta:
    #    abstract = False

class cerdoRol(models.Model):
    tipo = (
            ('Reproductora','Reproductora'),
            ('Reproductor','Reproductor'),
            ('Engorde','Engorde'),
            ('Nacido','Nacido'))
    cerdo = models.ForeignKey(Cerdo,on_delete=models.CASCADE)
    rol_nombre = models.CharField(max_length=12,choices = tipo)
    active = models.BooleanField(default=True)  

    def __str__(self):
        return self.rol_nombre
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

