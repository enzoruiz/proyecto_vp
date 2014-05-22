from django.db import models
from django.contrib.auth.models import User
from apps.busqueda.models import Empresa, Local

# Create your models here.

class Perfil(models.Model):
	usuario = models.OneToOneField(User)
	tipo = models.CharField(max_length=15, default='Usuario')
	empresa = models.OneToOneField(Empresa, null=True, blank=True)
	local = models.OneToOneField(Local, null=True, blank=True)
	dni = models.CharField(max_length=8, null=True)
	celular = models.CharField(max_length=15)

	def __str__(self):
		return '%s perfil' % self.usuario.username