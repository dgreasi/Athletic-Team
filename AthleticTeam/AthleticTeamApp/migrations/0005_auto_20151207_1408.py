# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0004_auto_20151206_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranking',
            name='three_shots',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ranking',
            name='two_shots',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
