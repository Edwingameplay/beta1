# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-16 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0010_auto_20180503_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='telefono',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
