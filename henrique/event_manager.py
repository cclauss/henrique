# -*- coding: utf-8 -*-

import controller

class EventManager(object):
    def __init__(self, ui, app):
        self.ui = ui
        self.app = app
        self.bind()

    def bind(self):
        raise NotImplementedError("The EventManager must implement the 'bind' method")


class HenriqueEventManager(EventManager):

    def __init__(self, ui, app):
        super(HenriqueEventManager, self).__init__(ui)
        self.controller = controller.MainWindowController(self)

    def bind(self):
        pass
