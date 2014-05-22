from django.db import models
from django.contrib.auth.models import User
from apps.administracion.models import Cancha

# Create your models here.
class Alquiler(models.Model):
	usuario = models.ForeignKey(User)
	cancha = models.ForeignKey(Cancha)
	estadoalquiler = models.CharField(max_length=25)
	fecha = models.DateField()
	horaingreso = models.CharField(max_length=5)
	horasalida = models.CharField(max_length=5)
	estadohora = models.CharField(max_length=25)
	monto = models.FloatField()
	timestamp_first = models.DateTimeField(auto_now_add=True)
	timestamp_last = models.DateTimeField(auto_now=True)