# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FitTest'
        db.create_table('fittest_fittest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('switch_kicks', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('power_jacks', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('power_knees', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('power_jumps', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('globe_jumps', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('suicide_jumps', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('push_up_jacks', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('low_plank_oblique', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('fittest', ['FitTest'])


    def backwards(self, orm):
        
        # Deleting model 'FitTest'
        db.delete_table('fittest_fittest')


    models = {
        'fittest.fittest': {
            'Meta': {'ordering': "('date_created',)", 'object_name': 'FitTest'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'globe_jumps': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low_plank_oblique': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'power_jacks': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'power_jumps': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'power_knees': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'push_up_jacks': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'suicide_jumps': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'switch_kicks': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['fittest']
