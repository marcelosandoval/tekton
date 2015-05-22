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
def index(item_id):
    item = itens_facade.get_item_cmd(item_id)()
    item_form = itens_facade.item_form()
    context = {'save_path': router.to_path(save, item_id), 'item': item_form.fill_with_model(item)}
    return TemplateResponse(context, 'itenss/itens_form.html')

@login_not_required
def save(item_id, **item_properties):
    cmd = itens_facade.update_item_cmd(item_id, **item_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors, 'item': item_properties}

        return TemplateResponse(context, 'itenss/itens_form.html')
    return RedirectResponse(router.to_path(itenss))

