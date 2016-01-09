# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(default='photos/index.png', upload_to='photos/', blank=True)),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('profile', models.TextField(blank=True)),
                ('position', models.CharField(blank=True, max_length=50, choices=[('President', 'President'), ('Member', 'Member'), ('Executive Director', 'Executive Director'), ('Technical Director', 'Technical Director'), ('Football Manager Operation Department', 'Football Manager Operation Department'), ('CEO', 'CEO'), ('Communications Director', 'Communications Director'), ('Commercial Director', 'Commercial Director'), ('Deputy General Manager-Communication and Public Relations', 'Deputy General Manager-Communication and Public Relations'), ('CFO', 'CFO')])),
                ('nationality', models.CharField(max_length=30, blank=True)),
            ],
        ),
    ]
