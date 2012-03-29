# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Job'
        db.create_table('main_job', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('job_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=8192)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('experience', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('main', ['Job'])


    def backwards(self, orm):
        
        # Deleting model 'Job'
        db.delete_table('main_job')


    models = {
        'main.job': {
            'Meta': {'object_name': 'Job'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '8192'}),
            'experience': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'})
        }
    }

    complete_apps = ['main']
