# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0005_bestplayers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bestplayers',
            name='player',
        ),
        migrations.AddField(
            model_name='ranking',
            name='overall_rank',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='BestPlayers',
        ),
    ]
