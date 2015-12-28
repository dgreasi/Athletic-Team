# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0004_auto_20151225_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestPlayers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('average_rank', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
                ('player', models.ForeignKey(to='AthleticTeamApp.Player')),
            ],
        ),
    ]
