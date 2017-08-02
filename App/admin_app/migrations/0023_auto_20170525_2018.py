# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 00:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Developmet_group', '0001_initial'),
        ('admin_app', '0022_auto_20170525_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplication_log1',
            fields=[
                ('Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Estate', models.CharField(choices=[('1', 'En desarrollo'), ('2', 'En producción'), ('3', 'Indefinido'), ('4', 'Concluido')], max_length=50)),
                ('State_Store', models.CharField(blank=True, choices=[('1', 'Publicada'), ('2', 'En Proceso'), ('3', 'En certificación'), ('4', 'Eliminada'), ('5', 'Indefinido')], max_length=100, null=True)),
                ('URL_store', models.URLField(blank=True, max_length=300, null=True)),
                ('Console_Developer', models.URLField(blank=True, max_length=300, null=True)),
                ('Device', models.CharField(blank=True, max_length=100, null=True)),
                ('Monetization', models.CharField(blank=True, max_length=100, null=True)),
                ('Photo1', models.ImageField(blank=True, null=True, upload_to='media/Image')),
                ('Photo2', models.ImageField(blank=True, null=True, upload_to='media/Image')),
                ('Photo3', models.ImageField(blank=True, null=True, upload_to='media/Image')),
                ('Photo4', models.ImageField(blank=True, null=True, upload_to='media/Image')),
                ('Key_project', models.CharField(blank=True, max_length=100, null=True)),
                ('URL_VCS', models.URLField(blank=True, max_length=300, null=True)),
                ('Packages', models.FileField(blank=True, null=True, upload_to='media/Packges')),
                ('Description', models.TextField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('API', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Aplication_log4', to='admin_app.API_Tools')),
                ('Client', models.ManyToManyField(related_name='Shop_client2', to='admin_app.Shop_client')),
                ('Group_developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Developmet_group.Developmet_group')),
                ('Means', models.ManyToManyField(to='admin_app.Resouces_tools')),
                ('Store', models.ManyToManyField(related_name='Shopclient1', to='admin_app.Shop_client')),
                ('Type_app', models.ManyToManyField(to='admin_app.API_Tools')),
                ('VCS', models.ManyToManyField(related_name='Aplication_log5', to='admin_app.VCS')),
            ],
        ),
        migrations.RemoveField(
            model_name='aplication_log',
            name='API',
        ),
        migrations.RemoveField(
            model_name='aplication_log',
            name='Client',
        ),
        migrations.RemoveField(
            model_name='aplication_log',
            name='Means',
        ),
        migrations.RemoveField(
            model_name='aplication_log',
            name='Store',
        ),
        migrations.RemoveField(
            model_name='aplication_log',
            name='Type_app',
        ),
        migrations.RemoveField(
            model_name='aplication_log',
            name='VCS',
        ),
        migrations.AddField(
            model_name='developer1',
            name='Group_developer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Developmet_group.Developmet_group'),
        ),
        migrations.AlterField(
            model_name='developer1',
            name='Name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Aplication_log6', serialize=False, to='admin_app.Aplication_log1'),
        ),
        migrations.DeleteModel(
            name='Aplication_log',
        ),
    ]