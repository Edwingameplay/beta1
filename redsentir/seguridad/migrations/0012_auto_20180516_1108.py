# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-16 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0011_auto_20180516_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='municipio',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='seguridad.Municipio'),
        ),
    ]