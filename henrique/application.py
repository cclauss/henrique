# -*- coding: utf-8 -*-

import sys
import argparse
from PyQt4 import QtCore, QtGui
from utils import UiFactory
from ui.henrique import Ui_Henrique

class Henrique(object):

    def __init__(self, argv):
        self.argv = argv
        print self.argv
        sys.exit(0)
        self.uifactory = UiFactory()
        self.setupEnvironment()

    def setupEnvironment(self):
        pass

    def start(self):
        app = QtGui.QApplication(self.argv)
        main_window = QtGui.QMainWindow()
        ui_event = self.uifactory.make("Henrique")
        ui = ui_event.ui
        ui.setupUi(main_window)
        main_window.show()
        sys.exit(app.exec_())
