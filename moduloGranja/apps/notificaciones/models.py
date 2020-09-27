from django.db import models

# Create your models here.
class Notificacion(models.Model):
	mensaje = models.CharField(max_length=50)
	prioridad = models.BooleanField()

	def __str__(self):
		return self.mensaje
