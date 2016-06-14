# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model', models.CharField(max_length=30)),
                ('action', models.CharField(max_length=16)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True, max_length=19)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.CharField(max_length=40)),
                ('requested_url', models.CharField(max_length=255)),
                ('request_type', models.CharField(max_length=10)),
                ('request_ip', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Standard'), (2, b'Higher')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=125, verbose_name=b'Name')),
                ('last_name', models.CharField(max_length=125, verbose_name=b'Last name')),
                ('birth_date', models.DateField(null=True, verbose_name=b'Date of Birth')),
                ('bio', models.TextField(verbose_name=b'Bio')),
                ('email', models.EmailField(max_length=75, verbose_name=b'Email')),
                ('jabber', models.EmailField(max_length=75, verbose_name=b'Jabber')),
                ('skype', models.CharField(max_length=125, verbose_name=b'Skype')),
                ('other_conts', models.TextField(verbose_name=b'Other contacts')),
                ('photo', models.ImageField(null=True, upload_to=b'photo/', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
