# Generated by Django 3.0.6 on 2020-05-25 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('uc', models.IntegerField(blank=True, editable=False, null=True)),
                ('um', models.IntegerField(blank=True, editable=False, null=True)),
                ('descripcion', models.CharField(help_text='Descripción del barrio', max_length=45, unique=True, verbose_name='Descripción barrio')),
                ('nota', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Barrio',
                'verbose_name_plural': 'Barrios',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('uc', models.IntegerField(blank=True, editable=False, null=True)),
                ('um', models.IntegerField(blank=True, editable=False, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la ciudad', max_length=45, unique=True, verbose_name='Descripción ciudad')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('uc', models.IntegerField(blank=True, editable=False, null=True)),
                ('um', models.IntegerField(blank=True, editable=False, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la EPS', max_length=45, unique=True, verbose_name='Descripción EPS')),
            ],
            options={
                'verbose_name': 'EPS',
                'verbose_name_plural': "EPS's",
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('uc', models.IntegerField(blank=True, editable=False, null=True)),
                ('um', models.IntegerField(blank=True, editable=False, null=True)),
                ('descripcion', models.CharField(help_text='Descripción del género', max_length=45, unique=True, verbose_name='Descripción género')),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Géneros',
            },
        ),
        migrations.CreateModel(
            name='Rol_miembro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('uc', models.IntegerField(blank=True, editable=False, null=True)),
                ('um', models.IntegerField(blank=True, editable=False, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la sede dende estudia', max_length=45, unique=True, verbose_name='Descripción sede')),
            ],
            options={
                'verbose_name': 'Rol miembro',
                'verbose_name_plural': 'Rol miembro',
            },
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('uc', models.IntegerField(blank=True, editable=False, null=True)),
                ('um', models.IntegerField(blank=True, editable=False, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la sede dende estudia', max_length=255, unique=True, verbose_name='Descripción sede')),
            ],
            options={
                'verbose_name': 'Sede',
                'verbose_name_plural': 'Sedes',
            },
        ),
        migrations.CreateModel(
            name='Tipo_sangre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('uc', models.IntegerField(blank=True, editable=False, null=True)),
                ('um', models.IntegerField(blank=True, editable=False, null=True)),
                ('descripcion', models.CharField(help_text='Descripción del tipo de sangre', max_length=45, unique=True, verbose_name='Descripción tipo de sangre')),
            ],
            options={
                'verbose_name': 'Tipo_sangre',
                'verbose_name_plural': 'Tipo_sangre',
            },
        ),
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('uc', models.IntegerField(blank=True, editable=False, null=True)),
                ('um', models.IntegerField(blank=True, editable=False, null=True)),
                ('nombres', models.CharField(max_length=45, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=45, verbose_name='Apellidos')),
                ('correo_institucional', models.EmailField(max_length=70, unique=True, verbose_name='Correo electrónico')),
                ('correo_personal', models.EmailField(max_length=70, unique=True, verbose_name='Correo electrónico')),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('celular', models.CharField(max_length=15, null=True)),
                ('barrio', models.ForeignKey(help_text='Barrio donde vive el miembro', null=True, on_delete=django.db.models.deletion.PROTECT, to='miembro.Barrio', verbose_name='Barrio')),
                ('eps', models.ForeignKey(help_text='EPS del miembro', null=True, on_delete=django.db.models.deletion.PROTECT, to='miembro.Eps', verbose_name='EPS')),
                ('genero', models.ForeignKey(help_text='Gérero del miembro', null=True, on_delete=django.db.models.deletion.PROTECT, to='miembro.Genero', verbose_name='Género')),
                ('rol_miembro', models.ForeignKey(help_text='Rol del miembro dentro de la rama', null=True, on_delete=django.db.models.deletion.PROTECT, to='miembro.Rol_miembro', verbose_name='Rol miembro')),
                ('sede', models.ForeignKey(help_text='Sede donde estudia el miembro', null=True, on_delete=django.db.models.deletion.PROTECT, to='miembro.Sede', verbose_name='Sede')),
                ('tipo_sangre', models.ForeignKey(help_text='Tipo de sangre del miembro', null=True, on_delete=django.db.models.deletion.PROTECT, to='miembro.Tipo_sangre', verbose_name='RH')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Miembro',
                'verbose_name_plural': 'Miembros',
            },
        ),
        migrations.AddField(
            model_name='barrio',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='miembro.Ciudad'),
        ),
    ]
