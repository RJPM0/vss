from django.contrib import admin

# Register models, show values in screen admins
from .models import Alumno, Curso, School

admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(School)
