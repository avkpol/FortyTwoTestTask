# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avkpol4', '0002_userdata_other_cont'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='other_cont',
            new_name='other_conts',
        ),
    ]
