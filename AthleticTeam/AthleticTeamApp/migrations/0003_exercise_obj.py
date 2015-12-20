# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('AthleticTeamApp', '0002_auto_20151220_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='obj',
            field=multiselectfield.db.fields.MultiSelectField(default=b'', max_length=39, choices=[(b'SPD', b'Speed'), (b'STA', b'Stamina'), (b'POW', b'Power'), (b'MEN', b'Mentality'), (b'SHO', b'Shoot'), (b'ATK', b'Attack'), (b'DEF', b'Defence'), (b'DRI', b'Dribbling'), (b'PAS', b'Pass'), (b'TMW', b'Teamwork')]),
        ),
    ]
