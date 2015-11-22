# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0004_auto_20151122_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.DecimalField(max_digits=3, decimal_places=0, blank=True),
        ),
    ]
