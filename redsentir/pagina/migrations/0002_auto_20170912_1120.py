# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-12 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrusel',
            name='avatar',
        ),
        migrations.AddField(
            model_name='carrusel',
            name='imagen',
            field=models.ImageField(default=1, upload_to='static/images/pagina/carrusel'),
            preserve_default=False,
        ),
    ]
