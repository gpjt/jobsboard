# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Retweeter'
        db.create_table('main_retweeter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('access_key', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('access_secret', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal('main', ['Retweeter'])


    def backwards(self, orm):
        # Deleting model 'Retweeter'
        db.delete_table('main_retweeter')


    models = {
        'main.job': {
            'Meta': {'object_name': 'Job'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'experience': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'filled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'salary': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'})
        },
        'main.retweeter': {
            'Meta': {'object_name': 'Retweeter'},
            'access_key': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'access_secret': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['main']