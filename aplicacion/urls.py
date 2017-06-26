from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.lista_encuesta),
	#url(r'^login/home$', views.lista_encuesta),
	url(r'^login/$', views.login),
    url(r'^encuesta/(?P<pk>[0-9]+)/$', views.detalle_encuesta),
    url(r'^encuesta/new/$', views.nueva_encuesta, name='nueva_encuesta'),
]