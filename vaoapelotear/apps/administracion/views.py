from django.shortcuts import render
from django.views.generic import TemplateView
from apps.usuarios.models import Perfil
from apps.busqueda.models import Local, Empresa
from .models import Cancha, Dia, Periodo, Hora
import datetime

# Create your views here.
class HomeLocalView(TemplateView):
	template_name = 'jaja.html'

class HomeEmpresaView(TemplateView):
	template_name = 'jaja.html'

class EmpresaPeriodosView(TemplateView):

	def validarCrucePeriodo(self, miDia, idCancha, horaInicio, horaFin):
		res = False
		canchas = Cancha.objects.raw('SELECT DISTINCT p.id FROM administracion_cancha c INNER JOIN administracion_dia d ON c.id = d.id INNER JOIN administracion_periodo p ON d.id = p.id INNER JOIN administracion_hora h ON p.id = h.id WHERE d.nombre = %s AND c.id = %s AND (((%s > p.horainicio AND %s < p.horafin) OR (%s > p.horainicio AND %s < p.horafin)) OR ((p.horainicio >= %s AND p.horainicio <= %s) OR (p.horafin >= %s AND p.horafin <= %s)))', [miDia, idCancha, horaInicio, horaInicio, horaFin, horaFin, horaInicio, horaFin, horaInicio, horaFin])
		cantidad = len(list(canchas))
		if cantidad > 0:
			res = True

		return res

	def get(self, request, *args, **kwargs):
		user = request.user
		locales = Local.objects.filter(empresa__perfil__usuario__id=user.id)
		valores = {}
		valores['locales'] = locales
		print(kwargs)
		valores.update(kwargs)
		return render(request, 'administracion/misperiodos.html', valores)

	def post(self, request, *args, **kwargs):
		dias = []
		if request.POST.get('chkLunes'):
			dias.append('Lunes')
		if request.POST.get('chkMartes'):
			dias.append('Martes')
		if request.POST.get('chkMiercoles'):
			dias.append('Miercoles')
		if request.POST.get('chkJueves'):
			dias.append('Jueves')
		if request.POST.get('chkViernes'):
			dias.append('Viernes')
		if request.POST.get('chkSabado'):
			dias.append('Sabado')
		if request.POST.get('chkDomingo'):
			dias.append('Domingo')

		horas = {1 : '07:00', 2 : '08:00', 3 : '09:00', 4 : '10:00', 5 : '11:00', 6 : '12:00', 7 : '13:00', 8 : '14:00', 9 : '15:00', 10 : '16:00', 11 : '17:00', 12 : '18:00', 13 : '19:00', 14 : '20:00', 15 : '21:00', 16 : '22:00', 17 : '23:00'}

		idCancha = request.POST.get('cboCancha')
		horaInicio = horas[int(request.POST.get('cboHoraInicio'))]
		horaFin = horas[int(request.POST.get('cboHoraFin'))]
		precio = request.POST.get('txtPrecioPeriodo')

		can = len(dias)
		i = 0
		secruza = False
		while i < can:
			miDia = dias[i]
			res = self.validarCrucePeriodo(miDia, idCancha, horaInicio, horaFin)
			if res == True:
				secruza = True
			i = i + 1
		
		if secruza == False:
			cancha = Cancha.objects.get(id=idCancha)
			j = 0
			while j < can:
				dia = Dia(cancha=cancha, nombre=dias[j])
				dia.save()
				per = Periodo(dia=dia, horainicio=horaInicio, horafin=horaFin, precio=precio)
				per.save()

				hi = datetime.datetime.strptime(horaInicio, "%H:%M")
				hf = datetime.datetime.strptime(horaFin, "%H:%M")

				while hi < hf:
					h = hi + datetime.timedelta(hours=1)
					hora = Hora(periodo=per, horaingreso=hi.strftime('%H:%M'), horasalida=h.strftime('%H:%M'))
					hora.save()
					hi = hi + datetime.timedelta(hours=1)
				j = j + 1

			return self.get(request, mensaje='Periodo registrado correctamente.')
		else:
			return self.get(request, errorValidar='El periodo ingresado se cruza con uno ya creado.')