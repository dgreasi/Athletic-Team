# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('height', models.FloatField(blank=True)),
                ('weight', models.FloatField(blank=True)),
                ('birth_date', models.DateField(blank=True)),
                ('primary_position', models.CharField(blank=True, max_length=2, choices=[(b'PG', b'Point Guard'), (b'SG', b'Shooting Guard'), (b'SF', b'Small Forward'), (b'PF', b'Power Forward'), (b'CE', b'Center')])),
                ('number', models.DecimalField(max_digits=3, decimal_places=1, blank=True)),
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
    ]
