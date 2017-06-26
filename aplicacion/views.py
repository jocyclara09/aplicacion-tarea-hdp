from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib.auth.models import User
from .models import Encuesta
from .forms import LoginForm
from .forms import EncuestaForm

def login(request):
	message  = None
	if request.method =="POST":
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate( username = username_post, password = password_post)
		if user is not None:
			login_django(request, user)
			return redirect('http://127.0.0.1:8000/')
			#return render(request, 'aplicacion/lista_encuesta.html', {})
		else:
			message = "El Username o Password es incorrecto"
	form = LoginForm()
	context = {
		'form' : form,
		'message' : message,
	}
	return render(request, 'aplicacion/login.html', context)

def lista_encuesta(request):
	encuestas = Encuesta.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
	return render(request, 'aplicacion/lista_encuesta.html', {'encuestas': encuestas})

def detalle_encuesta(request, pk):
    encuesta = get_object_or_404(Encuesta, pk=pk)
    return render(request, 'aplicacion/detalle_encuesta.html', {'encuesta': encuesta})

def nueva_encuesta(request):
    if request.method == "POST":
        form = EncuestaForm(request.POST)
        if form.is_valid():
            encuesta = form.save(commit=False)
            encuesta.autor = request.user
            encuesta.fecha_creacion = timezone.now()
            encuesta.save()
            #return redirect('detalle_encuesta', pk=encuesta.pk)
            return render(request, 'aplicacion/detalle_encuesta.html', {'encuesta': encuesta})
    else:
        form = EncuestaForm()
    return render(request, 'aplicacion/edicion_encuesta.html', {'form': form})
