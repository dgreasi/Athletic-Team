# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0002_auto_20151125_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='training',
            name='team',
            field=models.ForeignKey(to='AthleticTeamApp.Team', null=True),
        ),
    ]
