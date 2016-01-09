# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendarium', '0001_initial'),
        ('AthleticTeamApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='event_object',
            field=models.ForeignKey(to='calendarium.Event', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='exercises',
            field=models.ManyToManyField(to='AthleticTeamApp.Exercise', blank=True),
        ),
        migrations.AddField(
            model_name='training',
            name='team',
            field=models.ForeignKey(to='AthleticTeamApp.Team'),
        ),
        migrations.AddField(
            model_name='training',
            name='team_plays',
            field=models.ManyToManyField(to='AthleticTeamApp.TeamPlay', blank=True),
        ),
        migrations.AddField(
            model_name='ranking',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='ranking',
            name='player',
            field=models.ForeignKey(to='AthleticTeamApp.Player'),
        ),
        migrations.AddField(
            model_name='player',
            name='account',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='AthleticTeamApp.Team'),
        ),
        migrations.AddField(
            model_name='matchplayerstatistics',
            name='match',
            field=models.ForeignKey(to='AthleticTeamApp.Match'),
        ),
        migrations.AddField(
            model_name='matchplayerstatistics',
            name='player',
            field=models.ForeignKey(to='AthleticTeamApp.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(related_name='away_team', to='AthleticTeamApp.Team', null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='event_object',
            field=models.ForeignKey(to='calendarium.Event', null=True),
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
            model_name='event',
            name='creator',
            field=models.ForeignKey(related_name='creator', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coachingstaffmember',
            name='account',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
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
