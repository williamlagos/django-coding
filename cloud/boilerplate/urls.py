import xadmin
xadmin.autodiscover()
from django.conf.urls import patterns, include, url
from nexgyn.views import RenovacaoView, ProcedimentoView, ObstetricoView
import nexgyn.views

urlpatterns = patterns('',
                       url(r'^$', 'nexgyn.views.home', name='home'),
                       url(r'^relatorio/$', 'nexgyn.views.pdfversion'),
                       url(r'^exames/', ObstetricoView.as_view()),
                       url(r'^renovacoes/', RenovacaoView.as_view()),
                       url(r'^procedimentos/', ProcedimentoView.as_view()),
                       url(r'^admin/', include(xadmin.site.urls)),
                       )
