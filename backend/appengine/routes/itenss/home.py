# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from itens_app import itens_facade
from routes.itenss import new, edit
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    cmd = itens_facade.list_items_cmd()
    items = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    item_form = itens_facade.item_form()

    def localize_item(item):
        item_dct = item_form.fill_with_model(item)
        item_dct['edit_path'] = router.to_path(edit_path, item_dct['id'])
        item_dct['delete_path'] = router.to_path(delete_path, item_dct['id'])
        return item_dct

    localized_items = [localize_item(item) for item in items]
    context = {'items': localized_items,
               'new_path': router.to_path(new)}
    return TemplateResponse(context, 'itenss/itens_home.html')


def delete(item_id):
    itens_facade.delete_item_cmd(item_id)()
    return RedirectResponse(router.to_path(index))

