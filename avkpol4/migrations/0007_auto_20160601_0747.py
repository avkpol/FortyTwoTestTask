# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avkpol4', '0006_auto_20160601_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestlog',
            name='datetime',
            field=models.CharField(max_length=40),
        ),
    ]
