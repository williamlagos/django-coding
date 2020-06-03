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
#!/usr/bin/python
# -*- coding: utf-8 -*-
from .control import Profiles,Passwords,Control,Places,Photos

def explore(request):
    p = Profiles()
    if request.method == 'GET':
        return p.view_userinfo(request)

def activity(request):
    p = Profiles()
    if request.method == 'GET':
        return p.view_activity(request)

def profile(request):
    prof = Profiles()
    if request.method == 'GET':
        return prof.view_profile(request)
    elif request.method == 'POST':
        return prof.update_profile(request)

def password(request):
    pasw = Passwords()
    if request.method == 'GET':
        return pasw.view_password(request)
    elif request.method == 'POST':
        return pasw.change_password(request)

def place(request):
    p = Places()
    if request.method == 'GET':
        return p.register_place(request)
    elif request.method == 'POST':
        return p.create_place(request)

def photo(request):
    p = Photos()
    if request.method == 'GET':
        return p.view_photo(request)
    elif request.method == 'POST':
        return p.change_photo(request)

def appearance(request):
    c = Control()
    if request.method == 'GET':
        return c.view_control(request)
    elif request.method == 'POST':
        return c.change_control(request)

def options(request):
    c = Control()
    if request.method == 'GET':
        return c.view_options(request)

def config(request):
    c = Control()
    if request.method == 'GET':
        return c.view_panel(request)

def integrations(request):
    c = Control()
    if request.method == 'GET':
        return c.view_integrations(request)