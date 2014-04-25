# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from utils import UiFactory
from ui.mainwindow import Ui_MainWindow

class Henrique(object):

    def __init__(self, argv):
        self.argv = argv
        self.uifactory = UiFactory()

    def start(self):
        app = QtGui.QApplication(self.argv)
        main_window = QtGui.QMainWindow()
        ui_event = self.uifactory.make("MainWindow")
        ui = ui_event.ui
        ui.setupUi(main_window)
        main_window.show()
        sys.exit(app.exec_())
