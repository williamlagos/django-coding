import xadmin
from models import *


class MenstruacaoAdmin(object):
    list_display = Menstruacao._meta.get_all_field_names()


class AntecedenteAdmin(object):
    list_display = Antecedente._meta.get_all_field_names()


class OutroAdmin(object):
    list_display = Outro._meta.get_all_field_names()


class AtividadeAdmin(object):
    list_display = Atividade._meta.get_all_field_names()


class TabelaAnomaliaAdmin(object):
    list_display = TabelaAnomalia._meta.get_all_field_names()


class TabelaMamariaAdmin(object):
    list_display = TabelaMamaria._meta.get_all_field_names()


class TabelaGinecologicaAdmin(object):
    list_display = TabelaGinecologica._meta.get_all_field_names()

xadmin.site.register(Menstruacao, MenstruacaoAdmin)
xadmin.site.register(Antecedente, AntecedenteAdmin)
xadmin.site.register(Outro, OutroAdmin)
xadmin.site.register(Atividade, AtividadeAdmin)
xadmin.site.register(TabelaAnomalia, TabelaAnomaliaAdmin)
xadmin.site.register(TabelaMamaria, TabelaMamariaAdmin)
xadmin.site.register(TabelaGinecologica, TabelaGinecologicaAdmin)
