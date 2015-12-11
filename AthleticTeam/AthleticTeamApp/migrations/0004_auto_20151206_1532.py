# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0003_auto_20151205_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ranking',
            old_name='power',
            new_name='power_arm',
        ),
        migrations.AddField(
            model_name='ranking',
            name='co_op',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ranking',
            name='power_body',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ranking',
            name='power_legs',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ranking',
            name='rate_of_pos',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ranking',
            name='team_play',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
