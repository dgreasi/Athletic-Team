# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0006_auto_20151220_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationalchart',
            name='position',
            field=models.CharField(blank=True, choices=[(b'Sports Organizational Manager', b'Sports Organizational Manager'), (b'Youth Department Techincal Manager', b'Youth Department Techincal Manager')], max_length=50),
        ),
    ]
