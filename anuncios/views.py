from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from .models import School, Alumno, Curso #Llamamos al modelo para tenerlo tambiwen conectado la base de datos

center= 0
curso=0

# Creating views conection by URL
def centros_list(request):
    listaCentros = School.objects.all()
    #indicamos que queremos todos los datos de state en la vista siguiente
    if(len(listaCentros)!=0):
        return render(request, "anuncios.html",{
                        'listaCentros': listaCentros
                    })
    else:
        html = '<html><body><strong>No hay datos</strong></body></html>'
        return HttpResponse(html)

def cursos_list(request):
    center = request.GET.get("id")
    centro = School.objects.get(id = center)
    listaCursos = Curso.objects.filter(center_id = center)
    #indicamos que queremos todos los datos de state en la vista siguiente
    if(len(listaCursos)!=0):
        return render(request, "cursos.html",{
                        'listCursos': listaCursos,
                        'centro': centro
                    })
    else:
        html = '<html><body><strong>No hay datos</strong></body></html>'
        return HttpResponse(html)

def student_list(request):
    print(request.GET)
    curso = request.GET.get("id")
    curso = Curso.objects.get(id = curso)
    listaAlumno = Alumno.objects.filter(cuso_id = request.GET.get("id"))
    return render(request, "student.html",{
                    'listaAlumnos': listaAlumno,
                    "curso": curso
                })