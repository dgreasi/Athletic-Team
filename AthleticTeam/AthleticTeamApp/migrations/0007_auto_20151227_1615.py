# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0006_auto_20151227_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranking',
            name='overall_rank',
        ),
        migrations.AddField(
            model_name='player',
            name='overall_rank',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
    ]
