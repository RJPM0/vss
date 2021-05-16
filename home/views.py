from django.shortcuts import render
from django.template import RequestContext
from anuncios.models import Curso #Llamamos al modelo para tenerlo tambiwen conectado la base de datos

# Create your views conection by URL
def home_init(request):
    listaCursos = Curso.objects.all()
    return render(request, "home.html",{'listCursos': listaCursos})
