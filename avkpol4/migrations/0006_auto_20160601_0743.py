# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avkpol4', '0005_auto_20160531_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestlog',
            name='is_viewed',
        ),
        migrations.AddField(
            model_name='requestlog',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Standard'), (2, b'Higher')]),
            preserve_default=True,
        ),
    ]
