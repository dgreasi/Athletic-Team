# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coachingstaffmember',
            name='user',
        ),
        migrations.RemoveField(
            model_name='player',
            name='user',
        ),
    ]
