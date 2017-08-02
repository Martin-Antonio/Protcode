# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_auto_20170519_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='API_Tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business', models.CharField(max_length=100)),
                ('Platform', models.CharField(max_length=100)),
                ('API', models.CharField(max_length=100)),
                ('URL_Platform', models.URLField(max_length=300)),
                ('User', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Estate', models.CharField(max_length=100)),
                ('Client', models.CharField(max_length=100)),
                ('Store', models.CharField(max_length=100)),
                ('Device', models.CharField(max_length=100)),
                ('VCS', models.CharField(max_length=100)),
                ('URL_VCS', models.URLField(max_length=300)),
                ('Platform', models.CharField(max_length=100)),
                ('API', models.CharField(max_length=100)),
                ('Type_app', models.CharField(max_length=100)),
                ('Date_start', models.DateTimeField()),
                ('Data_finish', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Resouces_tools2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Means', models.CharField(max_length=100)),
                ('Utility', models.CharField(max_length=100)),
                ('URL_tools', models.URLField(max_length=300)),
                ('User', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Type_app', models.CharField(max_length=100)),
                ('Commentary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VCS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VCS', models.CharField(max_length=100)),
                ('URL_VCS', models.URLField(max_length=300)),
                ('User', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Resouces_tools',
        ),
        migrations.RemoveField(
            model_name='aplication_log1',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='aplication_log1',
            name='id',
        ),
        migrations.AlterField(
            model_name='aplication_log1',
            name='Name',
            field=models.CharField(help_text='En este campo tiene  que  introducir el nombre de la app', max_length=100, primary_key=True, serialize=False),
        ),
    ]