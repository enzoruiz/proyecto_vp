from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from django.core import serializers
from apps.busqueda.models import Departamento, Provincia, Distrito, Local
from apps.usuarios.models import Perfil
from apps.administracion.models import Cancha
from django.core.urlresolvers import reverse_lazy
import json

# Create your views here.

def checkuser(request):
	if request.method == 'GET':
		user = request.user
		perfil = Perfil.objects.get(usuario_id=user.id)
		tipo = perfil.tipo
		local = perfil.local
		empresa = perfil.empresa
		
		if tipo == 'Local':
			return redirect('../administracion/local/')
		elif tipo == 'Empresa':
			return redirect('../administracion/empresa/')
		elif tipo == 'Usuario':
			return redirect('../')

class GetDepartamentosView(TemplateView):
	def post(self, request, *args, **kwargs):
		departamentos = Departamento.objects.all()
		data = serializers.serialize('json', departamentos, fields=('nombre',))
		return HttpResponse(data, mimetype='application/json')

class GetProvinciasView(TemplateView):
	def post(self, request, *args, **kwargs):
		iddep = request.POST['iddepartamento']
		provincias = Provincia.objects.filter(departamento__id = iddep)
		data = serializers.serialize('json', provincias, fields=('nombre',))
		return HttpResponse(data, mimetype='application/json')

class GetDistritosView(TemplateView):
	def post(self, request, *args, **kwargs):
		idpro = request.POST['idprovincia']
		distritos = Distrito.objects.filter(provincia__id = idpro)
		data = serializers.serialize('json', distritos, fields=('nombre',))
		return HttpResponse(data, mimetype='application/json')

class GetCanchasView(TemplateView):
	def post(self, request, *args, **kwargs):
		idlocal = request.POST['idlocal']
		canchas = Cancha.objects.filter(local__id = idlocal)
		data = serializers.serialize('json', canchas, fields=('descripcion',))
		return HttpResponse(data, mimetype='application/json')

class SearchCanchaView(TemplateView):
	def get(self, request, *args, **kwargs):
		results = Local.objects.all()
		result_list = []
		for item in results:
			diccionario = {}
			diccionario['nombre'] = item.nombre + '  (' + item.distrito.provincia.nombre + ' - ' + item.distrito.nombre + ')'
			result_list.append(diccionario)

		response_text = json.dumps(result_list, separators=(',',':'))
		return HttpResponse(response_text, content_type="application/json")