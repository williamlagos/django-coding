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

from django.http import HttpResponse as response
import json
# Create your views here.

def client_id(request):
	response_data = {
		'client_id':'d63f53a7a6cceba04db5',
		'client_secret':'afe899288b9ac4127d57f2f12ac5a49d839364dc'
	}
	return response(json.dumps(response_data), content_type="application/json")

def request_token(request):
	response_data = { 
		'access_token': 'a832106c17d00fd3b9094181c598820ef3ff76f4', 
		'scope': 'read write', 
		'expires_in': 86399, 
		'refresh_token': 'bfdbd5510ae724a2dbd458e68274ab5c8590d3e4'
	}
	return response(json.dumps(response_data), content_type="application/json")

def refresh_token(request):
	response_data = {
		'access_token': 'a83546456254645678321181c59884gt54jk6rf9'
	}
	return response(json.dumps(response_data), content_type="application/json")

def grant_access(request):
	f = open('/var/run/upnp.exec','w')
	f.write('granted')
	f.close()
	response_data = { 'access': 'granted' }
	return response(json.dumps(response_data), content_type="application/json")
