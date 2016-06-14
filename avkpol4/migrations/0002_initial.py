# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserData'
        db.create_table(u'avkpol4_userdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=125)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=125)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=125)),
            ('other_conts', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('avkpol4', ['UserData'])

        # Adding model 'RequestLog'
        db.create_table(u'avkpol4_requestlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('requested_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('request_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('request_ip', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('avkpol4', ['RequestLog'])

        # Adding model 'ModelLog'
        db.create_table(u'avkpol4_modellog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, max_length=19, blank=True)),
        ))
        db.send_create_signal(u'avkpol4', ['ModelLog'])


    def backwards(self, orm):
        # Deleting model 'UserData'
        db.delete_table(u'avkpol4_userdata')

        # Deleting model 'RequestLog'
        db.delete_table(u'avkpol4_requestlog')

        # Deleting model 'ModelLog'
        db.delete_table(u'avkpol4_modellog')


    models = {
        u'avkpol4.modellog': {
            'Meta': {'object_name': 'ModelLog'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'max_length': '19', 'blank': 'True'})
        },
        'avkpol4.requestlog': {
            'Meta': {'object_name': 'RequestLog'},
            'datetime': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_ip': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'request_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'requested_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'avkpol4.userdata': {
            'Meta': {'object_name': 'UserData'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'other_conts': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '125'})
        }
    }

    complete_apps = ['avkpol4']