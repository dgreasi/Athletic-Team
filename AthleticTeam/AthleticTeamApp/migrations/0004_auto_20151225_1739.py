# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0003_auto_20151223_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranking',
            name='average_rank',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='co_op',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='power_arm',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='power_body',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='power_legs',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='rate_of_pos',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='speed',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='team_play',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='three_shots',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='two_shots',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
    ]
