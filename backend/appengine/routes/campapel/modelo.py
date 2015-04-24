# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb

from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node


class CamPapel(Node):
    name=ndb.StringProperty(required=True)
    image=ndb.StringProperty()

class CamPapelForm(ModelForm):
    _model_class = CamPapel
    _exclude = [CamPapel.creation]

