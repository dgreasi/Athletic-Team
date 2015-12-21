# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields
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
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=30)),
                ('type', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Personal'), (b'T', b'Team')])),
                ('duration', models.SmallIntegerField(default=0)),
                ('obj', multiselectfield.db.fields.MultiSelectField(blank=True, max_length=39, choices=[(b'SPD', b'Speed'), (b'STA', b'Stamina'), (b'POW', b'Power'), (b'MEN', b'Mentality'), (b'SHO', b'Shoot'), (b'ATK', b'Attack'), (b'DEF', b'Defence'), (b'DRI', b'Dribbling'), (b'PAS', b'Pass'), (b'TMW', b'Teamwork')])),
                ('desc', models.TextField(blank=True)),
            ],
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
                ('away_team', models.CharField(max_length=30, blank=True)),
                ('home_away', models.CharField(max_length=30, blank=True)),
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
        migrations.CreateModel(
            name='TeamPlay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=30)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('location', models.CharField(max_length=30)),
                ('exercises', models.ManyToManyField(to='AthleticTeamApp.Exercise', blank=True)),
                ('team', models.ForeignKey(to='AthleticTeamApp.Team')),
                ('team_plays', models.ManyToManyField(to='AthleticTeamApp.TeamPlay', blank=True)),
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
