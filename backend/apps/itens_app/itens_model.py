# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Item(Node):
    nome = ndb.StringProperty(required=True)
    tipo = ndb.StringProperty(required=True)
    bonus = ndb.StringProperty(required=True)
    passiva = ndb.StringProperty(required=True)
    ativa = ndb.StringProperty(required=True)
    aura = ndb.StringProperty(required=True)
    vlrCompra = ndb.IntegerProperty(required=True)
    vlrVenda = ndb.IntegerProperty(required=True)

