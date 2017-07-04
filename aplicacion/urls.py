from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^home/$', views.inicio),
	url(r'^encuesta/(?P<pk>[0-9]+)/$', views.detalle),
	url(r'^login/$', views.login),
	url(r'^logout/$', views.logout),
	url(r'^login/home/$', views.lista_encuesta),
    url(r'^login/encuesta/(?P<pk>[0-9]+)/$', views.detalle_encuesta),
    url(r'^login/encuesta/new/$', views.nueva_encuesta, name='nueva_encuesta'),
    url(r'^login/encuesta/pregunta/$', views.Preg.as_view()),
]