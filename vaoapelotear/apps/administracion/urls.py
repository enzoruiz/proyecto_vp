from django.conf.urls import patterns, include, url
from .views import HomeLocalView, HomeEmpresaView, EmpresaPeriodosView

urlpatterns = patterns('',

	url(r'^local/$', HomeLocalView.as_view(), name='homeLocal'),
	url(r'^empresa/$', HomeEmpresaView.as_view(), name='homeEmpresa'),
	url(r'^empresa/periodos/$', EmpresaPeriodosView.as_view(), name='empresaPeriodos'),

)
