# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission import facade
from config.tmpl_middleware import TemplateResponse


@no_csrf
def index():
    path_infos = facade.web_path_security_info()
    path_infos = sorted(path_infos, key=lambda i: i.path)
    return TemplateResponse({'path_infos': path_infos},'permission/security_table.html')