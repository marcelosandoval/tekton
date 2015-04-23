# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms import base
from gaeforms.base import Form
from gaegraph.model import Node
from gaepermission.decorator import login_not_required
from tekton import router


@login_not_required
@no_csrf
def index(nome='none'):
    return TemplateResponse()



@no_csrf
def form():
    contexto={'salvar_path':router.to_path(salvar)}
    return TemplateResponse(contexto,template_path='criatura/form.html')

class Criatura(Node):
    name=ndb.StringProperty(required=True)
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

class CriaturaForm(Form):

    name=base.StringField(required=True)
    type=base.StringField()
    gold=base.IntegerField()
    xp=base.IntegerField()
    hp=base.IntegerField()
    damage=base.IntegerField()
    atksp=base.IntegerField()
    armor=base.IntegerField()
    magicres=base.IntegerField()
    movesp=base.IntegerField()
    spawn=base.StringField()
    respawn=base.StringField()
    buff=base.StringField()

def salvar(_resp,**prop):

    criaturaF=CriaturaForm(**prop)
    erros=criaturaF.validate()
    if erros:
        _resp.write(erros)
    else:
        pass

    #criatura=Criatura(name=prop['name'],
    #                  type=prop['type'],
     #                 gold=int(prop['gold']),
      #                xp=int(prop['xp']),
       #               hp=int(prop['hp']),
        #              damage=int(prop['damage']),
         #             atksp=int(prop['atksp']),
          #            armor=int(prop['armor']),
           #           magicres=int(prop['magicres']),
            #          movesp=int(prop['movesp']),
             #         spawn=prop['spawn'],
              #        respawn=prop['respawn'],
               #       buff=prop['buff'])
 #   criatura.put()
  #  _resp.write(prop)