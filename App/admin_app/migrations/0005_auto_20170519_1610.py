# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 20:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0004_auto_20170519_1539'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aplication_log1',
            new_name='Aplication_log',
        ),
        migrations.RenameModel(
            old_name='Resouces_tools2',
            new_name='Resouces_tools',
        ),
    ]
