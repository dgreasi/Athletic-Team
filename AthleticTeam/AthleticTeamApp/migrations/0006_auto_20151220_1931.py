# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0005_auto_20151220_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='time',
            new_name='duration',
        ),
    ]
