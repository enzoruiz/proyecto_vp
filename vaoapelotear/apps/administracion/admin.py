from django.contrib import admin
from .models import Cancha, Dia, Periodo, Hora

# Register your models here.
admin.site.register(Cancha)
admin.site.register(Dia)
admin.site.register(Periodo)
admin.site.register(Hora)