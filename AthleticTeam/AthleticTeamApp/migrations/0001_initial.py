# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoachingStaffMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('info', models.TextField()),
                ('image', models.ImageField(default=b'photos/index.png', upload_to=b'photos/', blank=True)),
                ('position', models.CharField(max_length=30, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('info', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('approved_by_owner', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=30)),
                ('type', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Personal'), (b'T', b'Team')])),
                ('duration', models.SmallIntegerField(default=0)),
                ('obj', multiselectfield.db.fields.MultiSelectField(blank=True, max_length=39, choices=[(b'SPD', b'Speed'), (b'STA', b'Stamina'), (b'POW', b'Power'), (b'MEN', b'Mentality'), (b'SHO', b'Shoot'), (b'ATK', b'Attack'), (b'DEF', b'Defence'), (b'DRI', b'Dribbling'), (b'PAS', b'Pass'), (b'TMW', b'Teamwork')])),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'name', max_length=30)),
                ('season', models.CharField(default=b'2015-2016', max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeagueTeamRel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gp', models.PositiveSmallIntegerField(default=0)),
                ('wins', models.PositiveSmallIntegerField(default=0)),
                ('loses', models.PositiveSmallIntegerField(default=0)),
                ('pts_difference', models.SmallIntegerField(default=0)),
                ('pts', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_pts', models.PositiveSmallIntegerField(null=True)),
                ('away_pts', models.PositiveSmallIntegerField(null=True)),
                ('stadium', models.CharField(max_length=30)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('info', models.TextField()),
                ('home_away', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MatchPlayerStatistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('started', models.BooleanField()),
                ('time_played', models.CharField(max_length=10)),
                ('pts', models.PositiveSmallIntegerField(null=True)),
                ('two_pa', models.PositiveSmallIntegerField(null=True)),
                ('two_pm', models.PositiveSmallIntegerField(null=True)),
                ('three_pa', models.PositiveSmallIntegerField(null=True)),
                ('three_pm', models.PositiveSmallIntegerField(null=True)),
                ('fta', models.PositiveSmallIntegerField(null=True)),
                ('ftm', models.PositiveSmallIntegerField(null=True)),
                ('tov', models.PositiveSmallIntegerField(null=True)),
                ('oreb', models.PositiveSmallIntegerField(null=True)),
                ('dreb', models.PositiveSmallIntegerField(null=True)),
                ('ast', models.PositiveSmallIntegerField(null=True)),
                ('stl', models.PositiveSmallIntegerField(null=True)),
                ('blk', models.PositiveSmallIntegerField(null=True)),
                ('pf', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('info', models.TextField()),
                ('image', models.ImageField(default=b'photos/index.png', upload_to=b'photos/', blank=True)),
                ('height', models.DecimalField(null=True, max_digits=3, decimal_places=2)),
                ('weight', models.PositiveSmallIntegerField(null=True)),
                ('birth_date', models.DateField(null=True)),
                ('primary_position', models.CharField(max_length=2, choices=[(b'PG', b'Point Guard'), (b'SG', b'Shooting Guard'), (b'SF', b'Small Forward'), (b'PF', b'Power Forward'), (b'CE', b'Center')])),
                ('secondary_positions', models.CharField(max_length=30)),
                ('number', models.PositiveSmallIntegerField(null=True)),
                ('overall_rank', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('nationality', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('power_arm', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('power_body', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('power_legs', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('speed', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('team_play', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('co_op', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('rate_of_pos', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('two_shots', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('three_shots', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('average_rank', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=30)),
                ('image', models.ImageField(default=b'photos/index.png', upload_to=b'photos/', blank=True)),
                ('owned', models.BooleanField()),
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
            ],
            options={
                'abstract': False,
            },
        ),
    ]
