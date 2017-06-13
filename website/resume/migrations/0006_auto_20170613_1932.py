# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 17:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20170612_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='intro_url',
            field=models.URLField(default=None),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='intro_url_en',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='intro_url_es',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='intro_url_fr',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2017, 6, 13, 17, 32, 12, 793972, tzinfo=utc)),
        ),
    ]
