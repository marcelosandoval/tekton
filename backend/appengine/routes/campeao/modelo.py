# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb

from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node


class Campeao(Node):
    name=ndb.StringProperty(required=True)
    image=ndb.StringProperty()
    papelP=ndb.KeyProperty( required=True)
    title=ndb.StringProperty(required=True)
    papelS=ndb.KeyProperty()
    barra=ndb.StringProperty()
    hp=ndb.IntegerProperty()
    hpregen=ndb.IntegerProperty()
    ataqueT=ndb.StringProperty()
    range=ndb.IntegerProperty()
    atksp=ndb.IntegerProperty()
    damage=ndb.IntegerProperty()
    armor=ndb.IntegerProperty()
    magicres=ndb.IntegerProperty()
    movesp=ndb.IntegerProperty()



class CampeaoForm(ModelForm):
    _model_class = Campeao
    _exclude = [Campeao.creation]

