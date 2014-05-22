from django.conf.urls import patterns, include, url
from .views import GetProvinciasView, GetDistritosView, SearchCanchaView, GetDepartamentosView, GetCanchasView

urlpatterns = patterns('',

	url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name' : 'index.html'}, name='loginHome'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name' : 'home/login.html'}, name='login'),
    url(r'^checkuser/$', 'apps.home.views.checkuser', name='checkuser'),
    
    url(r'^damedepartamentos/$', GetDepartamentosView.as_view(), name='damedepartamentos'),
    url(r'^dameprovincias/$', GetProvinciasView.as_view(), name='dameprovincias'),
    url(r'^damedistritos/$', GetDistritosView.as_view(), name='damedistritos'),
    url(r'^damecanchas/$', GetCanchasView.as_view(), name='damecanchas'),
    url(r'^search-cancha/$', SearchCanchaView.as_view(), name='search-cancha'),

)
