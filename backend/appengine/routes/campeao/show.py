# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from google.appengine.ext import ndb
from gaepermission.decorator import login_not_required
from routes.campapel.modelo import CamPapel, CamPapelForm
from routes.criatura.modelo import Criatura
from tekton import router
from routes.campeao.home import returnIndex
from routes.campeao.modelo import Campeao,CampeaoForm
from tekton.gae.middleware.redirect import RedirectResponse


@login_not_required
@no_csrf
def index(_resp,campeao_id):

    campeao_id=int(campeao_id)
    campeao=Campeao.get_by_id(campeao_id)
    papelP=CamPapel.get_by_id(campeao.papelP.id())
    papelS=CamPapel.get_by_id(campeao.papelS.id())
    contexto={'campeao':campeao,
              'papelP':papelP,
              'papelS':papelS}
    return TemplateResponse(contexto)



@no_csrf
def form(_resp):
    query=CamPapel.query().order(CamPapel.name)
    camPapelL=query.fetch()
    contexto={'camPapelL':camPapelL,
              'salvar_path':router.to_path(salvar)}
    return TemplateResponse(contexto,'campeao/form.html')


def salvar(_resp,**prop):

    prop['papelP']=ndb.Key(CamPapel,int(prop['papelP']))
    prop['papelS']=ndb.Key(CamPapel,int(prop['papelS']))

    campeaoF=CampeaoForm(**prop)
    erros=campeaoF.validate()

    if erros:
        query=CamPapel.query().order(CamPapel.name)
        camPapelL=query.fetch()
        contexto={'salvar_path':router.to_path(salvar),
                  'erros':erros,
                  'campeao':campeaoF,
                  'camPapelL':camPapelL}
        return TemplateResponse(contexto,'campeao/form.html')

    else:
        campeao=campeaoF.fill_model()
        campeao.put()
        return RedirectResponse(returnIndex())



@no_csrf
def editar_form(campeao_id):

    query=CamPapel.query().order(CamPapel.name)
    camPapelL=query.fetch()

    campeao_id=int(campeao_id)
    campeao=Campeao.get_by_id(campeao_id)

    papelP=CamPapel.get_by_id(campeao.papelP.id())
    papelS=CamPapel.get_by_id(campeao.papelS.id())

    contexto={'salvar_path':router.to_path(editar,campeao_id),
              'camPapelL':camPapelL,
              'campeao':campeao,
              'papelP':papelP,
              'papelS':papelS}
    return TemplateResponse(contexto,template_path='campeao/form.html')


def editar(campeao_id,**prop):


    prop['papelP']=ndb.Key(CamPapel,int(prop['papelP']))
    prop['papelS']=ndb.Key(CamPapel,int(prop['papelS']))

    campeao_id=int(campeao_id)
    campeao=Campeao.get_by_id(campeao_id)

    campeaoF=CampeaoForm(**prop)
    erros=campeaoF.validate()
    if erros:
        contexto={'salvar_path':router.to_path(editar),
                  'erros':erros,
                  'campeao':campeaoF}
        return TemplateResponse(contexto,'campapel/form.html')

    else:
        campeaoF.fill_model(campeao)
        campeao.put()
        return RedirectResponse(router.to_path(returnIndex()))

def deletar(campeao_id):
    chave=ndb.Key(Campeao,int(campeao_id))
    chave.delete()
    return RedirectResponse(router.to_path(returnIndex()))