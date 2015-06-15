# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.campapel.home import returnIndex
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node
from google.appengine.ext import ndb
from tekton.gae.middleware.redirect import RedirectResponse
from routes.campapel.modelo import CamPapel, CamPapelForm


@login_not_required
@no_csrf
def form(_resp):
    contexto={'salvar_path':router.to_path(salvar)}
    return TemplateResponse(contexto,'campapel/form.html')


@login_not_required
def salvar(**prop):

    camPapelF=CamPapelForm(**prop)
    erros=camPapelF.validate()
    if erros:
        contexto={'salvar_path':router.to_path(salvar),
                  'erros':erros,
                  'camPapel':prop}
        return TemplateResponse(contexto,'campapel/form.html')

    else:
        camPapel=camPapelF.fill_model()
        camPapel.put()
        return RedirectResponse(returnIndex())


@login_not_required
@no_csrf
def editar_form(camPapel_id):
    camPapel_id=int(camPapel_id)
    camPapel=CamPapel.get_by_id(camPapel_id)
    contexto={'salvar_path':router.to_path(editar,camPapel_id),'camPapel':camPapel}
    return TemplateResponse(contexto,template_path='campapel/form.html')


@login_not_required
def editar(camPapel_id,**prop):

    camPapel_id=int(camPapel_id)
    camPapel=CamPapel.get_by_id(camPapel_id)

    camPapelF=CamPapelForm(**prop)
    erros=camPapelF.validate()
    if erros:
        contexto={'salvar_path':router.to_path(editar),
                  'erros':erros,
                  'camPapel':camPapelF}
        return TemplateResponse(contexto,'campapel/form.html')

    else:
        camPapelF.fill_model(camPapel)
        camPapel.put()
        return RedirectResponse(router.to_path(returnIndex()))

@login_not_required
def deletar(camPapel_id):
    chave=ndb.Key(CamPapel,int(camPapel_id))
    chave.delete()
    return RedirectResponse(router.to_path(returnIndex()))