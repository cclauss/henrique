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
        return str(element.text())

    def getLineEditValues(self, keys):
        value_dict = {}
        for key in keys:
            value_dict[key] = self.getLineEditValue(key)

        return value_dict

    def setLineEditValues(self, value_dict):
        for key in value_dict.keys():
            self.setLineEditValue(key, value_dict[key])

    def setLineEditValue(self, attribute, value):
        element = self.getLineEditElement(attribute)
        value = str(value)

        element.setText(value)

    def getLineEditElement(self, attribute):
        element_name = "".join(word.capitalize() for word in attribute.split("_")).capitalize()
        element_name = "{0}LineEdit".format(element_name)

        if not hasattr(self.ui, element_name):
            raise UnexistentUiElementError("The element {0} doesn't exist in this UI".format(element_name))

        return getattr(self.ui, element_name)


class MainWindow(Ui_Henrique, BaseUi):

    def bindEvents(self):
        self.ReportCalendarWidget.selectionChanged.connect(self.controller.onReportDateChange)
        self.ReportText.textChanged.connect(self.controller.onReportTextChange)
        self.SettingsAction.triggered.connect(self.controller.onSettingsActionTriggered)
        self.SendButton.clicked.connect(self.controller.onSendButtonClicked)
        self.SendAndShutdownButton.clicked.connect(self.controller.onSendAndShutdownButtonClicked)
        self.SendAndLogoffButton.clicked.connect(self.controller.onSendAndLogoffButtonClicked)

    def getReportDate(self):
         return self.ReportCalendarWidget.selectedDate().toPyDate()

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
        self.ui.SaveButton.clicked.connect(self.controller.onSaveButtonClick)
        self.ui.CloseButton.clicked.connect(self.controller.onCloseButtonClick)

    def getSMTPSettings(self, keys):
        has_ssl = False

        if 'ssl' in keys:
            has_ssl = True
            keys.remove('ssl')

        values = self.getLineEditValues(keys)
        values['ssl'] = self.getSSL()

        return values

    def setSMTPSettings(self, settings):
        if 'ssl' in settings:
            self.setSSL(settings.pop('ssl'))

        self.setLineEditValues(settings)

    def getEmailSettings(self, keys):
        return self.getLineEditValues(keys)

    def setEmailSettings(self, settings):
        self.setLineEditValues(settings)

    def setSSL(self, ssl):
        state = QtCore.Qt.Checked if int(ssl) == 1 else QtCore.Qt.Unchecked
        self.ui.SSLCheckBox.setCheckState(state)

    def getSSL(self):
        state = self.ui.SSLCheckBox.checkState()
        return 1 if state == QtCore.Qt.Checked else 0
