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

'''
Created on Oct 2, 2013

@author: DiegoCavalli
'''

from tornado import websocket, web, ioloop

class MainHandler(web.RequestHandler):
    def get(self):
        self.render('websocket.html')

class SocketHandler(websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"

    def on_message(self, message):
        print message
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"
