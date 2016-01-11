# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0004_auto_20160111_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='calendarium.Event', null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='event_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='calendarium.Event', null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='event_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='calendarium.Event', null=True),
        ),
    ]
