from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vaoapelotear.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('apps.home.urls')),
    url(r'^administracion/', include('apps.administracion.urls')),
    url(r'^busqueda/', include('apps.busqueda.urls')),
    url(r'^reservas/', include('apps.reservas.urls')),
    url(r'^usuarios/', include('apps.usuarios.urls')),
)
