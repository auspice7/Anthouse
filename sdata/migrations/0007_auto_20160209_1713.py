# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdata', '0006_stock_current_volumediff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_current',
            name='shcode',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]