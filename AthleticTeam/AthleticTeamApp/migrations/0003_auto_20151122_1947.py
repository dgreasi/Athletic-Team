# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0002_player_secondary_positions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.DecimalField(max_digits=3, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.DecimalField(max_digits=3, decimal_places=1, blank=True),
        ),
    ]
