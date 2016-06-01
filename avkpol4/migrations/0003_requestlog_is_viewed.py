# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avkpol4', '0002_auto_20160526_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlog',
            name='is_viewed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
