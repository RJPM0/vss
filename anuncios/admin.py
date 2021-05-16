from django.contrib import admin

# Register models, show values in screen admins
from .models import Anuncio, Curso

admin.site.register(Anuncio)
admin.site.register(Curso)
