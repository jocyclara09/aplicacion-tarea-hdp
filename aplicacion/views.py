from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logut_django
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib.auth.models import User
from .models import Encuesta, Pregunta
from .forms import LoginForm
from .forms import EncuestaForm, PreguntaForm, RespuestaForm

def login(request):
	message  = None
	if request.method =="POST":
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate( username = username_post, password = password_post)
		if user is not None:
			login_django(request, user)
			return redirect('/login/home/')
			#return render(request, 'aplicacion/lista_encuesta.html', {})
		else:
			message = "El Username o Password es incorrecto"
	form = LoginForm()
	context = {
		'form' : form,
		'message' : message,
	}
	return render(request, 'aplicacion/login.html', context)

def logout(request):
	logut_django(request)
	return redirect('http://127.0.0.1:8000/')

def inicio(request):
	encuestas = Encuesta.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
	return render(request, 'aplicacion/inicio.html', {'encuestas': encuestas})

def detalle(request, pk):
    encuesta = get_object_or_404(Encuesta, pk=pk)
    return render(request, 'aplicacion/detalle.html', {'encuesta': encuesta})

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
            return redirect('http://127.0.0.1:8000/login/encuesta/pregunta/')
            #return render(request, 'aplicacion/detalle_encuesta.html', {'encuesta': encuesta})
    else:
        form = EncuestaForm()
    return render(request, 'aplicacion/edicion_encuesta.html', {'form': form})

class Preg(CreateView):
	model = Pregunta
	template_name = 'aplicacion/pregunta.html'
	form_class = RespuestaForm
	second_form_class = PreguntaForm
	success_url = reverse_lazy('/login/home/')

	def get_context_data(self, **kwargs):
		context = super(Preg, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] =self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.objects = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			respuesta = form.save(commit=False)
			respuesta.idP = form2.save()
			respuesta.save()
			return redirect('/login/home/')
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))
