# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from itens_app.itens_model import Item



class ItemSaveForm(ModelForm):
    """
    Form used to save and update Item
    """
    _model_class = Item
    _include = [Item.tipo, 
                Item.nome, 
                Item.bonus, 
                Item.ativa, 
                Item.passiva, 
                Item.aura, 
                Item.vlrVenda, 
                Item.vlrCompra]


class ItemForm(ModelForm):
    """
    Form used to expose Item's properties for list or json
    """
    _model_class = Item


class GetItemCommand(NodeSearch):
    _model_class = Item


class DeleteItemCommand(DeleteNode):
    _model_class = Item


class SaveItemCommand(SaveCommand):
    _model_form_class = ItemSaveForm


class UpdateItemCommand(UpdateNode):
    _model_form_class = ItemSaveForm


class ListItemCommand(ModelSearchCommand):
    def __init__(self):
        super(ListItemCommand, self).__init__(Item.query_by_creation())

