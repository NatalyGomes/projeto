# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170808_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Aluno', to='blog.Curso', verbose_name=b'Curso'),
        ),
    ]
