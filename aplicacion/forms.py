from django import forms

from .models import Encuesta

class LoginForm(forms.Form):
	username = forms.CharField(max_length=15)
	password = forms.CharField(max_length=10, widget= forms.PasswordInput())

class EncuestaForm(forms.ModelForm):

    class Meta:
        model = Encuesta
        fields = ('nombre', 'universo',)