#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db.models import *

class Outro(Model):
    nome = CharField(max_length=100, null=True, blank=True)
    descricao = TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Outro Antecedente'
        verbose_name_plural = 'Outros Antecedentes'

    def __unicode__(self):
        if self.nome is not None:
            return self.nome
        else:
            return 'Sem Nome'


class Menstruacao(Model):
    menarca = IntegerField(default=0, null=True, blank=True)
    mensreg = BooleanField(default=False)
    mensregdiasl = IntegerField(default=0, null=True, blank=True)
    mensregdiasd = IntegerField(default=0, null=True, blank=True)
    mensirregdiasl = IntegerField(default=0, null=True, blank=True)
    mensirregdiasd = IntegerField(default=0, null=True, blank=True)
    trocas = CharField(default='', max_length=50, null=True, blank=True)
    menopausa = IntegerField(default=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Menstruação'
        verbose_name_plural = 'Menstruações'

    def __unicode__(self):
        return 'Tabela de Menstruação'


class Antecedente(Model):
    diabetes = BooleanField('Diabetes', default=False)
    hipertensao = BooleanField('Hipertensão', default=False)
    asma = BooleanField('Asma', default=False)
    rubeola = BooleanField('Rubéola', default=False)
    gesta = DateTimeField('Gestação', default=False, null=True, blank=True)
    para = BooleanField('Parada', default=False)
    parto = BooleanField('Parto', default=False)
    ces = BooleanField('Cesárea', default=False)
    RN = BooleanField(default=False)
    rubeola_igg = BooleanField('Rubéola IGG', default=False)
    rubeola_igm = BooleanField('Rubéola IGM', default=False)
    toxo_igg1 = BooleanField('Toxo IGG 1', default=False)
    toxo_igg2 = BooleanField('Toxo IGG 2', default=False)
    toxo_igm1 = BooleanField('Toxo IGM 1', default=False)
    toxo_igm2 = BooleanField('Toxo IGM 2', default=False)
    citomegalovirus_igg1 = BooleanField('Citomegalovirus IGG 1', default=False)
    citomegalovirus_igg2 = BooleanField('Citomegalovirus IGG 2', default=False)
    citomegalovirus_igm1 = BooleanField('Citomegalovirus IGM 1', default=False)
    citomegalovirus_igm2 = BooleanField('Citomegalovirus IGM 2', default=False)
    HIV = BooleanField(default=False)
    HCV = BooleanField(default=False)
    VDRL = BooleanField(default=False)
    TSH = BooleanField(default=False)
    VAT = BooleanField(default=False)
    HbsAg = BooleanField(default=False)
    outros = ManyToManyField(Outro, verbose_name='Outros',
                             null=True, blank=True)

    class Meta:
        verbose_name = 'Antecedente'
        verbose_name_plural = 'Antecedentes'

    def __unicode__(self):
        return 'Tabela de Antecedentes'


class Atividade(Model):
    cancermama = BooleanField('Câncer de Mama', default=False)
    cancermamapar = TextField('Parentes com Câncer de Mama',
                              default='', null=True, blank=True)
    cancerutero = BooleanField('Câncer de Útero', default=False)
    canceruteropar = TextField('Parentes com Câncer de Útero',
                               default='', null=True, blank=True)
    diabetes = BooleanField('Diabetes', default=False)
    diabetespar = TextField('Parentes com Diabetes',
                            default='', null=True, blank=True)
    hipertensao = BooleanField('Hipertensão', default=False)
    hipertensaopar = TextField('Parentes com Hipertensão',
                               default='', null=True, blank=True)
    outros = TextField('Outros', default='', null=True, blank=True)

    class Meta:
        verbose_name = 'Doença'
        verbose_name_plural = 'Doenças'

    def __unicode__(self):
        return 'Tabela de Doenças'


class TabelaAnomalia(Model):
    DEPUNTI = BooleanField(default=False)
    LACER = BooleanField(default=False)
    FTRAN = BooleanField(default=False)
    CNABOTH = BooleanField(default=False)
    ENDOMET = BooleanField(default=False)
    EROSAO = BooleanField(default=False)
    POLIPO = BooleanField(default=False)
    QUERATO = BooleanField(default=False)
    JECZ = IntegerField(default=0, null=True, blank=True)
    NTZ = BooleanField(default=False)
    INMUDA = BooleanField(default=False)
    MOSAICO = BooleanField(default=False)
    EPBRFINO = BooleanField(default=False)
    EPBESPES = BooleanField(default=False)
    ORGLESP = BooleanField(default=False)
    VASO = BooleanField(default=False)
    COLPITE = BooleanField(default=False)
    VULVA_HPV = BooleanField(default=False)
    VULVA_HERPES = BooleanField(default=False)
    VULVA_VULVITE = BooleanField(default=False)
    VULVA_LEUCO = BooleanField(default=False)

    class Meta:
        verbose_name = 'Anomalia'
        verbose_name_plural = 'Anomalias'

    def __unicode__(self):
        return 'Tipo de Anomalia'


class TabelaMamaria(Model):
    MAMAD_TU_QSE = IntegerField(default=0, null=True, blank=True)
    MAMAD_TU_QSI = IntegerField(default=0, null=True, blank=True)
    MAMAD_TU_QIE = IntegerField(default=0, null=True, blank=True)
    MAMAD_TU_QII = IntegerField(default=0, null=True, blank=True)
    MAMAD_CISTO_QSE = IntegerField(default=0, null=True, blank=True)
    MAMAD_CISTO_QSI = IntegerField(default=0, null=True, blank=True)
    MAMAD_CISTO_QIE = IntegerField(default=0, null=True, blank=True)
    MAMAD_CISTO_QII = IntegerField(default=0, null=True, blank=True)
    MAMAE_TU_QSE = IntegerField(default=0, null=True, blank=True)
    MAMAE_TU_QSI = IntegerField(default=0, null=True, blank=True)
    MAMAE_TU_QIE = IntegerField(default=0, null=True, blank=True)
    MAMAE_TU_QII = IntegerField(default=0, null=True, blank=True)
    MAMAE_CISTO_QSE = IntegerField(default=0, null=True, blank=True)
    MAMAE_CISTO_QSI = IntegerField(default=0, null=True, blank=True)
    MAMAE_CISTO_QIE = IntegerField(default=0, null=True, blank=True)
    MAMAE_CISTO_QII = IntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = 'Tabela Mamária'
        verbose_name_plural = 'Tabelas Mamárias'

    def __unicode__(self):
        return 'Tabela Mamária'


class TabelaGinecologica(Model):
    data = DateTimeField('Data', null=True, blank=True)
    ut = IntegerField('Útero', default=0, null=True, blank=True)
    desc = IntegerField('Descrição', default=0, null=True, blank=True)
    comp = IntegerField('Comprimento', default=0, null=True, blank=True)
    ap = IntegerField('AP', default=0, null=True, blank=True)
    ll = IntegerField('LL', default=0, null=True, blank=True)
    mioma = IntegerField('Mioma', default=0, null=True, blank=True)
    mioma11 = IntegerField('Mioma 11', default=0, null=True, blank=True)
    mioma12 = IntegerField('Mioma 12', default=0, null=True, blank=True)
    mioma21 = IntegerField('Mioma 21', default=0, null=True, blank=True)
    mioma22 = IntegerField('Mioma 22', default=0, null=True, blank=True)
    mioma3 = IntegerField('Mioma 3', default=0, null=True, blank=True)
    cisto = IntegerField('Cisto', default=0, null=True, blank=True)
    reto = IntegerField('Reto', default=0, null=True, blank=True)
    cistoovd = IntegerField('Cisto Ovário Direita',
                            default=0, null=True, blank=True)
    cistoove = IntegerField('Cisto Ovário Esquerda',
                            default=0, null=True, blank=True)
    tuovd = IntegerField('TU Ovário Direito', default=0, null=True, blank=True)
    tuove = IntegerField('TU Ovário Esquerdo',
                         default=0, null=True, blank=True)
    endo = IntegerField('Endoscopia', default=0, null=True, blank=True)
    tuoutros = IntegerField('TU Outros', default=0, null=True, blank=True)
    trompae = IntegerField('Trompa Esquerda', default=0, null=True, blank=True)
    trompad = IntegerField('Trompa Direita', default=0, null=True, blank=True)
    utoutros = IntegerField('Útero Outros', default=0, null=True, blank=True)
    anomalias = ForeignKey(TabelaAnomalia, verbose_name='Anomalias',
                           null=True, blank=True)
    mama = ForeignKey(TabelaMamaria, verbose_name='Tabela Mamária',
                      null=True, blank=True)

    class Meta:
        verbose_name = 'Tabela Ginecológica'
        verbose_name_plural = 'Tabelas Ginecológicas'

    def __unicode__(self):
        return 'Tabela Ginecológica'
