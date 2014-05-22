from django.db import models

# Create your models here.

class Departamento(models.Model):
	nombre = models.CharField(max_length=25)

	def __str__(self):
		return self.nombre

class Provincia(models.Model):
	departamento = models.ForeignKey(Departamento)
	nombre = models.CharField(max_length=25)

	def __str__(self):
		return self.nombre

class Distrito(models.Model):
	provincia = models.ForeignKey(Provincia)
	nombre = models.CharField(max_length=45)

	def __str__(self):
		return self.nombre

class Empresa(models.Model):
	distrito = models.ForeignKey(Distrito)
	rasonsocial = models.CharField(max_length=45)
	direccion = models.CharField(max_length=45)
	telefono = models.CharField(max_length=45)
	correo = models.EmailField(max_length=25)
	timestamp_first = models.DateTimeField(auto_now_add=True)
	timestamp_last = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.rasonsocial

class Local(models.Model):
	empresa = models.ForeignKey(Empresa)
	distrito = models.ForeignKey(Distrito)
	nombre = models.CharField(max_length=45, unique=True)
	direccion = models.CharField(max_length=45)
	telefono = models.CharField(max_length=45)
	fotoprincipal = models.ImageField(upload_to='fotos')
	foto2 = models.ImageField(upload_to='fotos')
	foto3 = models.ImageField(upload_to='fotos')
	servicios = models.TextField(max_length=140)
	calificacion = models.IntegerField(default=0)
	timestamp_first = models.DateTimeField(auto_now_add=True)
	timestamp_last = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nombre
