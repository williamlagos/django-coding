#
# This file is part of Efforia project.
#
# Copyright (C) 2013 William Oliveira de Lagos <william@efforia.com.br>
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
#!/usr/bin/env python2
from os import path,environ,chdir
from subprocess import call as exe
from optparse import OptionParser
from app.sockets import SocketHandler
import django.core.handlers.wsgi
import tornado.web
import tornado.ioloop
import tornado.websocket
import tornado.wsgi

#environ['DJANGO_SETTINGS_MODULE'] = 'efforia.settings'

#wsgi_app = tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())
application = tornado.web.Application([
    (r'/websocket',SocketHandler),
    #(r'.*',tornado.web.FallbackHandler,{'fallback':wsgi_app})
],
debug=True, 
template_path=path.abspath('templates/'),
static_path  =path.abspath('static/'))

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

    #if opt.vagrant:
    #    chdir('../..')
    #    exe('vagrant up',shell=True)
    #    exe('vagrant ssh -c "killall python"',shell=True)
    #    exe('vagrant ssh -c "python /vagrant/plethora/main.py"',shell=True)

    #    print path.abspath('/')
