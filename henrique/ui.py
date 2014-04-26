# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from qtdesigner.henrique import Ui_Henrique
from qtdesigner.settings import Ui_Settings

class BaseUi(object):

    def __init__(self, controller):
        self.controller = controller


class MainWindow(Ui_Henrique, BaseUi):

    def bindEvents(self):
        self.ReportCalendarWidget.selectionChanged.connect(self.controller.onReportDateChange)
        self.ReportText.textChanged.connect(self.controller.onReportTextChange)
        self.SettingsAction.triggered.connect(self.controller.onSettingsActionTriggered)

    def getReportText(self):
        return str(self.ReportText.toPlainText())


class SettingsWindow(BaseUi, QtGui.QDialog):

    def __init__(self, controller, parent=None):
        BaseUi.__init__(self, controller)
        QtGui.QDialog.__init__(self, parent)

        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.ui.PasswordLineEdit.setEchoMode(QtGui.QLineEdit.Password)

    def bindEvents(self):
        self.ui.SettingsButtonBox.accepted.connect(self.controller.onSaveButtonClick)
        self.ui.SettingsButtonBox.rejected.connect(self.controller.onCloseButtonClick)

    def setUsername(self, username):
        username = QtCore.QString(username)
        self.ui.UsernameLineEdit.setText(username)

    def getUsername(self):
        return str(self.ui.UsernameLineEdit.text())

    def setPassword(self, password):
        password = QtCore.QString(password)
        self.ui.PasswordLineEdit.setText(password)

    def getPassword(self):
        return str(self.ui.PasswordLineEdit.text())

    def setAddress(self, address):
        address = QtCore.QString(address)
        self.ui.AddressLineEdit.setText(address)

    def getAddress(self):
        return str(self.ui.AddressLineEdit.text())

    def setPort(self, port):
        port = QtCore.QString(port)
        self.ui.PortLineEdit.setText(port)

    def getPort(self):
        return str(self.ui.PortLineEdit.text())

    def setSSL(self, ssl):
        state = QtCore.Qt.Checked if int(ssl) == 1 else QtCore.Qt.Unchecked
        self.ui.SSLCheckBox.setCheckState(state)

    def getSSL(self):
        state = self.ui.SSLCheckBox.checkState()
        return 1 if state == QtCore.Qt.Checked else 0
