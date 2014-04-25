# -*- coding: utf-8 -*-

import sys
import os
import shutil
import getopt
from PyQt4 import QtCore, QtGui
from utils import UiFactory
from ui.henrique import Ui_Henrique

DATABASE = 'henrique.db'

class Henrique(object):

    def __init__(self, argv):
        self.argv = argv
        self.uifactory = UiFactory(self)
        self.setupEnvironment()

    def setupEnvironment(self):
        argv = self.argv[1:]
        optlist, args = getopt.getopt(argv, '', ['home-dir='])

        for opt, val in optlist:
            if opt == '--home-dir':
                self.home = val

        self.makeHomeDirectory()
        self.copyDatabase()

    def copyDatabase(self):
        dbfile = os.path.join(self.home, DATABASE)

        if not os.path.exists(dbfile):
            currentpath = os.path.dirname(os.path.realpath(__file__))
            sourcefile = os.path.realpath(os.path.join(currentpath, '..', 'db', DATABASE))
            shutil.copy2(sourcefile, dbfile)

        self.dbfile = dbfile

    def makeHomeDirectory(self):
        self.home = self.home if hasattr(self, 'home') else os.path.expanduser('~/.henrique')

        if not os.path.exists(self.home):
            os.makedirs(self.home, mode = 0755)

    def start(self):
        app = QtGui.QApplication(self.argv)
        main_window = QtGui.QMainWindow()
        self.main_window = main_window
        ui_event = self.uifactory.make("Henrique")
        sys.exit(app.exec_())
