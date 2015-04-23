# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb

from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node


class Criatura(Node):
    name=ndb.StringProperty(required=True)
    image=ndb.StringProperty()
    type=ndb.StringProperty()
    gold=ndb.IntegerProperty()
    xp=ndb.IntegerProperty()
    hp=ndb.IntegerProperty()
    damage=ndb.IntegerProperty()
    atksp=ndb.IntegerProperty()
    armor=ndb.IntegerProperty()
    magicres=ndb.IntegerProperty()
    movesp=ndb.IntegerProperty()
    spawn=ndb.StringProperty()
    respawn=ndb.StringProperty()
    buff=ndb.TextProperty()

class CriaturaForm(ModelForm):
    _model_class = Criatura
    _exclude = [Criatura.creation]

