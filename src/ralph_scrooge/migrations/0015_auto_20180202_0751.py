# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-02-02 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ralph_scrooge', '0014_dailycosts_partitioning'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='environment',
            name='ci_id',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='ci_uid',
        ),
        migrations.RemoveField(
            model_name='environment',
            name='ralph3_id',
        ),
        migrations.AlterField(
            model_name='environment',
            name='name',
            field=models.CharField(db_index=True, max_length=75, unique=True, verbose_name='name'),
        ),
    ]