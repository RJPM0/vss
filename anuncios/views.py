from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from .models import Anuncio, Curso #Llamamos al modelo para tenerlo tambiwen conectado la base de datos

# Creating views conection by URL
def anuncios_list(request):
    # listaCursos = Curso.objects.all()
    anuncios = Anuncio.objects.filter(estate="publico") #indicamos que queremos todos los datos de state en la vista siguiente
    return render(request, "anuncios.html",
                {
                    'anuncios': anuncios,
                    # 'listCurso': listaCursos
                })