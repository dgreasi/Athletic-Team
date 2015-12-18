# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('announcement_title', models.CharField(max_length=50)),
                ('announcement_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.TextField()),
                ('votes', models.IntegerField(default=0)),
                ('announcement', models.ForeignKey(to='announcementsApp.Announcement')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
