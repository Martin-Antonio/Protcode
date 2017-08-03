# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0008_auto_20170521_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api_tools',
            name='id',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='resouces_tools',
            name='id',
        ),
        migrations.RemoveField(
            model_name='shop_client',
            name='id',
        ),
        migrations.RemoveField(
            model_name='vcs',
            name='id',
        ),
        migrations.AlterField(
            model_name='api_tools',
            name='Business',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='aplication_log',
            name='Client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.Shop_client'),
        ),
        migrations.AlterField(
            model_name='aplication_log',
            name='Estate',
            field=models.CharField(help_text='Aqui de ve', max_length=100),
        ),
        migrations.AlterField(
            model_name='developer',
            name='Name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='developer',
            name='Store',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resouces_tools',
            name='Means',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='shop_client',
            name='Client',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vcs',
            name='VCS',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
