# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarium', '0001_initial'),
        ('AthleticTeamApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='event_object',
            field=models.ForeignKey(default=0, to='calendarium.Event'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(related_name='home_team', to='AthleticTeamApp.Team', null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(to='AthleticTeamApp.Player', through='AthleticTeamApp.MatchPlayerStatistics'),
        ),
        migrations.AddField(
            model_name='leagueteamrel',
            name='league',
            field=models.ForeignKey(to='AthleticTeamApp.League'),
        ),
        migrations.AddField(
            model_name='leagueteamrel',
            name='team',
            field=models.ForeignKey(to='AthleticTeamApp.Team'),
        ),
        migrations.AddField(
            model_name='league',
            name='teams',
            field=models.ManyToManyField(to='AthleticTeamApp.Team', through='AthleticTeamApp.LeagueTeamRel'),
        ),
        migrations.AddField(
            model_name='coachingstaffmember',
            name='team',
            field=models.ForeignKey(to='AthleticTeamApp.Team'),
        ),
        migrations.AlterUniqueTogether(
            name='ranking',
            unique_together=set([('player', 'owner')]),
        ),
    ]
