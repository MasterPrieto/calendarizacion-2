from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from settings import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'horarios.views.index'),
    url(r'registroaula$', 'horarios.views.registroaula'),
    url(r'registroprofesor$', 'horarios.views.registroprofesor'),
    url(r'registroprofesordiscapacidad$', 'horarios.views.registroprofesordiscapacidad'),
    url(r'registrogrupo$', 'horarios.views.registrogrupo'),
    url(r'registrogrupodiscapacidad$', 'horarios.views.registrogrupodiscapacidad'),
    url(r'registroasignatura$', 'horarios.views.registroasignatura'),
    url(r'registroasignacion$', 'horarios.views.registroasignacion'),
    url(r'registrocarrera$', 'horarios.views.registrocarrera'),
    url(r'registroinstituto$', 'horarios.views.registroinstituto'),
    url(r'registrodiscapacidad$', 'horarios.views.registrodiscapacidad'),
    url(r'registrorecurso$', 'horarios.views.registrorecurso'),
    url(r'registroespacio$', 'horarios.views.registroespacio'),
    url(r'registrotipoespacio$', 'horarios.views.registrotipoespacio'),
    url(r'registroespaciodiscapacidad$', 'horarios.views.registroespaciodiscapacidad'),
    url(r'registroespaciorecurso$', 'horarios.views.registroespaciorecurso'),
    url(r'registroasignaturarecurso$', 'horarios.views.registroasignaturarecurso'),
    url(r'registrohorariolaboral$', 'horarios.views.registrohorariolaboral'),
    url(r'editaraula/$', 'horarios.views.editaraula'),
    url(r'edicionaula/(?P<registroseleccionado>[0-9]+)/$', 'horarios.views.edicionaula'),
    url(r'editarprofesor/$', 'horarios.views.editarprofesor'),
    url(r'edicionprofesor/(?P<registroseleccionado>[0-9]+)/$', 'horarios.views.edicionprofesor'),
    url(r'editargrupo/$', 'horarios.views.editargrupo'),
    url(r'ediciongrupo/(?P<registroseleccionado>[0-9]+)/$', 'horarios.views.ediciongrupo'),
    url(r'editarasignatura/$', 'horarios.views.editarasignatura'),
    url(r'edicionasignatura/(?P<registroseleccionado>[0-9]+)/$', 'horarios.views.edicionasignatura'),



)

#staticpattern = STATIC_URL  + r'cosa(.*)$'
urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
#    (staticpattern, 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
)
