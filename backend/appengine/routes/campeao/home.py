# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from google.appengine.ext import ndb
from gaepermission.decorator import login_not_required
from routes.campapel.modelo import CamPapel
from routes.campeao.modelo import Campeao
from tekton import router

@login_not_required
@no_csrf
def index(_resp,campeao_filtro=None):
    if campeao_filtro==None:
        query=Campeao.query().order(Campeao.name)
        campeaoL=query.fetch()
    else:
        chave=ndb.Key(CamPapel,int(campeao_filtro))
        query=Campeao.query(Campeao.papelP==chave).order(Campeao.name)
        campeaoL=query.fetch()

    query=CamPapel.query().order(CamPapel.name)
    camPapelL=query.fetch()

    contexto={'camPapelL':camPapelL,
              'campeaoL':campeaoL}

    return TemplateResponse(contexto)


def returnIndex():
    return router.to_path(index)