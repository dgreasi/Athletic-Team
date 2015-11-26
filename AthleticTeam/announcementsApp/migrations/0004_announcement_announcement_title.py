# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('announcementsApp', '0003_auto_20151115_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='announcement_title',
            field=models.CharField(default=datetime.datetime(2015, 11, 18, 9, 10, 28, 974549, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
