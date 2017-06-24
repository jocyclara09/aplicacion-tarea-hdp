from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_encuesta),
    url(r'^encuesta/(?P<pk>[0-9]+)/$', views.detalle_encuesta),
]