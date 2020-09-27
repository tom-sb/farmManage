from django.db import models
from apps.clusters.models import Cluster
from datetime import date

# Create your models here.
class Alimento(models.Model):
	nombre_alimento = models.CharField(max_length = 50)
	stock_alimento = models.IntegerField()

	def __str__(self):
		return self.nombre_alimento
	
	def updateStock(self, val):
		self.stock_alimento = self.stock_alimento + val

	

class FichaAlimento(models.Model):
	nombre_ficha = models.CharField(max_length = 50)
	alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
	cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
	fecha_expiracion = models.DateField(default = (date.today))
	frecuencia_xdia = models.PositiveSmallIntegerField()
	cantidad_xtoma = models.PositiveSmallIntegerField()
	auto_renovar = models.BooleanField(default = False)

	def __str__(self):
		return self.nombre_ficha
