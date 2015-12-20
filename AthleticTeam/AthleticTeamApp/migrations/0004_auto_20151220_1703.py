# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0003_exercise_obj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
