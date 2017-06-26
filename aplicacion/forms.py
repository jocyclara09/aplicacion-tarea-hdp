from django import forms

from .models import Encuesta, Pregunta, Respuesta

class LoginForm(forms.Form):
	username = forms.CharField(max_length=15)
	password = forms.CharField(max_length=10, widget= forms.PasswordInput())

class EncuestaForm(forms.ModelForm):

    class Meta:
        model = Encuesta
        fields = ('nombre', 'universo',)

class PreguntaForm(forms.ModelForm):

    class Meta:
        model = Pregunta
        fields = ('idE', 'pregunta',)

class RespuestaForm(forms.ModelForm):

    class Meta:
        model = Respuesta
        fields = ('respuesta',)