# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0002_auto_20160106_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='event_object',
            field=models.ForeignKey(to='calendarium.Event'),
        ),
    ]
