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
                ('time_played', models.CharField(max_length=10, blank=True)),
                ('pts', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('two_pa', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('two_pm', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('three_pa', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('three_pm', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('fta', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ftm', models.PositiveSmallIntegerField(null=True, blank=True)),
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
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('height', models.DecimalField(null=True, max_digits=3, decimal_places=2, blank=True)),
                ('weight', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('primary_position', models.CharField(blank=True, max_length=2, choices=[(b'PG', b'Point Guard'), (b'SG', b'Shooting Guard'), (b'SF', b'Small Forward'), (b'PF', b'Power Forward'), (b'CE', b'Center')])),
                ('secondary_positions', models.CharField(max_length=30, blank=True)),
                ('number', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('info', models.TextField(blank=True)),
                ('nationality', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='AthleticTeamApp.Team'),
        ),
        migrations.AddField(
            model_name='matchplayerstatistics',
            name='player',
            field=models.ForeignKey(to='AthleticTeamApp.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(to='AthleticTeamApp.Player', through='AthleticTeamApp.MatchPlayerStatistics'),
        ),
    ]