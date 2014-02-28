#
# This file is part of Efforia project.
#
# Copyright (C) 2011-2013 William Oliveira de Lagos <william@efforia.com.br>
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

from social_feed.feed import Activity
from django.template import Template,Context

class Application(Activity):
    def __init__(self,user,app):
        Activity.__init__(self,user,app)
    def mosaic(self,request,feed):
        t = Template(self.source)
        self.context['f'] = feed
        self.context['path'] = request.path
        rendered = t.render(Context(self.context))
        for object in feed.object_list: rendered += object.render()
        return rendered
