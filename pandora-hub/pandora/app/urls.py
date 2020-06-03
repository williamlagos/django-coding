#
# This file is part of Efforia project.
#
# Copyright (C) 2013 Diego Stuani Cavalli <diego.stuani.cavalli@gmail.com>
#
# Efforia is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Efforia is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Efforia. If not, see <http://www.gnu.org/licenses/>.
#

from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

from .views import *

urlpatterns = [ #'app.views',
	# url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),
	url(r'^oauth/client_id', client_id),
	url(r'^oauth/request_token', request_token),
	url(r'^oauth/refresh_token', refresh_token),
	url(r'^oauth/grant_access', grant_access),
]
