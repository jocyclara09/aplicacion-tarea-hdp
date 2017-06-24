from django.shortcuts import render
from django.utils import timezone
from .models import Encuesta

def lista_encuesta(request):
	encuestas = Encuesta.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
	return render(request, 'aplicacion/lista_encuesta.html', {'encuestas': encuestas})
