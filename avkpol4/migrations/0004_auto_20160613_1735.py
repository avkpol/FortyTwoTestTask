# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avkpol4', '0003_auto_20160613_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='other_conts',
            field=models.TextField(verbose_name=b'Other contacts'),
        ),
    ]
