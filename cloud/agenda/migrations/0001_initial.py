# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lembrete'
        db.create_table(u'agenda_lembrete', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('texto', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'agenda', ['Lembrete'])

        # Adding model 'Prescricao'
        db.create_table(u'agenda_prescricao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'agenda', ['Prescricao'])

        # Adding model 'Telefone'
        db.create_table(u'agenda_telefone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(default='51', max_length=2)),
            ('numero', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
        ))
        db.send_create_signal(u'agenda', ['Telefone'])

        # Adding model 'Pessoa'
        db.create_table(u'agenda_pessoa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('sobrenome', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('nascimento', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('apartamento', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('cidade', self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'agenda', ['Pessoa'])

        # Adding M2M table for field telefones on 'Pessoa'
        m2m_table_name = db.shorten_name(u'agenda_pessoa_telefones')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pessoa', models.ForeignKey(orm[u'agenda.pessoa'], null=False)),
            ('telefone', models.ForeignKey(orm[u'agenda.telefone'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pessoa_id', 'telefone_id'])

        # Adding model 'Paciente'
        db.create_table(u'agenda_paciente', (
            (u'pessoa_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['agenda.Pessoa'], unique=True, primary_key=True)),
            ('antecedentes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nexgyn.Antecedente'], null=True, blank=True)),
            ('gesta', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('para', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('idadeprimeiro', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('parto', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('cesaria', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('abe', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('abp', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('contracepcao', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('curetagem', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('observacoes', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('gruposanguineo', self.gf('django.db.models.fields.CharField')(default='', max_length=5, null=True, blank=True)),
            ('fatorrh', self.gf('django.db.models.fields.CharField')(default='+', max_length=5, null=True, blank=True)),
        ))
        db.send_create_signal(u'agenda', ['Paciente'])

        # Adding M2M table for field procedimentos on 'Paciente'
        m2m_table_name = db.shorten_name(u'agenda_paciente_procedimentos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('paciente', models.ForeignKey(orm[u'agenda.paciente'], null=False)),
            ('procedimento', models.ForeignKey(orm[u'nexgyn.procedimento'], null=False))
        ))
        db.create_unique(m2m_table_name, ['paciente_id', 'procedimento_id'])

        # Adding model 'Historico'
        db.create_table(u'agenda_historico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('paciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agenda.Paciente'])),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
            ('DUM', self.gf('django.db.models.fields.DateTimeField')()),
            ('TA', self.gf('django.db.models.fields.IntegerField')()),
            ('Peso', self.gf('django.db.models.fields.FloatField')()),
            ('Queixas', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('HDiag', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Conduta', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'agenda', ['Historico'])

        # Adding model 'Imagem'
        db.create_table(u'agenda_imagem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('paciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agenda.Paciente'])),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'agenda', ['Imagem'])

        # Adding model 'Anexo'
        db.create_table(u'agenda_anexo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('paciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agenda.Paciente'])),
            ('anexo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'agenda', ['Anexo'])

        # Adding model 'Exame'
        db.create_table(u'agenda_exame', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('paciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agenda.Paciente'])),
            ('iniciogest', self.gf('django.db.models.fields.DateTimeField')()),
            ('IG', self.gf('django.db.models.fields.IntegerField')()),
            ('TAmax', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('TAmin', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('Peso', self.gf('django.db.models.fields.FloatField')(default=0.1, null=True, blank=True)),
            ('DBP', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('PC', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('PA', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('CF', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('observacoes', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'agenda', ['Exame'])


    def backwards(self, orm):
        # Deleting model 'Lembrete'
        db.delete_table(u'agenda_lembrete')

        # Deleting model 'Prescricao'
        db.delete_table(u'agenda_prescricao')

        # Deleting model 'Telefone'
        db.delete_table(u'agenda_telefone')

        # Deleting model 'Pessoa'
        db.delete_table(u'agenda_pessoa')

        # Removing M2M table for field telefones on 'Pessoa'
        db.delete_table(db.shorten_name(u'agenda_pessoa_telefones'))

        # Deleting model 'Paciente'
        db.delete_table(u'agenda_paciente')

        # Removing M2M table for field procedimentos on 'Paciente'
        db.delete_table(db.shorten_name(u'agenda_paciente_procedimentos'))

        # Deleting model 'Historico'
        db.delete_table(u'agenda_historico')

        # Deleting model 'Imagem'
        db.delete_table(u'agenda_imagem')

        # Deleting model 'Anexo'
        db.delete_table(u'agenda_anexo')

        # Deleting model 'Exame'
        db.delete_table(u'agenda_exame')


    models = {
        u'agenda.anexo': {
            'Meta': {'object_name': 'Anexo'},
            'anexo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agenda.Paciente']"})
        },
        u'agenda.exame': {
            'CF': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'DBP': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'IG': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'Exame'},
            'PA': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'PC': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Peso': ('django.db.models.fields.FloatField', [], {'default': '0.1', 'null': 'True', 'blank': 'True'}),
            'TAmax': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'TAmin': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iniciogest': ('django.db.models.fields.DateTimeField', [], {}),
            'observacoes': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agenda.Paciente']"})
        },
        u'agenda.historico': {
            'Conduta': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'DUM': ('django.db.models.fields.DateTimeField', [], {}),
            'HDiag': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'Historico'},
            'Peso': ('django.db.models.fields.FloatField', [], {}),
            'Queixas': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'TA': ('django.db.models.fields.IntegerField', [], {}),
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agenda.Paciente']"})
        },
        u'agenda.imagem': {
            'Meta': {'object_name': 'Imagem'},
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agenda.Paciente']"})
        },
        u'agenda.lembrete': {
            'Meta': {'object_name': 'Lembrete'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'agenda.paciente': {
            'Meta': {'object_name': 'Paciente', '_ormbases': [u'agenda.Pessoa']},
            'abe': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'abp': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'antecedentes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nexgyn.Antecedente']", 'null': 'True', 'blank': 'True'}),
            'cesaria': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'contracepcao': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'curetagem': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'fatorrh': ('django.db.models.fields.CharField', [], {'default': "'+'", 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'gesta': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'gruposanguineo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'idadeprimeiro': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'observacoes': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'para': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'parto': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'pessoa_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['agenda.Pessoa']", 'unique': 'True', 'primary_key': 'True'}),
            'procedimentos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['nexgyn.Procedimento']", 'null': 'True', 'blank': 'True'})
        },
        u'agenda.pessoa': {
            'Meta': {'object_name': 'Pessoa'},
            'apartamento': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nascimento': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sobrenome': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'telefones': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['agenda.Telefone']", 'null': 'True', 'blank': 'True'})
        },
        u'agenda.prescricao': {
            'Meta': {'object_name': 'Prescricao'},
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'agenda.telefone': {
            'Meta': {'object_name': 'Telefone'},
            'codigo': ('django.db.models.fields.CharField', [], {'default': "'51'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        },
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
        u'nexgyn.nomeprocedimento': {
            'Meta': {'object_name': 'NomeProcedimento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
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
        }
    }

    complete_apps = ['agenda']