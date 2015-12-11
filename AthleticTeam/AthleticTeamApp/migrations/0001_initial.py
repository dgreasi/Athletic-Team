# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoachingStaffMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('info', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to=b'photos/', blank=True)),
                ('position', models.CharField(max_length=30, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
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
                ('info', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to=b'photos/', blank=True)),
                ('height', models.DecimalField(null=True, max_digits=3, decimal_places=2, blank=True)),
                ('weight', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('primary_position', models.CharField(blank=True, max_length=2, choices=[(b'PG', b'Point Guard'), (b'SG', b'Shooting Guard'), (b'SF', b'Small Forward'), (b'PF', b'Power Forward'), (b'CE', b'Center')])),
                ('secondary_positions', models.CharField(max_length=30, blank=True)),
                ('number', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('nationality', models.CharField(max_length=30, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('power_arm', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('power_body', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('power_legs', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('speed', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('team_play', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('co_op', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('rate_of_pos', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('two_shots', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('three_shots', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('player', models.ForeignKey(to='AthleticTeamApp.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=30, blank=True)),
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
            name='away_team',
            field=models.ForeignKey(related_name='away_team', to='AthleticTeamApp.Team', null=True),
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
            model_name='coachingstaffmember',
            name='team',
            field=models.ForeignKey(to='AthleticTeamApp.Team'),
        ),
        migrations.AlterUniqueTogether(
            name='ranking',
            unique_together=set([('player', 'owner')]),
        ),
    ]
