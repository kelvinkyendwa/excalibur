# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-04 06:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_movies_logo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='ser_name',
        ),
        migrations.RemoveField(
            model_name='series',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='series',
            name='series_genre',
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
        migrations.DeleteModel(
            name='Series',
        ),
    ]
