# -*- coding: utf-8 -*-

from qtdesigner.henrique import Ui_Henrique

class BaseUi(object):

    def __init__(self, controller):
        self.controller = controller


class MainWindow(Ui_Henrique, BaseUi):

    def bindEvents(self):
        pass
