from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import date
from .models import Local
from apps.administracion.models import Cancha, Periodo

# Create your views here.
class CanchaNombreView(TemplateView):
	def post(self, request, *args, **kwargs):
		nombre = request.POST.get('txtBusquedaCancha')
		fecha = request.POST.get('dpcalendario')
		hora = request.POST.get('cboHoraCancha')
		
		pos = nombre.find('  ')
		nombre = nombre[:pos].upper()

		dia = int(fecha[0:2])
		mes = int(fecha[3:5])
		anio = int(fecha[6:10])
		nroDia = date(anio, mes, dia).weekday()

		listaDias = {0 : 'Lunes', 1 : 'Martes', 2 : 'Miercoles', 3 : 'Jueves', 4 : 'Viernes', 5 : 'Sabado', 6 : 'Domingo'}
		nombreDia = listaDias[nroDia]

		horaIngreso = hora[0:5]

		# local = Local.objects.get(nombre=nombre, cancha__dia__periodo__hora__horaingreso=horaIngreso, cancha__dia__nombre=nombreDia)
		local = Local.objects.get(nombre=nombre)
		listaCalif = {0 : '', 1 : 'x', 2 :'xx', 3 : 'xxx', 4 : 'xxxx', 5 : 'xxxxx'}
		trofeoDorado = listaCalif[local.calificacion]
		trofeoGris = listaCalif[5 - local.calificacion]

		canchas = Cancha.objects.filter(local=local, dia__periodo__hora__horaingreso=horaIngreso, dia__nombre=nombreDia)
		periodos = Periodo.objects.filter(dia__cancha__local=local, hora__horaingreso=horaIngreso, dia__nombre=nombreDia)

		return render(request, 'busqueda/canchanombre.html', {"local": local, "periodos": periodos, "dorados": trofeoDorado, "grises": trofeoGris})
