#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db.models import *
# Create your models here.


class PesoDBP(Model):
    DBP = IntegerField('Diâmetro', default=0, null=True, blank=True)
    PA = IntegerField('Perímetro Abdominal', default=0, null=True, blank=True)
    Peso = FloatField(default=0.1, null=True, blank=True)

    class Meta:
        verbose_name = 'Diâmetro Biparietal'
        verbose_name_plural = 'Diâmetros Biparietais'

    def __unicode__(self):
        if self.DBP is not None:
            return self.DBP
        else:
            return 'Sem Diâmetro Biparietal'


class PesoCF(Model):
    CF = FloatField('Comprimento Femoral', default=0, null=True, blank=True)
    PA_40 = IntegerField('4,0', default=0, null=True, blank=True)
    PA_41 = IntegerField('4,1', default=0, null=True, blank=True)
    PA_42 = IntegerField('4,2', default=0, null=True, blank=True)
    PA_43 = IntegerField('4,3', default=0, null=True, blank=True)
    PA_44 = IntegerField('4,4', default=0, null=True, blank=True)
    PA_45 = IntegerField('4,5', default=0, null=True, blank=True)
    PA_46 = IntegerField('4,6', default=0, null=True, blank=True)
    PA_47 = IntegerField('4,7', default=0, null=True, blank=True)
    PA_48 = IntegerField('4,8', default=0, null=True, blank=True)
    PA_49 = IntegerField('4,9', default=0, null=True, blank=True)
    PA_50 = IntegerField('5,0', default=0, null=True, blank=True)
    PA_51 = IntegerField('5,1', default=0, null=True, blank=True)
    PA_52 = IntegerField('5,2', default=0, null=True, blank=True)
    PA_53 = IntegerField('5,3', default=0, null=True, blank=True)
    PA_54 = IntegerField('5,4', default=0, null=True, blank=True)
    PA_55 = IntegerField('5,5', default=0, null=True, blank=True)
    PA_56 = IntegerField('5,6', default=0, null=True, blank=True)
    PA_57 = IntegerField('5,7', default=0, null=True, blank=True)
    PA_58 = IntegerField('5,8', default=0, null=True, blank=True)
    PA_59 = IntegerField('5,9', default=0, null=True, blank=True)
    PA_60 = IntegerField('6,0', default=0, null=True, blank=True)
    PA_61 = IntegerField('6,1', default=0, null=True, blank=True)
    PA_62 = IntegerField('6,2', default=0, null=True, blank=True)
    PA_63 = IntegerField('6,3', default=0, null=True, blank=True)
    PA_64 = IntegerField('6,4', default=0, null=True, blank=True)
    PA_65 = IntegerField('6,5', default=0, null=True, blank=True)
    PA_66 = IntegerField('6,6', default=0, null=True, blank=True)
    PA_67 = IntegerField('6,7', default=0, null=True, blank=True)
    PA_68 = IntegerField('6,8', default=0, null=True, blank=True)
    PA_69 = IntegerField('6,9', default=0, null=True, blank=True)
    PA_70 = IntegerField('7,0', default=0, null=True, blank=True)
    PA_71 = IntegerField('7,1', default=0, null=True, blank=True)
    PA_72 = IntegerField('7,2', default=0, null=True, blank=True)
    PA_73 = IntegerField('7,3', default=0, null=True, blank=True)
    PA_74 = IntegerField('7,4', default=0, null=True, blank=True)
    PA_75 = IntegerField('7,5', default=0, null=True, blank=True)
    PA_76 = IntegerField('7,6', default=0, null=True, blank=True)
    PA_77 = IntegerField('7,7', default=0, null=True, blank=True)
    PA_78 = IntegerField('7,8', default=0, null=True, blank=True)
    PA_79 = IntegerField('7,9', default=0, null=True, blank=True)
    PA_80 = IntegerField('8,0', default=0, null=True, blank=True)
    PA_81 = IntegerField('8,1', default=0, null=True, blank=True)
    PA_82 = IntegerField('8,2', default=0, null=True, blank=True)
    PA_83 = IntegerField('8,3', default=0, null=True, blank=True)

    class Meta:
        verbose_name = 'Comprimento Femoral'
        verbose_name_plural = 'Comprimentos Femorais'

    def __unicode__(self):
        if self.CF is not None:
            return self.CF
        else:
            return 'Sem Comprimento Femoral'


class IdadeGestacional(Model):
    IG = IntegerField('Idade Gestacional', default=0, null=True, blank=True)
    Data = DateTimeField('Data inicial da Gestação', null=True, blank=True)

    class Meta:
        verbose_name = 'Idade Gestacional'
        verbose_name_plural = 'Idades Gestacionais'

    def __unicode__(self):
        if self.IG is not None:
            return self.IG
        else:
            return 'Sem Idade Gestacional'
