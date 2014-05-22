from django.conf.urls import patterns, include, url
from .views import CanchaNombreView

urlpatterns = patterns('',

	url(r'^canchanombre/$', CanchaNombreView.as_view(), name='canchanombre'),

)
