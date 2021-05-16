from django.db import models #importación estructuración de Base de datos
from django.utils import timezone #importando funciones de fecha y hora
from django.contrib.auth.models import User #importando usuario

# Creamos nuestro proyecto
class Curso(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, verbose_name= "Curso")
    alumnos = models.IntegerField(verbose_name= "Cantidad alumnos")
    approved = models.IntegerField(verbose_name= "Aprobados")
    suspense = models.IntegerField(verbose_name= "Suspensos")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['name']
    def __str__(self):
        return self.name

class Anuncio(models.Model):#Alumno
    STATUS_CHOICES={
        ('oculto', 'Oculto'),
        ('publico','Publico')
    }

    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=100, verbose_name="Titulación")
    photo = models.ImageField(null=True, upload_to='images', verbose_name='Foto')
    studen = models.CharField(max_length=50,verbose_name="Estudiante")
    comentary = models.TextField(verbose_name="Cometario")
    note = models.IntegerField(verbose_name="Nota total")
    aprove = models.BooleanField(blank=True, default=False, verbose_name="Aprobado")
    datetitulation = models.DateTimeField(auto_now_add=True, verbose_name="Fecha titulación")
    datematriculation = models.DateTimeField(verbose_name="Fecha matriculción")
    estate = models.CharField(max_length=15,
                            choices=STATUS_CHOICES,
                            default='oculto')
    cuso_id = models.ForeignKey('Curso', on_delete= models.CASCADE, null=True, verbose_name="Curso")
    class Meta: #Creamos la clase metadatos
        ordering = ("note","aprove","-datetitulation",) #Ordenamos los datos por fecha

    def __str__(self): #Función devolución de nombre titulo
        return  self.title + " - " + self.studen
