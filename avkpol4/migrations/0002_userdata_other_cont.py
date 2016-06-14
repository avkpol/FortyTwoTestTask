# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('avkpol4', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='other_cont',
            field=models.CharField(default=datetime.date(2016, 6, 13), max_length=125, verbose_name=b'Other contacts'),
            preserve_default=False,
        ),
    ]
