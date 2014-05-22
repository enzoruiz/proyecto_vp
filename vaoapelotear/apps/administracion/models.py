from django.db import models
from apps.busqueda.models import Local

# Create your models here.
class Cancha(models.Model):
	local = models.ForeignKey(Local)
	descripcion = models.CharField(max_length=7)
	timestamp_first = models.DateTimeField(auto_now_add=True)
	timestamp_last = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.local.nombre + ' - ' + self.descripcion

class Dia(models.Model):
	cancha = models.ForeignKey(Cancha)
	nombre = models.CharField(max_length=10)
	timestamp_first = models.DateTimeField(auto_now_add=True)
	timestamp_last = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.cancha.__str__() + ' - ' + self.nombre

class Periodo(models.Model):
	dia = models.ForeignKey(Dia)
	horainicio = models.CharField(max_length=5)
	horafin = models.CharField(max_length=5)
	precio = models.FloatField()
	timestamp_first = models.DateTimeField(auto_now_add=True)
	timestamp_last = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.dia.__str__() + ' - (' + self.horainicio + ' - ' + self.horafin + ')'

class Hora(models.Model):
	periodo = models.ForeignKey(Periodo)
	horaingreso = models.CharField(max_length=5)
	horasalida = models.CharField(max_length=5)
	timestamp_first = models.DateTimeField(auto_now_add=True)
	timestamp_last = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.periodo.__str__() + ' - (' + self.horaingreso + ' - ' + self.horasalida + ')'