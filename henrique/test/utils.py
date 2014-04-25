# -*- coding: utf-8 -*-

import unittest
import exceptions
import henrique.utils

class UiFactoryTest(unittest.TestCase):

    def setUp(self):
        self.uifactory = utils.UiFactory(events_module="henrique.test.mock.event",
                ui_module="henrique.test.mock.ui")

    def test_modules(self):
        self.assertEqual("henrique.test.mock.event", self.uifactory.events_module)
        self.assertEqual("henrique.test.mock.event", self.uifactory.ui_module)

    def test_make_class_generation(self):
        event_manager = self.uifactory.make('MainWindow')
        self.assertIsInstance(event_manager, henrique.test.mock.event.MainWindowEventManager)
        self.assertIsInstance(event_manager.ui, henrique.test.mock.ui.Ui_MainWindow)

    def test_make_invalid_class(self):
        self.assertRaises(exceptions.ImportError, self.uifactory.make('UnexistentWIndow'))

