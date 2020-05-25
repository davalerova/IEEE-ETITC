from django.db import models

from bases.models import ClaseModelo
from django.contrib.auth.models import User
# Create your models here.


#################################################################################
class Genero( ClaseModelo ):

    descripcion = models.CharField(
        max_length=45,
        help_text='Descripción del género',
        unique=True,
        verbose_name='Descripción género'
    )

    def __str__(self):
        return '{}'.format( self.descripcion )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super( Genero, self ).save()

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

#################################################################################
class Eps( ClaseModelo ):

    descripcion = models.CharField(
        max_length=45,
        help_text='Descripción de la EPS',
        unique=True,
        verbose_name='Descripción EPS'
    )

    def __str__(self):
        return '{}'.format( self.descripcion )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super( Eps, self ).save()

    class Meta:
        verbose_name = 'EPS'
        verbose_name_plural = "EPS's"

#################################################################################
class Ciudad( ClaseModelo ):

    descripcion = models.CharField(
        max_length=45,
        help_text='Descripción de la ciudad',
        unique=True,
        verbose_name='Descripción ciudad'
    )

    def __str__(self):
        return '{}'.format( self.descripcion )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super( Ciudad, self ).save()

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = "Ciudades"

#################################################################################
class Barrio( ClaseModelo ):

    descripcion = models.CharField(
        max_length=45,
        help_text='Descripción del barrio',
        unique=True,
        verbose_name='Descripción barrio'
    )

    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)

    nota = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format( self.descripcion )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super( Barrio, self ).save()

    class Meta:
        verbose_name = 'Barrio'
        verbose_name_plural = "Barrios"

#################################################################################
class Tipo_sangre( ClaseModelo ):

    descripcion = models.CharField(
        max_length=45,
        help_text='Descripción del tipo de sangre',
        unique=True,
        verbose_name='Descripción tipo de sangre'
    )

    def __str__(self):
        return '{}'.format( self.descripcion )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super( Tipo_sangre, self ).save()

    class Meta:
        verbose_name = 'Tipo_sangre'
        verbose_name_plural = "Tipo_sangre"

#################################################################################
class Sede( ClaseModelo ):

    descripcion = models.CharField(
        max_length=255,
        help_text='Descripción de la sede dende estudia',
        unique=True,
        verbose_name='Descripción sede'
    )

    def __str__(self):
        return '{}'.format( self.descripcion )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super( Sede, self ).save()

    class Meta:
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'

#################################################################################
class Rol_miembro( ClaseModelo ):

    descripcion = models.CharField(
        max_length=45,
        help_text='Descripción de la sede dende estudia',
        unique=True,
        verbose_name='Descripción sede'
    )

    def __str__(self):
        return '{}'.format( self.descripcion )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super( Rol_miembro, self ).save()

    class Meta:
        verbose_name = 'Rol miembro'
        verbose_name_plural = 'Rol miembro'

#################################################################################

class Miembro(ClaseModelo):

    nombres = models.CharField(
        max_length=45,
        # help_text='Nombres del miembro',
        verbose_name='Nombres'
    )

    apellidos = models.CharField(
        max_length=45,
        # help_text='Apellidos del miembro',
        verbose_name='Apellidos'
    )

    correo_institucional = models.EmailField(
        max_length=70,
        # help_text='Correo electrónico del miembro',
        verbose_name='Correo electrónico',
        unique=True
    )

    correo_personal = models.EmailField(
        max_length=70,
        # help_text='Correo electrónico del miembro',
        verbose_name='Correo electrónico',
        unique=True
    )


    fecha_nacimiento = models.DateField(null=True)
    
    celular = models.CharField(max_length=15, null=True)
    
    genero = models.ForeignKey(Genero,
    help_text='Gérero del miembro',
    verbose_name='Género',
    on_delete=models.PROTECT,
    null=True
    )
    
    eps = models.ForeignKey(Eps,
    help_text='EPS del miembro',
    verbose_name='EPS',
    on_delete=models.PROTECT,
    null=True
    )

    barrio = models.ForeignKey(Barrio,
    help_text='Barrio donde vive el miembro',
    verbose_name='Barrio',
    on_delete=models.PROTECT,
    null=True
    )

    tipo_sangre = models.ForeignKey(Tipo_sangre,
    help_text='Tipo de sangre del miembro',
    verbose_name='RH',
    on_delete=models.PROTECT,
    null=True
    )

    sede = models.ForeignKey(Sede,
    help_text='Sede donde estudia el miembro',
    verbose_name='Sede',
    on_delete=models.PROTECT,
    null=True
    )

    rol_miembro = models.ForeignKey(Rol_miembro,
    help_text='Rol del miembro dentro de la rama',
    verbose_name='Rol miembro',
    on_delete=models.PROTECT,
    null=True
    )

    usuario = models.ForeignKey(User,
    on_delete=models.PROTECT
    )

    def save(self):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        self.correo_institucional = self.correo_institucional.lower()
        self.correo_personal = self.correo_personal.lower()
        super( Miembro, self ).save()
    
    def __str__(self):
        return '{}'.format( self.nombres + " " + self.apellidos )

    class Meta:
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'
