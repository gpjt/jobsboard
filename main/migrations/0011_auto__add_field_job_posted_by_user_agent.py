# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Job.posted_by_user_agent'
        db.add_column('main_job', 'posted_by_user_agent',
                      self.gf('django.db.models.fields.CharField')(default='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22', max_length=1024),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Job.posted_by_user_agent'
        db.delete_column('main_job', 'posted_by_user_agent')


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
            'posted_by_user_agent': ('django.db.models.fields.CharField', [], {'default': "'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22'", 'max_length': '1024'}),
            'posted_from_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'salary': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'spam': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'})
        },
        'main.retweeter': {
            'Meta': {'object_name': 'Retweeter'},
            'access_key': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'access_secret': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        }
    }

    complete_apps = ['main']