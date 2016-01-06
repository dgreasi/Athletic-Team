# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SponsorsApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='image',
            new_name='image_model',
        ),
    ]
