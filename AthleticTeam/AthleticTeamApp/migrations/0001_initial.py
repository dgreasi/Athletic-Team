# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_pts', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('away_pts', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('stadium', models.CharField(max_length=30, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('time', models.TimeField(null=True, blank=True)),
                ('info', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MatchPlayerStatistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('started', models.BooleanField()),
                ('time_played', models.TimeField()),
                ('pts', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('two_pm', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('two_pa', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('three_pm', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('three_pa', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ftm', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('fta', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('tov', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('oreb', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('dreb', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ast', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('stl', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('blk', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('pf', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('match', models.ForeignKey(to='AthleticTeamApp.Match')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='matchplayerstatistics',
            name='player',
            field=models.ForeignKey(to='AthleticTeamApp.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(related_name='away_team', to='AthleticTeamApp.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(related_name='home_team', to='AthleticTeamApp.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(to='AthleticTeamApp.Player', through='AthleticTeamApp.MatchPlayerStatistics'),
        ),
    ]
