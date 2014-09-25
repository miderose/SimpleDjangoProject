from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from MainApp.views import telefonini, persone, persona, index

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SimpleDjangoProject.views.home', name='home'),
    # url(r'^SimpleDjangoProject/', include('SimpleDjangoProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index),
    url(r'^telefonini/', telefonini),
    url(r'^persone/', persone),
    url(r'^persona/(?P<persona_id>[\d]+)/', persona),
)
