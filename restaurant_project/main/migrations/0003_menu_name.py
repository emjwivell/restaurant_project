# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160312_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.CharField(default='Lunch Menu', max_length=255),
            preserve_default=False,
        ),
    ]