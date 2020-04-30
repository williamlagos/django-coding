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

from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from models import Media,MediaShare
from tastypie import fields
from efforia.social import OAuth20Authentication

class MediaResource(ModelResource):
    class Meta:
        queryset = Resource.objects.all()
        resource_name = 'media'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()

class MediaShareResource(ModelResource):
    class Meta:
        queryset = Resource.objects.all()
        resource_name = 'mediashare'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
