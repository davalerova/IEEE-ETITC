from django.contrib import admin

from .models import Miembro, Genero, Eps, Ciudad, Barrio, Tipo_sangre, Sede, Rol_miembro, User

# Register your models here.
admin.site.register(Genero)
admin.site.register(Eps)
admin.site.register(Ciudad)
admin.site.register(Tipo_sangre)
admin.site.register(Sede)
admin.site.register(Rol_miembro)


@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'correo_institucional', 'correo_personal', 'fecha_nacimiento', 'edad', 'mayor_de_edad','celular', 'genero', 'eps', 'barrio', 'ciudad', 'tipo_sangre', 'sede', 'rol_miembro', 'activo')
    list_display_links = ('nombres', 'apellidos', 'correo_institucional', 'correo_personal', 'fecha_nacimiento', 'edad', 'mayor_de_edad','celular', 'genero', 'eps', 'barrio', 'ciudad','tipo_sangre', 'sede', 'rol_miembro')
    list_filter = ('barrio__ciudad', 'genero', 'sede', 'rol_miembro', 'eps', 'tipo_sangre', 'activo')
    search_fields = ('nombres', 'apellidos', 'barrio__descripcion', 'barrio__ciudad__descripcion', 'celular', 'rol_miembro__descripcion', 'genero__descripcion', 'barrio__descripcion', 'tipo_sangre__descripcion')

@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    list_display = ('descripcion','ciudad')
    list_display_links = ('descripcion','ciudad')
    list_filter = ('ciudad',)