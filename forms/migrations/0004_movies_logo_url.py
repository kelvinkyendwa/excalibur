# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-02 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_series_logo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='logo_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]