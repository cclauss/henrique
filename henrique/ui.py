# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from qtdesigner.henrique import Ui_Henrique
from qtdesigner.settings import Ui_Settings

class UnexistentUiElementError(AttributeError):
    pass

class BaseUi(object):

    def __init__(self, controller):
        self.controller = controller

    def getLineEditValue(self, attribute):
        element = self.getLineEditElement(attribute)
        return str(element.toPlainText())

    def setLineEditValue(self, attribute, value):
        element = self.getLinEditElement(attribute)
        value = str(value)

        element.setText(value)

    def getLineEditElement(self, attribute):
        element_name = "{0}LineEdit".format(attribute)

        if not hasattr(self.ui, element_name):
            raise UnexistentUiElementError("The element {0} doesn't exist in this UI".format(element_name))

        return getattr(self.ui, element_name)


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
        pass

    def setSSL(self, ssl):
        state = QtCore.Qt.Checked if int(ssl) == 1 else QtCore.Qt.Unchecked
        self.ui.SSLCheckBox.setCheckState(state)

    def getSSL(self):
        state = self.ui.SSLCheckBox.checkState()
        return 1 if state == QtCore.Qt.Checked else 0
