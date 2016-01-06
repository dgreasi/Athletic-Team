# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarium', '0001_initial'),
        ('AthleticTeamApp', '0003_auto_20160106_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='event_object',
            field=models.ForeignKey(default='', to='calendarium.Event'),
            preserve_default=False,
        ),
    ]
