# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-10 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0002_auto_20180303_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuentro',
            name='carreta11',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/images/pagina/articulo'),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='carreta12',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/images/pagina/articulo'),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='carreta13',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/images/pagina/articulo'),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='carreta14',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/images/pagina/articulo'),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='carreta15',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/images/pagina/articulo'),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='entrevista2',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='entrevista3',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='entrevista4',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='entrevista5',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='imagen4',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/images/pagina/articulo'),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='parrafo5',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='parrafo6',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='encuentro',
            name='subTitulo',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]