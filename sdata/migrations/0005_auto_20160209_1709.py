# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 08:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdata', '0004_auto_20160209_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock_current',
            old_name='jnivolume',
            new_name='jnilvolume',
        ),
    ]
