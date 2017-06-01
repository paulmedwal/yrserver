# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yrtoolkitapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='add_date',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]