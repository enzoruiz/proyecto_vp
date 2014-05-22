from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	# url(r'^$', ),
	url(r'^fillprofile/$', 'apps.usuarios.views.profile', name='fill_profile'),
	url(r'^registro/$', 'apps.usuarios.views.registrarUsuario', name='registro'),

)
