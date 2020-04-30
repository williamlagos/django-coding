# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Outro'
        db.create_table(u'nexgyn_outro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'nexgyn', ['Outro'])

        # Adding model 'NomeProcedimento'
        db.create_table(u'nexgyn_nomeprocedimento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
        ))
        db.send_create_signal(u'nexgyn', ['NomeProcedimento'])

        # Adding model 'Procedimento'
        db.create_table(u'nexgyn_procedimento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
            ('resultado', self.gf('django.db.models.fields.TextField')(default='')),
            ('renovar', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'nexgyn', ['Procedimento'])

        # Adding M2M table for field nome on 'Procedimento'
        m2m_table_name = db.shorten_name(u'nexgyn_procedimento_nome')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('procedimento', models.ForeignKey(orm[u'nexgyn.procedimento'], null=False)),
            ('nomeprocedimento', models.ForeignKey(orm[u'nexgyn.nomeprocedimento'], null=False))
        ))
        db.create_unique(m2m_table_name, ['procedimento_id', 'nomeprocedimento_id'])

        # Adding model 'Menstruacao'
        db.create_table(u'nexgyn_menstruacao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('menarca', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mensreg', self.gf('django.db.models.fields.BooleanField')()),
            ('mensregdiasl', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mensregdiasd', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mensirregdiasl', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mensirregdiasd', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('trocas', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('menopausa', self.gf('django.db.models.fields.IntegerField')(default=50)),
        ))
        db.send_create_signal(u'nexgyn', ['Menstruacao'])

        # Adding model 'Antecedente'
        db.create_table(u'nexgyn_antecedente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('diabetes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hipertensao', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('asma', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rubeola', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gesta', self.gf('django.db.models.fields.DateTimeField')(default=False)),
            ('para', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('parto', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ces', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('RN', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rubeola_igg', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rubeola_igm', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('toxo_igg1', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('toxo_igg2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('toxo_igm1', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('toxo_igm2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('citomegalovirus_igg1', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('citomegalovirus_igg2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('citomegalovirus_igm1', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('citomegalovirus_igm2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('HIV', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('HCV', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('VDRL', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('TSH', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('VAT', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('HbsAg', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'nexgyn', ['Antecedente'])

        # Adding M2M table for field outros on 'Antecedente'
        m2m_table_name = db.shorten_name(u'nexgyn_antecedente_outros')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('antecedente', models.ForeignKey(orm[u'nexgyn.antecedente'], null=False)),
            ('outro', models.ForeignKey(orm[u'nexgyn.outro'], null=False))
        ))
        db.create_unique(m2m_table_name, ['antecedente_id', 'outro_id'])

        # Adding model 'Atividade'
        db.create_table(u'nexgyn_atividade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cancermama', self.gf('django.db.models.fields.BooleanField')()),
            ('cancermamapar', self.gf('django.db.models.fields.TextField')(default='')),
            ('cancerutero', self.gf('django.db.models.fields.BooleanField')()),
            ('canceruteropar', self.gf('django.db.models.fields.TextField')(default='')),
            ('diabetes', self.gf('django.db.models.fields.BooleanField')()),
            ('diabetespar', self.gf('django.db.models.fields.TextField')(default='')),
            ('hipertensao', self.gf('django.db.models.fields.BooleanField')()),
            ('hipertensaopar', self.gf('django.db.models.fields.TextField')(default='')),
            ('outros', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'nexgyn', ['Atividade'])

        # Adding model 'TabelaAnomalia'
        db.create_table(u'nexgyn_tabelaanomalia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('DEPUNTI', self.gf('django.db.models.fields.BooleanField')()),
            ('LACER', self.gf('django.db.models.fields.BooleanField')()),
            ('FTRAN', self.gf('django.db.models.fields.BooleanField')()),
            ('CNABOTH', self.gf('django.db.models.fields.BooleanField')()),
            ('ENDOMET', self.gf('django.db.models.fields.BooleanField')()),
            ('EROSAO', self.gf('django.db.models.fields.BooleanField')()),
            ('POLIPO', self.gf('django.db.models.fields.BooleanField')()),
            ('QUERATO', self.gf('django.db.models.fields.BooleanField')()),
            ('JECZ', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('NTZ', self.gf('django.db.models.fields.BooleanField')()),
            ('INMUDA', self.gf('django.db.models.fields.BooleanField')()),
            ('MOSAICO', self.gf('django.db.models.fields.BooleanField')()),
            ('EPBRFINO', self.gf('django.db.models.fields.BooleanField')()),
            ('EPBESPES', self.gf('django.db.models.fields.BooleanField')()),
            ('ORGLESP', self.gf('django.db.models.fields.BooleanField')()),
            ('VASO', self.gf('django.db.models.fields.BooleanField')()),
            ('COLPITE', self.gf('django.db.models.fields.BooleanField')()),
            ('VULVA_HPV', self.gf('django.db.models.fields.BooleanField')()),
            ('VULVA_HERPES', self.gf('django.db.models.fields.BooleanField')()),
            ('VULVA_VULVITE', self.gf('django.db.models.fields.BooleanField')()),
            ('VULVA_LEUCO', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'nexgyn', ['TabelaAnomalia'])

        # Adding model 'TabelaMamaria'
        db.create_table(u'nexgyn_tabelamamaria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('MAMAD_TU_QSE', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAD_TU_QSI', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAD_TU_QIE', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAD_TU_QII', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAD_CISTO_QSE', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAD_CISTO_QSI', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAD_CISTO_QIE', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAD_CISTO_QII', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAE_TU_QSE', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAE_TU_QSI', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAE_TU_QIE', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAE_TU_QII', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAE_CISTO_QSE', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAE_CISTO_QSI', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAE_CISTO_QIE', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('MAMAE_CISTO_QII', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'nexgyn', ['TabelaMamaria'])

        # Adding model 'TabelaGinecologica'
        db.create_table(u'nexgyn_tabelaginecologica', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
            ('ut', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('desc', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ap', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ll', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mioma', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mioma11', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mioma12', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mioma21', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mioma22', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mioma3', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cisto', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('reto', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cistoovd', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cistoove', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tuovd', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tuove', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('endo', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tuoutros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('trompae', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('trompad', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('utoutros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('anomalias', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nexgyn.TabelaAnomalia'])),
            ('mama', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nexgyn.TabelaMamaria'])),
        ))
        db.send_create_signal(u'nexgyn', ['TabelaGinecologica'])

        # Adding model 'Obstetrico'
        db.create_table(u'nexgyn_obstetrico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('DUM', self.gf('django.db.models.fields.DateTimeField')()),
            ('NGest', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('HEPATITEB', self.gf('django.db.models.fields.BooleanField')()),
            ('LUES', self.gf('django.db.models.fields.BooleanField')()),
            ('TOXO', self.gf('django.db.models.fields.BooleanField')()),
            ('RUBEOLANEG', self.gf('django.db.models.fields.BooleanField')()),
            ('VAT', self.gf('django.db.models.fields.BooleanField')()),
            ('PLACENTA', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'nexgyn', ['Obstetrico'])


    def backwards(self, orm):
        # Deleting model 'Outro'
        db.delete_table(u'nexgyn_outro')

        # Deleting model 'NomeProcedimento'
        db.delete_table(u'nexgyn_nomeprocedimento')

        # Deleting model 'Procedimento'
        db.delete_table(u'nexgyn_procedimento')

        # Removing M2M table for field nome on 'Procedimento'
        db.delete_table(db.shorten_name(u'nexgyn_procedimento_nome'))

        # Deleting model 'Menstruacao'
        db.delete_table(u'nexgyn_menstruacao')

        # Deleting model 'Antecedente'
        db.delete_table(u'nexgyn_antecedente')

        # Removing M2M table for field outros on 'Antecedente'
        db.delete_table(db.shorten_name(u'nexgyn_antecedente_outros'))

        # Deleting model 'Atividade'
        db.delete_table(u'nexgyn_atividade')

        # Deleting model 'TabelaAnomalia'
        db.delete_table(u'nexgyn_tabelaanomalia')

        # Deleting model 'TabelaMamaria'
        db.delete_table(u'nexgyn_tabelamamaria')

        # Deleting model 'TabelaGinecologica'
        db.delete_table(u'nexgyn_tabelaginecologica')

        # Deleting model 'Obstetrico'
        db.delete_table(u'nexgyn_obstetrico')


    models = {
        u'nexgyn.antecedente': {
            'HCV': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'HIV': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'HbsAg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'Antecedente'},
            'RN': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'TSH': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'VAT': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'VDRL': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'asma': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'citomegalovirus_igg1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'citomegalovirus_igg2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'citomegalovirus_igm1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'citomegalovirus_igm2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diabetes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gesta': ('django.db.models.fields.DateTimeField', [], {'default': 'False'}),
            'hipertensao': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outros': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nexgyn.Outro']", 'symmetrical': 'False'}),
            'para': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rubeola': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rubeola_igg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rubeola_igm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'toxo_igg1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'toxo_igg2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'toxo_igm1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'toxo_igm2': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'nexgyn.atividade': {
            'Meta': {'object_name': 'Atividade'},
            'cancermama': ('django.db.models.fields.BooleanField', [], {}),
            'cancermamapar': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'cancerutero': ('django.db.models.fields.BooleanField', [], {}),
            'canceruteropar': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'diabetes': ('django.db.models.fields.BooleanField', [], {}),
            'diabetespar': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'hipertensao': ('django.db.models.fields.BooleanField', [], {}),
            'hipertensaopar': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outros': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'nexgyn.menstruacao': {
            'Meta': {'object_name': 'Menstruacao'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menarca': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'menopausa': ('django.db.models.fields.IntegerField', [], {'default': '50'}),
            'mensirregdiasd': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mensirregdiasl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mensreg': ('django.db.models.fields.BooleanField', [], {}),
            'mensregdiasd': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mensregdiasl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'trocas': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        },
        u'nexgyn.nomeprocedimento': {
            'Meta': {'object_name': 'NomeProcedimento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'nexgyn.obstetrico': {
            'DUM': ('django.db.models.fields.DateTimeField', [], {}),
            'HEPATITEB': ('django.db.models.fields.BooleanField', [], {}),
            'LUES': ('django.db.models.fields.BooleanField', [], {}),
            'Meta': {'object_name': 'Obstetrico'},
            'NGest': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'PLACENTA': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'RUBEOLANEG': ('django.db.models.fields.BooleanField', [], {}),
            'TOXO': ('django.db.models.fields.BooleanField', [], {}),
            'VAT': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'nexgyn.outro': {
            'Meta': {'object_name': 'Outro'},
            'descricao': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'nexgyn.procedimento': {
            'Meta': {'object_name': 'Procedimento'},
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nexgyn.NomeProcedimento']", 'symmetrical': 'False'}),
            'renovar': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resultado': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'nexgyn.tabelaanomalia': {
            'CNABOTH': ('django.db.models.fields.BooleanField', [], {}),
            'COLPITE': ('django.db.models.fields.BooleanField', [], {}),
            'DEPUNTI': ('django.db.models.fields.BooleanField', [], {}),
            'ENDOMET': ('django.db.models.fields.BooleanField', [], {}),
            'EPBESPES': ('django.db.models.fields.BooleanField', [], {}),
            'EPBRFINO': ('django.db.models.fields.BooleanField', [], {}),
            'EROSAO': ('django.db.models.fields.BooleanField', [], {}),
            'FTRAN': ('django.db.models.fields.BooleanField', [], {}),
            'INMUDA': ('django.db.models.fields.BooleanField', [], {}),
            'JECZ': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'LACER': ('django.db.models.fields.BooleanField', [], {}),
            'MOSAICO': ('django.db.models.fields.BooleanField', [], {}),
            'Meta': {'object_name': 'TabelaAnomalia'},
            'NTZ': ('django.db.models.fields.BooleanField', [], {}),
            'ORGLESP': ('django.db.models.fields.BooleanField', [], {}),
            'POLIPO': ('django.db.models.fields.BooleanField', [], {}),
            'QUERATO': ('django.db.models.fields.BooleanField', [], {}),
            'VASO': ('django.db.models.fields.BooleanField', [], {}),
            'VULVA_HERPES': ('django.db.models.fields.BooleanField', [], {}),
            'VULVA_HPV': ('django.db.models.fields.BooleanField', [], {}),
            'VULVA_LEUCO': ('django.db.models.fields.BooleanField', [], {}),
            'VULVA_VULVITE': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'nexgyn.tabelaginecologica': {
            'Meta': {'object_name': 'TabelaGinecologica'},
            'anomalias': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nexgyn.TabelaAnomalia']"}),
            'ap': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cisto': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cistoovd': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cistoove': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'comp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'desc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'endo': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'll': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mama': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nexgyn.TabelaMamaria']"}),
            'mioma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mioma11': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mioma12': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mioma21': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mioma22': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mioma3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reto': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'trompad': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'trompae': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tuoutros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tuovd': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tuove': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ut': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'utoutros': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'nexgyn.tabelamamaria': {
            'MAMAD_CISTO_QIE': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAD_CISTO_QII': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAD_CISTO_QSE': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAD_CISTO_QSI': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAD_TU_QIE': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAD_TU_QII': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAD_TU_QSE': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAD_TU_QSI': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAE_CISTO_QIE': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAE_CISTO_QII': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAE_CISTO_QSE': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAE_CISTO_QSI': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAE_TU_QIE': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAE_TU_QII': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAE_TU_QSE': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'MAMAE_TU_QSI': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Meta': {'object_name': 'TabelaMamaria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['nexgyn']