# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from henrique.ui.mainwindow import Ui_MainWindow

class Henrique(object):

    def __init__(self, argv):
        self.argv = argv

    def start(self):
        app = QtGui.QApplication(self.argv)
        MainWindow = QtGui.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
