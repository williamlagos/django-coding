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

from efforia.feed import Activity
from efforia.control import Option
from sockets import SocketHandler

class Application(Activity):
    def __init__(self,user,feed):
        Activity.__init__(self,user,feed)
        self.ws_handler = SocketHandler()
        self.context = {}
        self.source = ""
    def deadline(self): pass
    def relations(self,feed): pass
    def groupables(self,feed): pass
    def duplicates(self,feed): pass
    def mosaic(self,request,feed): pass
    def remote_control(self,request): pass
    def send_command(self,request): pass

class MediaShares(Option):
	def __init__(self):
		Option.__init__(self)
	def change(self,request): pass
	def view(self,request): pass
