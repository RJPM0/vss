from django.contrib import admin
from django.urls import path, include
#importando vistas
from anuncios import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('centros/', views.centros_list, name='centros_list'),
    path('centros/#/cursos/', views.cursos_list, name='cursos_list'),
    path('centros/#/cursos/#/alumnos/', views.student_list, name='student_list')
]