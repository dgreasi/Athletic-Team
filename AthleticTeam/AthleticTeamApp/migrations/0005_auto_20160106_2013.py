# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0004_training_event_object'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='event_object',
            field=models.ForeignKey(to='calendarium.Event', null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='event_object',
            field=models.ForeignKey(to='calendarium.Event', null=True),
        ),
    ]
