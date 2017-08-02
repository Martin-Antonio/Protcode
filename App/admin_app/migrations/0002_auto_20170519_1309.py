# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplication_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Estate', models.CharField(max_length=100)),
                ('Store', models.CharField(max_length=100)),
                ('State_Store', models.CharField(max_length=100)),
                ('URL_store', models.URLField(max_length=300)),
                ('Console_Developer', models.URLField(max_length=300)),
                ('Client', models.CharField(max_length=100)),
                ('Platform', models.CharField(max_length=100)),
                ('API', models.CharField(max_length=100)),
                ('Type_app', models.CharField(max_length=100)),
                ('Means', models.CharField(max_length=100)),
                ('Device', models.CharField(max_length=100)),
                ('Monetization', models.CharField(max_length=100)),
                ('VCS', models.CharField(max_length=100)),
                ('Key_project', models.CharField(max_length=100)),
                ('URL_VCS', models.URLField(max_length=300)),
                ('Description', models.TextField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resouces_tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Means', models.CharField(max_length=100)),
                ('Utility', models.CharField(max_length=100)),
                ('URL_tools', models.URLField(max_length=300)),
                ('User', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shop_client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client', models.CharField(max_length=100)),
                ('URL_client', models.URLField(max_length=300)),
                ('Store', models.CharField(max_length=100)),
                ('URL_store', models.URLField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Admin_app',
        ),
    ]
