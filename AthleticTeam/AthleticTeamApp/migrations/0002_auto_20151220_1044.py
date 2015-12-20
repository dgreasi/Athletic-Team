# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='desc',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='exercise',
            name='time',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='type',
            field=models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Personal'), (b'T', b'Team')]),
        ),
    ]
