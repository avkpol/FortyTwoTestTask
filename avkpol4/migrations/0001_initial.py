# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.CharField(max_length=25)),
                ('requested_url', models.CharField(max_length=255)),
                ('request_type', models.CharField(max_length=10)),
                ('request_ip', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('name', models.CharField(max_length=125, verbose_name=b'Name')),
                ('last_name', models.CharField(max_length=125, verbose_name=b'Last name')),
                ('birth_date', models.DateField(null=True, verbose_name=b'Date of Birth')),
                ('bio', models.TextField(verbose_name=b'Bio')),
                ('email', models.EmailField(max_length=75, verbose_name=b'Email')),
                ('jabber', models.EmailField(max_length=75, verbose_name=b'Jabber')),
                ('skype', models.CharField(max_length=125, verbose_name=b'Skype')),
                ('photo', models.ImageField(null=True, upload_to=b'photo/', blank=True)),
                ('user_id', models.AutoField(default=1, unique=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
