# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0006_auto_20151122_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
