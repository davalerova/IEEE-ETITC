# Generated by Django 3.0.6 on 2020-05-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividad_interna', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad_interna',
            name='lugar_actividad',
            field=models.CharField(max_length=255),
        ),
    ]