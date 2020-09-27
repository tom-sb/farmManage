from django.db import models

# Create your models here.
class Personal(models.Model):
	nombre_personal = models.CharField(max_length=25)
	dni = models.IntegerField()
	vencimiento_carnet = models.DateField()

	def __str__(self):
		return self.nombre_personal
