# -*- coding: utf-8 -*-

class EventManager(object):
    def __init__(self, ui):
        self.ui = ui
        self.bind()

    def bind(self):
        raise NotImplementedError("The EventManager must implement the 'bind' method")


class MainWindowEventManager(EventManager):

    def bind(self):
        print "Binding!"
