# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-06 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacion', '0003_auto_20180310_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuentro',
            name='video',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]