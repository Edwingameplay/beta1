# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-18 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipio',
            name='imagen_fondo',
            field=models.ImageField(default='static/images/isotiporedsentir.png', upload_to='static/images/mesa/municipio'),
        ),
        migrations.AddField(
            model_name='municipio',
            name='imagen_mapa',
            field=models.ImageField(default='static/images/isotiporedsentir.png', upload_to='static/images/mesa/municipio'),
        ),
    ]
