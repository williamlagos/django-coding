# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PesoDBP'
        db.create_table(u'calculo_pesodbp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('DBP', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('PA', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('Peso', self.gf('django.db.models.fields.FloatField')(default=0.1)),
        ))
        db.send_create_signal(u'calculo', ['PesoDBP'])

        # Adding model 'PesoCF'
        db.create_table(u'calculo_pesocf', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('CF', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('PA', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('Peso', self.gf('django.db.models.fields.FloatField')(default=0.1)),
        ))
        db.send_create_signal(u'calculo', ['PesoCF'])

        # Adding model 'IdadeGestacional'
        db.create_table(u'calculo_idadegestacional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('IG', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('Data', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'calculo', ['IdadeGestacional'])


    def backwards(self, orm):
        # Deleting model 'PesoDBP'
        db.delete_table(u'calculo_pesodbp')

        # Deleting model 'PesoCF'
        db.delete_table(u'calculo_pesocf')

        # Deleting model 'IdadeGestacional'
        db.delete_table(u'calculo_idadegestacional')


    models = {
        u'calculo.idadegestacional': {
            'Data': ('django.db.models.fields.DateTimeField', [], {}),
            'IG': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Meta': {'object_name': 'IdadeGestacional'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calculo.pesocf': {
            'CF': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Meta': {'object_name': 'PesoCF'},
            'PA': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Peso': ('django.db.models.fields.FloatField', [], {'default': '0.1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'calculo.pesodbp': {
            'DBP': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Meta': {'object_name': 'PesoDBP'},
            'PA': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Peso': ('django.db.models.fields.FloatField', [], {'default': '0.1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['calculo']