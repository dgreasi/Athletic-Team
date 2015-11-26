# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcementsApp', '0002_auto_20151115_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.TextField()),
                ('votes', models.IntegerField(default=0)),
                ('announcement', models.ForeignKey(to='announcementsApp.Announcement')),
            ],
        ),
        migrations.RemoveField(
            model_name='vote',
            name='announcement',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
