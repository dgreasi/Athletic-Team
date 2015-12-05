# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0002_ranking'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ranking',
            unique_together=set([('player', 'owner')]),
        ),
    ]
