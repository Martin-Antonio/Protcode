# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 00:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0023_auto_20170525_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplication_log1',
            name='Group_developer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Developmet_group.Developmet_group'),
        ),
    ]
