from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Encuesta

def lista_encuesta(request):
	encuestas = Encuesta.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
	return render(request, 'aplicacion/lista_encuesta.html', {'encuestas': encuestas})

def detalle_encuesta(request, pk):
    encuesta = get_object_or_404(Encuesta, pk=pk)
    return render(request, 'aplicacion/detalle_encuesta.html', {'encuesta': encuesta})
