from django.db import models

from bases.models import ClaseModelo
from django.contrib.auth.models import User
# Create your models here.

from datetime import date

#################################################################################
class Tipo_actividad( ClaseModelo ):

    descripcion = models.CharField(
        max_length=45,
        help_text='Descripción del tipo de actividad',
        unique=True,
        verbose_name='Descripción tipo actividad'
    )

    def __str__(self):
        return '{}'.format( self.descripcion )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super( Tipo_actividad, self ).save()

    class Meta:
        verbose_name = 'Tipo de actividad'
        verbose_name_plural = 'Tipos de actividades'


#################################################################################

class Actividad_interna(ClaseModelo):

    tipo_actividad = models.ForeignKey(Tipo_actividad, on_delete=models.PROTECT)
    
    nombre = models.CharField(
        max_length=255,
        help_text='Nombre de la actividad',
        verbose_name='Nombre actividad'
    )

    descripcion = models.TextField(
        help_text='Descripción de la actividad',
        verbose_name='Descripción de la actividad'
    )

    fecha_actividad = models.DateTimeField(
    )

    lugar_actividad = models.CharField(max_length=255)

    solo_miembros = models.BooleanField(default=False
    )


    def save(self):
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.capitalize()
        self.lugar_actividad = self.lugar_actividad.upper()
        super( Actividad_interna, self ).save()
    
    def __str__(self):
        return '{}'.format( self.nombre)

    class Meta:
        verbose_name = 'Actividad interna'
        verbose_name_plural = 'Actividades internas'
