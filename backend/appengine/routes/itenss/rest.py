# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from itens_app import itens_facade


def index():
    cmd = itens_facade.list_items_cmd()
    item_list = cmd()
    item_form = itens_facade.item_form()
    item_dcts = [item_form.fill_with_model(m) for m in item_list]
    return JsonResponse(item_dcts)


def new(_resp, **item_properties):
    cmd = itens_facade.save_item_cmd(**item_properties)
    return _save_or_update_json_response(cmd, _resp)


def edit(_resp, id, **item_properties):
    cmd = itens_facade.update_item_cmd(id, **item_properties)
    return _save_or_update_json_response(cmd, _resp)


def delete(_resp, id):
    cmd = itens_facade.delete_item_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


def _save_or_update_json_response(cmd, _resp):
    try:
        item = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    item_form = itens_facade.item_form()
    return JsonResponse(item_form.fill_with_model(item))

