#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from django.db.models import *
from django_dropbox.storage import DropboxStorage
from nexgyn.models import *
from calculo.models import *

STORAGE = DropboxStorage()
# Create your models here.


class Lembrete(Model):
    titulo = CharField('Título', max_length=50, null=True, blank=True)
    texto = TextField('Descrição', null=True, blank=True)

    class Meta:
        verbose_name = 'Lembrete'
        verbose_name_plural = 'Lembretes'

    def __unicode__(self):
        if self.titulo is not None:
            return self.titulo
        else:
            return 'Sem Título'


class Prescricao(Model):
    titulo = CharField('Título', max_length=50, null=True, blank=True)
    descricao = TextField('Descrição', null=True, blank=True)
    data = DateTimeField('Data', null=True, blank=True)

    class Meta:
        verbose_name = 'Prescrição'
        verbose_name_plural = 'Prescrições'

    def __unicode__(self):
        if self.titulo is not None:
            return self.titulo
        else:
            return 'Sem Título'


class Telefone(Model):
    codigo = CharField('Código DDD', default='51',
                       max_length=2, null=True, blank=True)
    numero = CharField('Número', default='',
                       max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __unicode__(self):
        if self.numero is not None:
            return self.numero
        else:
            return 'Sem Número'


class Pessoa(Model):
    nome = CharField('Nome', max_length=50, null=True, blank=True)
    sobrenome = CharField('Sobrenome', max_length=50, null=True, blank=True)
    nascimento = DateTimeField('Data de Nascimento', null=True, blank=True)
    endereco = CharField('Endereço', max_length=100, null=True, blank=True)
    numero = IntegerField('Número', null=True, blank=True)
    apartamento = IntegerField('Apartamento', default=0, null=True, blank=True)
    cep = CharField('CEP', max_length=10, null=True, blank=True)
    cidade = CharField('Cidade', max_length=75, null=True, blank=True)
    telefones = ManyToManyField(Telefone, verbose_name='Telefones',
                                null=True, blank=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __unicode__(self):
        if self.nome is not None:
            if self.sobrenome is not None:
                return '%s %s' % (self.nome, self.sobrenome)
            else:
                return self.nome
        else:
            return 'Sem Nome'


class Paciente(Pessoa):
    #menstruacao = ForeignKey(Menstruacao)
    #atividadesfisicas = ForeignKey(Atividade)
    #exginecologista = ForeignKey(TabelaGinecologica)
    antecedentes = ForeignKey(Antecedente, verbose_name='Antecedentes',
                              null=True, blank=True)
    gesta = IntegerField('Gestação', default=0, null=True, blank=True)
    para = IntegerField('Parada', default=0, null=True, blank=True)
    idadeprimeiro = IntegerField('Idade do Primeiro',
                                 default=0, null=True, blank=True)
    parto = IntegerField('Parto', default=0, null=True, blank=True)
    cesaria = IntegerField('Cesárea', default=0, null=True, blank=True)
    abe = IntegerField('ABE', default=0, null=True, blank=True)
    abp = IntegerField('ABP', default=0, null=True, blank=True)
    contracepcao = IntegerField('Contracepção',
                                default=0, null=True, blank=True)
    curetagem = IntegerField('Curetagem', default=0, null=True, blank=True)
    observacoes = TextField('Observações', default='', null=True, blank=True)
    gruposanguineo = CharField('Grupo Sanguíneo', default='',
                               max_length=5, null=True, blank=True)
    fatorrh = CharField('Fator RH', default='+',
                        max_length=5, null=True, blank=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __unicode__(self):
        if self.nome is not None:
            if self.sobrenome is not None:
                return '%s %s' % (self.nome, self.sobrenome)
            else:
                return self.nome
        else:
            return 'Sem Nome'


class Historico(Model):
    paciente = ForeignKey(Paciente, null=True, blank=True)
    data = DateTimeField('Data', null=True, blank=True)
    DUM = DateTimeField(null=True, blank=True)
    TA = IntegerField(null=True, blank=True)
    Peso = FloatField(null=True, blank=True)
    Queixas = CharField(max_length=100, null=True, blank=True)
    HDiag = CharField('Diagnóstico', max_length=100, null=True, blank=True)
    Conduta = CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Histórico'
        verbose_name_plural = 'Históricos'

    def __unicode__(self):
        if self.data is not None:
            return self.data
        else:
            return 'Sem Data'


class Imagem(Model):
    paciente = ForeignKey(Paciente)
    foto = ImageField('Foto', upload_to='images', storage=STORAGE)

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __unicode__(self):
        if self.foto is not None:
            return self.foto
        else:
            return 'Sem Foto'


class Anexo(Model):
    paciente = ForeignKey(Paciente)
    anexo = FileField('Anexo', upload_to='archives', storage=STORAGE)

    class Meta:
        verbose_name = 'Anexo'
        verbose_name_plural = 'Anexos'

    def __unicode__(self):
        if self.anexo is not None:
            return self.anexo
        else:
            return 'Sem Anexo'


class Exame(Model):
    paciente = ForeignKey(Paciente, null=True, blank=True)
    iniciogest = DateTimeField('Início da Gestação', null=True, blank=True)
    IG = IntegerField('Idade Gestacional', null=True, blank=True)
    TAmax = IntegerField(default=0, null=True, blank=True)
    TAmin = IntegerField(default=0, null=True, blank=True)
    Peso = FloatField(default=0.1, null=True, blank=True)
    DBP = IntegerField('Diâmetro Biparietal', default=0, null=True, blank=True)
    PC = IntegerField(default=0, null=True, blank=True)
    PA = IntegerField('Perímetro Abdominal', default=0, null=True, blank=True)
    CF = IntegerField('Comprimento Femoral', default=0, null=True, blank=True)
    observacoes = TextField('Observações', default='', null=True, blank=True)

    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'

    def save(self):
        self.IG = ((datetime.now() - iniciogest).days) / 30
        self.Peso = PesoCF.objects.filter(CF=self.CF, PA=self.PA)[0].Peso
        super(Exame, self).save()

    def __unicode__(self):
        if self.iniciogest is not None:
            return self.iniciogest
        else:
            return 'Sem Data'


class Obstetrico(Model):
    paciente = ForeignKey(Paciente, null=True, blank=True)
    DUM = DateTimeField(null=True, blank=True)
    NGest = IntegerField('Número da Gestação',
                         default=0, null=True, blank=True)
    HEPATITEB = BooleanField('Hepatite B', default=False)
    LUES = BooleanField(default=False)
    TOXO = BooleanField(default=False)
    RUBEOLANEG = BooleanField('Rubéola Negativa', default=False)
    VAT = BooleanField(default=False)
    PLACENTA = IntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name = 'Obstétrico'
        verbose_name_plural = 'Obstétricos'

    def __unicode__(self):
        if self.DUM is not None:
            return self.DUM
        else:
            return 'Sem DUM'


class Procedimento(Model):
    paciente = ForeignKey(Paciente, null=True, blank=True)
    data = DateTimeField('Data', null=True, blank=True)
    resultado = TextField('Resultado', default='', null=True, blank=True)
    renovar = IntegerField('Renovação', default=0, null=True, blank=True)
    nome = CharField('Nome', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Procedimento'
        verbose_name_plural = 'Procedimentos'

    def __unicode__(self):
        if self.data is not None:
            return self.data
        else:
            return 'Sem Data'
