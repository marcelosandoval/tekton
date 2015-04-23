# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.criatura.modelo import Criatura
from tekton import router

@login_not_required
@no_csrf
def index():
    query=Criatura.query().order(Criatura.name)
    criaturaL=query.fetch()
    contexto={'criaturaL':criaturaL}

    return TemplateResponse(contexto)


def returnIndex():
    return router.to_path(index)