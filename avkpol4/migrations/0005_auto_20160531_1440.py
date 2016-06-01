# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avkpol4', '0004_modellog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modellog',
            name='model',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='modellog',
            name='updated',
            field=models.DateTimeField(auto_now=True, auto_now_add=True, max_length=19),
        ),
    ]
