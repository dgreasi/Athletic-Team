# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0005_auto_20151122_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
    ]
