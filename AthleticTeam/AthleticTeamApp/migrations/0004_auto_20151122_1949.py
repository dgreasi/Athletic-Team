# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0003_auto_20151122_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.DecimalField(max_digits=3, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.DecimalField(max_digits=3, decimal_places=0, blank=True),
        ),
    ]
