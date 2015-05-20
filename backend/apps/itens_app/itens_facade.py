# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from itens_app.itens_commands import ListItemCommand, SaveItemCommand, UpdateItemCommand, ItemForm,\
    GetItemCommand, DeleteItemCommand


def save_item_cmd(**item_properties):
    """
    Command to save Item entity
    :param item_properties: a dict of properties to save on model
    :return: a Command that save Item, validating and localizing properties received as strings
    """
    return SaveItemCommand(**item_properties)


def update_item_cmd(item_id, **item_properties):
    """
    Command to update Item entity with id equals 'item_id'
    :param item_properties: a dict of properties to update model
    :return: a Command that update Item, validating and localizing properties received as strings
    """
    return UpdateItemCommand(item_id, **item_properties)


def list_items_cmd():
    """
    Command to list Item entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListItemCommand()


def item_form(**kwargs):
    """
    Function to get Item's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ItemForm(**kwargs)


def get_item_cmd(item_id):
    """
    Find item by her id
    :param item_id: the item id
    :return: Command
    """
    return GetItemCommand(item_id)



def delete_item_cmd(item_id):
    """
    Construct a command to delete a Item
    :param item_id: item's id
    :return: Command
    """
    return DeleteItemCommand(item_id)

