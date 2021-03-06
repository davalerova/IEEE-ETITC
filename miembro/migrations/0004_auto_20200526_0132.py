# Generated by Django 3.0.6 on 2020-05-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembro', '0003_auto_20200525_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrio',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Está activo'),
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Está activo'),
        ),
        migrations.AlterField(
            model_name='eps',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Está activo'),
        ),
        migrations.AlterField(
            model_name='genero',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Está activo'),
        ),
        migrations.AlterField(
            model_name='miembro',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Está activo'),
        ),
        migrations.AlterField(
            model_name='rol_miembro',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Está activo'),
        ),
        migrations.AlterField(
            model_name='sede',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Está activo'),
        ),
        migrations.AlterField(
            model_name='tipo_sangre',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Está activo'),
        ),
    ]
