# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coachingstaffmember',
            name='image',
            field=models.ImageField(upload_to=b'photos/', blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='image',
            field=models.ImageField(upload_to=b'photos/', blank=True),
        ),
    ]
