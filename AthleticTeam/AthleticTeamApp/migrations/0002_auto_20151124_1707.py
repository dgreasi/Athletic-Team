# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(related_name='away_team', to='AthleticTeamApp.Team', null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(related_name='home_team', to='AthleticTeamApp.Team', null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
