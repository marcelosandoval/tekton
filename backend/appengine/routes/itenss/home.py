# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from itens_app import itens_facade
from routes.itenss import new, edit,rest
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    context = {'rest_list_path': router.to_path(rest.index),
               'rest_new_path': router.to_path(rest.new),
               'rest_delete_path': router.to_path(rest.delete)
    }
    return TemplateResponse(context, 'itenss/itens_home.html')


def delete(item_id):
    itens_facade.delete_item_cmd(item_id)()

    return RedirectResponse(router.to_path(index))

