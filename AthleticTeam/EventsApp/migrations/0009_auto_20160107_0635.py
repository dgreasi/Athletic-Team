# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventsApp', '0008_event_event_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_content',
            field=models.TextField(blank=True),
        ),
    ]
