# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-29 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0004_auto_20170801_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(default='static/images/avatar/defaultUser.png', upload_to='static/images/avatar/'),
        ),
    ]
