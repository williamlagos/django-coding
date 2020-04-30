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

from django.db import models

class Media(models.Model):
	name = models.CharField(default='$>',max_length=50)
	filename = models.CharField(max_length=100)
	user = ForeignKey(User,related_name='+')
	date = models.DateTimeField()
	def token(self): return self.name[:2]
	def render(self):
		source = ""
		return Template(source).render(Context({
			'name':object.name
		}))

class MediaShare(models.Model):
	name = models.CharField(default='$>',max_length=50)
	path = models.CharField(max_length=100)
	user = ForeignKey(User,related_name='+')
	date = models.DateTimeField()
	def token(self): return self.name[:2]
	def render(self):
		source = ""
		return Template(source).render(Context({
			'name':object.name
		}))
