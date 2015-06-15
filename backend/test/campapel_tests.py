# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unittest import TestCase
from base import GAETestCase
from routes.campapel.modelo import  CamPapel
from config.template_middleware import TemplateResponse
from mock import Mock
from routes.campapel import show
from routes.itenss import rest
from tekton.gae.middleware.redirect import RedirectResponse


class NewTests(GAETestCase):
    def test_sucesso(self):
        resposta = show.salvar(name='TesteaName', image='TesteImage')
        self.assertIsInstance(resposta, RedirectResponse)
        self.assertEqual('/campapel', resposta.context)
        campapel = CamPapel.query().fetch()
        self.assertEqual(1, len(campapel))
        cam = campapel[0]
        self.assertEqual('TesteaName', cam.name)
        self.assertEqual('TesteImage', cam.image)


    def test_validacao(self):
        resposta = show.salvar()
        self.assertIsInstance(resposta, TemplateResponse)
        self.assert_can_render(resposta)
        self.assertIsNone(CamPapel.query().get())
        self.maxDiff = True
        self.assertDictEqual({u'salvar_path': '/campapel/show/salvar',
                              u'camPapel': {},
                              u'erros': {'name': u'Required field'}}
                             , resposta.context)
