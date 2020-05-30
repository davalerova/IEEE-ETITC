from django.contrib import admin

from .models import Tipo_actividad, Actividad_interna

# Register your models here.


@admin.register(Tipo_actividad)
class Tipo_actividadAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'activo')
    list_display_links = ('descripcion', 'activo', )
    list_filter = ('descripcion', 'activo', )

@admin.register(Actividad_interna)
class ActividadInternaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion', 'solo_miembros', 'activo')
    list_display_links = ('nombre','descripcion')
    list_filter = ('tipo_actividad__descripcion', 'solo_miembros', 'activo')
    search_fields = ('nombre', 'descripcion', 'lugar_actividad', 'tipo_actividad__descripcion')