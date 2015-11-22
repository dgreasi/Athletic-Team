# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='secondary_positions',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
