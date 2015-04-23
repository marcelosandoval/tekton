# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.criatura.modelo import CriaturaForm, Criatura
from routes.criatura.home import returnIndex
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node
from google.appengine.ext import ndb


@login_not_required
@no_csrf
def index(_resp,criatura_id):

    criatura_id=int(criatura_id)
    criatura=Criatura.get_by_id(criatura_id)

    contexto={'criatura':criatura}
    return TemplateResponse(contexto)



@no_csrf
def form():
    contexto={'salvar_path':router.to_path(salvar)}
    return TemplateResponse(contexto,template_path='criatura/form.html')


def salvar(**prop):

    criaturaF=CriaturaForm(**prop)
    erros=criaturaF.validate()
    if erros:
        contexto={'salvar_path':router.to_path(salvar),
                  'erros':erros,
                  'criatura':criaturaF}
        return TemplateResponse(contexto,'criatura/form.html')

    else:
        criatura=criaturaF.fill_model()
        criatura.put()
        return RedirectResponse(returnIndex())


@no_csrf
def editar_form(criatura_id):
    criatura_id=int(criatura_id)
    criatura=Criatura.get_by_id(criatura_id)
    contexto={'salvar_path':router.to_path(editar,criatura_id),'criatura':criatura}
    return TemplateResponse(contexto,template_path='criatura/form.html')


def editar(criatura_id,**prop):

    criatura_id=int(criatura_id)
    criatura=Criatura.get_by_id(criatura_id)

    criaturaF=CriaturaForm(**prop)
    erros=criaturaF.validate()
    if erros:
        contexto={'salvar_path':router.to_path(salvar),
                  'erros':erros,
                  'criatura':criaturaF}
        return TemplateResponse(contexto,'criatura/form.html')

    else:
        criaturaF.fill_model(criatura)
        criatura.put()
        return RedirectResponse(returnIndex())

def deletar(criatura_id):
    chave=ndb.Key(Criatura,int(criatura_id))
    chave.delete()
    return RedirectResponse(returnIndex())