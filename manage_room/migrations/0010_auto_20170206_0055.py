# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-05 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_room', '0009_auto_20170205_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='next_id',
            field=models.PositiveSmallIntegerField(default=0, unique=True),
        ),
    ]