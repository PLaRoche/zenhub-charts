# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 15:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0013_pipeline_is_cycle_time_starter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pipeline',
            name='is_cycle_time_starter',
        ),
    ]