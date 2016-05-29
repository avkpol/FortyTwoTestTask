# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avkpol4', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='user_id',
        ),
        migrations.AddField(
            model_name='userdata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
