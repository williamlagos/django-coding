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

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Hidden, HTML, Field

class PhotoForm(forms.Form):
    file = forms.FileField(label='')
    redirect = forms.CharField(label='')
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_action = '/efforia/photo'
        self.helper.layout = Layout(
            Hidden('redirect',value='1'),
            Field('file',style='opacity:0; width:0; height:0',css_class='file'),
            Div(HTML("<span class='glyphicon glyphicon-cloud-upload icon-glyphicon'></span>"),css_class='upload')
        )
        super(PhotoForm, self).__init__(*args, **kwargs)
