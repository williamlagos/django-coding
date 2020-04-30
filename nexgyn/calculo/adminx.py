import xadmin
from models import *


class PesoDBPAdmin(object):
    list_display = PesoDBP._meta.get_all_field_names()


class PesoCFAdmin(object):
    list_display = PesoCF._meta.get_all_field_names()


class IdadeGestacionalAdmin(object):
    list_display = IdadeGestacional._meta.get_all_field_names()

xadmin.site.register(PesoDBP, PesoDBPAdmin)
xadmin.site.register(PesoCF, PesoCFAdmin)
xadmin.site.register(IdadeGestacional, IdadeGestacionalAdmin)
