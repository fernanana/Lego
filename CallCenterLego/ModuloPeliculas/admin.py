from django.contrib import admin
from .models import Pelicula

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('nombre','genero','clasificacion','duracion','sucursal','sala','fecha_exhibicion','hora_exhibicion', 'valor_ticket')
    list_filter = ('sucursal', 'genero', 'clasificacion', 'sala', 'fecha_exhibicion')
    search_fields = ('nombre', 'sucursal', 'genero')

admin.site.register(Pelicula)