# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(default='photos/index.png', upload_to='photos/', blank=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('info', models.TextField(blank=True)),
            ],
        ),
    ]
