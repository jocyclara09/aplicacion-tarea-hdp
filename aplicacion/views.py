from django.shortcuts import render

def lista_encuesta(request):
    return render(request, 'aplicacion/lista_encuesta.html', {})
