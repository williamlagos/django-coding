import xadmin
from models import *
from django.shortcuts import HttpResponseRedirect as redirect


def pdf_version(modeladmin, request, queryset):
    url = '/relatorio/?pks=' + ','.join([str(q.pk) for q in queryset])
    return redirect(url)


class LembreteAdmin(object):
    list_display = Lembrete._meta.get_all_field_names()


class PrescricaoAdmin(object):
    actions = [pdf_version]
    list_display = Prescricao._meta.get_all_field_names()


class PacienteAdmin(object):
    list_display = Paciente._meta.get_all_field_names()


class PessoaAdmin(object):
    list_display = Pessoa._meta.get_all_field_names()


class ImagemAdmin(object):
    list_display = ['Paciente','Imagem']
    def Paciente(self,obj):
        return obj.paciente
    def Imagem(self,obj):
        print obj.foto.url
        if obj.foto:
            return '<img src="%s" width="200px">' % obj.foto.url
        return ''
    Imagem.allow_tags = True


class AnexoAdmin(object):
    list_display = Anexo._meta.get_all_field_names()


class ExameAdmin(object):
    list_display = Exame._meta.get_all_field_names()


class TelefoneAdmin(object):
    list_display = Telefone._meta.get_all_field_names()


class HistoricoAdmin(object):
    list_display = Historico._meta.get_all_field_names()


class ObstetricoAdmin(object):
    list_display = Obstetrico._meta.get_all_field_names()


class ProcedimentoAdmin(object):
    list_display = Procedimento._meta.get_all_field_names()

xadmin.site.register(Lembrete, LembreteAdmin)
xadmin.site.register(Anexo, AnexoAdmin)
xadmin.site.register(Prescricao, PrescricaoAdmin)
xadmin.site.register(Paciente, PacienteAdmin)
xadmin.site.register(Pessoa, PessoaAdmin)
xadmin.site.register(Imagem, ImagemAdmin)
xadmin.site.register(Exame, ExameAdmin)
xadmin.site.register(Telefone, TelefoneAdmin)
xadmin.site.register(Historico, HistoricoAdmin)
xadmin.site.register(Obstetrico, ObstetricoAdmin)
xadmin.site.register(Procedimento, ProcedimentoAdmin)
