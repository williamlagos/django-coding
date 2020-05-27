from django.conf.urls import url,include
from alpha.views import *

urlpatterns = [
    url(r'^alpha$', init_create),
    url(r'^alpha/project', project_form),
    url(r'^alpha/events/(?P<eventid>\d+)$', eventview),
    url(r'^alpha/projects/(?P<projectid>\d+)$', project),
    url(r'^alpha/promoted', promoted),
    url(r'^alpha/eventid', eventid),
    url(r'^alpha/projectform', main),
    url(r'^alpha/backers', backers),
    url(r'^alpha/movements', movements),
    url(r'^alpha/promote', promote),
    url(r'^alpha/linkproj', link),
    url(r'^alpha/movement', movement),
    url(r'^alpha/pledge', pledge),
    url(r'^alpha/grab', grab),
    url(r'^alpha/eventimage', event_image),
    url(r'^alpha/event', eventview),
    url(r'^alpha/enroll', enroll),
    url(r'^alpha/calendar', event),
]

# from efforia.views import *
#
# urlpatterns = [
#     url(r'^efforia/mosaic', mosaic),
#     url(r'^efforia/config', config),
#     url(r'^efforia/profile', profile),
#     url(r'^efforia/basketclean', basketclean),
#     url(r'^efforia/basket', basket),
#     url(r'^efforia/photo', photo),
#     url(r'^efforia/appearance', appearance),
#     url(r'^efforia/options', options),
#     url(r'^efforia/place', place),
#     url(r'^efforia/password', password),
#     url(r'^efforia/integrations', integrations),
#     url(r'^efforia/enter', authenticate),
#     url(r'^efforia/leave', leave),
#     url(r'^efforia/delete', delete),
#     url(r'^efforia/userid', ids),
#     url(r'^efforia/search', search),
#     url(r'^efforia/explore', search),
#     url(r'^efforia/known', explore),
#     url(r'^efforia/activity', activity),
#     url(r'^efforia/following', following),
#     url(r'^efforia/follow', follow),
#     url(r'^efforia/unfollow', unfollow),
#     url(r'^efforia/twitter/post', twitter_post),
#     url(r'^efforia/facebook/post', facebook_post),
#     url(r'^efforia/facebook/eventcover', facebook_eventcover),
#     url(r'^efforia/facebook/event', facebook_event),
#     url(r'^efforia/participate', participate),
#     url(r'^efforia/tutorial', tutorial),
#     url(r'^efforia/pagseguro/cart', pagsegurocart),
#     url(r'^efforia/pagseguro', pagseguro),
#     url(r'^efforia/paypal/cart', paypalcart),
#     url(r'^efforia/paypal', paypal),
#     url(r'^efforia/pages', page),
#     url(r'^efforia/pageview', pageview),
#     url(r'^efforia/pageedit', pageedit),
#     url(r'^efforia/discharge', discharge),
#     url(r'^efforia/recharge', recharge),
#     url(r'^efforia/balance', balance),
#     url(r'^efforia/deadlines', deadlines),
# ]

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django_distill import distill_url
# from django_pagseguro.urls import pagseguro_urlpatterns

admin.autodiscover()

def getNone(): return None

urlpatterns += [
    # url(r'^efforia/efforia/',include('efforia.urls')),
    # url(r'^alpha/|alpha$',include('promote.urls')),
    # url(r'^(?P<name>\w+)$', profileview),
    url(r'^socialize/',include('socialize.urls')),
    url(r'^shipping/',include('shipping.urls')),
    url(r'^feedly/',include('feedly.urls')),
    distill_url(r'^',start, name='home', distill_func=getNone),
]

urlpatterns += staticfiles_urlpatterns()
# urlpatterns += pagseguro_urlpatterns()
