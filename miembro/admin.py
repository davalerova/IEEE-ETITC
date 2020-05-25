from django.contrib import admin

from .models import Miembro, Genero, Eps, Ciudad, Barrio, Tipo_sangre, Sede, Rol_miembro, User

# Register your models here.
admin.site.register(Genero)
admin.site.register(Eps)
admin.site.register(Ciudad)
admin.site.register(Barrio)
admin.site.register(Tipo_sangre)
admin.site.register(Sede)
admin.site.register(Rol_miembro)


@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'correo_institucional', 'correo_personal', 'fecha_nacimiento', 'edad', 'mayor_de_edad','celular', 'genero', 'eps', 'barrio', 'ciudad', 'tipo_sangre', 'sede', 'rol_miembro')
    list_display_links = ('nombres', 'apellidos', 'correo_institucional', 'correo_personal', 'fecha_nacimiento', 'edad', 'mayor_de_edad','celular', 'genero', 'eps', 'barrio', 'ciudad','tipo_sangre', 'sede', 'rol_miembro')
    list_filter = ('barrio__ciudad', 'genero', 'sede', 'rol_miembro', 'eps', 'tipo_sangre')
    search_fields = ('nombres', 'apellidos', 'barrio__descripcion', 'barrio__ciudad__descripcion', 'celular')