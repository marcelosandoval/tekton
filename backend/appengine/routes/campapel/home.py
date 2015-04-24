# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms import ndb
from gaepermission.decorator import login_not_required
from routes.campapel.modelo import CamPapel, CamPapelForm
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


@login_not_required
@no_csrf
def index():
    query=CamPapel.query().order(CamPapel.name)
    camPapelL=query.fetch()
    contexto={'camPapelL':camPapelL}

    return TemplateResponse(contexto)

def returnIndex():
    return router.to_path(index)

