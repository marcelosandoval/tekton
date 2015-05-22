# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse
from itens_app import itens_facade

@login_not_required
@no_csrf
def index():
    cmd = itens_facade.list_items_cmd()
    item_list = cmd()
    item_form = itens_facade.item_form()
    item_dcts = [item_form.fill_with_model(m) for m in item_list]
    return JsonResponse(item_dcts)

@login_not_required
def new(_resp, **item_properties):
    cmd = itens_facade.save_item_cmd(**item_properties)
    return _save_or_update_json_response(cmd, _resp)

@login_not_required
def edit(_resp, item_id, **item_properties):
    cmd = itens_facade.update_item_cmd(item_id, **item_properties)
    return _save_or_update_json_response(cmd, _resp)

@login_not_required
def delete(item_id):
    itens_facade.delete_item_cmd(item_id)()



def _save_or_update_json_response(cmd, _resp):
    try:
        item = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    item_form = itens_facade.item_form()
    return JsonResponse(item_form.fill_with_model(item))

