# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from gaepermission.decorator import login_not_required
from tekton import router
from gaecookie.decorator import no_csrf
from itens_app import itens_facade
from routes import itenss
from tekton.gae.middleware.redirect import RedirectResponse

@login_not_required
@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)}, 'itenss/itens_form.html')

@login_not_required
def save(**item_properties):
    cmd = itens_facade.save_item_cmd(**item_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'item': item_properties}

        return TemplateResponse(context, 'itenss/itens_form.html')
    return RedirectResponse(router.to_path(itenss))

