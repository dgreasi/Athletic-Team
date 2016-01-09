# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarium', '0001_initial'),
        ('AthleticTeamApp', '0002_auto_20160109_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_object',
            field=models.ForeignKey(to='calendarium.Event', null=True),
        ),
    ]
