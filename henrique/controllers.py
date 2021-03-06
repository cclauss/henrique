# -*- coding: utf-8 -*-

import sys
import models
import datetime
import ui
import helpers
from PyQt4 import QtCore, QtGui

class Controller(object):

    def __init__(self, app):
        self.app = app

    def showUi(self):
        self.ui.setupUi(self.app.main_window)
        self.ui.bindEvents()

        if not self.app.main_window.isVisible():
            self.app.main_window.show()
        else:
            self.app.main_window.update()

    def makeEmailHelper(self):
        if not hasattr(self, 'email_helper'):
            settings_model = models.SettingsModel(self.app)
            smtp_settings = settings_model.findSMTPSettings()
            email_settings = settings_model.findEmailSettings()
            self.email_helper = helpers.EmailHelper(smtp_settings, email_settings)

        return self.email_helper


class MainWindowController(Controller):

    def __init__(self, app):
        super(MainWindowController, self).__init__(app)
        self.ui = ui.MainWindow(self)
        self.model = models.ReportModel(self.app)

        self.showUi()
        self.onReportDateChange()

    def onReportDateChange(self):
        calendar_date = self.ui.getReportDate()
        report = self.model.findByDate(calendar_date)

        if len(report) == 0:
            self.model.create(date=calendar_date)
            report = self.model.findByDate(calendar_date)

        report = report[0]
        self.report = report

        helper = helpers.MainWindowHelper(self.ui, self.report)
        helper.refreshUi()

    def onExit(self):
        self.model.commit()

    def onReportTextChange(self):
        content = self.ui.getReportText()
        self.model.update(self.report['id'], content=content, status=self.report['status'])

    def onSettingsActionTriggered(self, checked):
        SettingsWindowController(self.app, self.ui.MainWidget)

    def onSendButtonClicked(self):
        # TODO - Add some visual tip of what's going on
        # TODO - Handle errors...
        self.makeEmailHelper().sendReport(self.report)
        self.report['status'] = models.ReportModel.STATUS_SENT
        self.model.update(self.report['id'], content=self.report['content'], status=models.ReportModel.STATUS_SENT)

        self.model.commit()
        helper = helpers.MainWindowHelper(self.ui, self.report)
        helper.refreshUi()

    def onSendAndShutdownButtonClicked(self):
        self.onSendButtonClicked()
        helper = helpers.OSActionsFactory.make()
        helper.shutdown()

    def onSendAndLockButtonClicked(self):
        self.onSendButtonClicked()
        helper = helpers.OSActionsFactory.make()
        helper.lock()


class SettingsWindowController(Controller):

    def __init__(self, app, parent):
        super(SettingsWindowController, self).__init__(app)
        self.ui = ui.SettingsWindow(self, parent)
        self.model = models.SettingsModel(self.app)

        self.loadSettings()
        self.ui.bindEvents()
        self.ui.show()

    def loadSettings(self):
        smtp_settings  = self.model.findSMTPSettings()
        email_settings = self.model.findEmailSettings()
        self.ui.setSMTPSettings(smtp_settings)
        self.ui.setEmailSettings(email_settings)

    def onCloseButtonClick(self):
        self.ui.close()

    def onSaveButtonClick(self):
        smtp_keys  = self.model.SETTINGS_SMTP.keys()
        email_keys = self.model.SETTINGS_EMAIL.keys()

        self.model.saveSMTPSettings(self.ui.getSMTPSettings(smtp_keys))
        self.model.saveEmailSettings(self.ui.getEmailSettings(email_keys))

        if hasattr(self, 'email_helper'):
            del self.email_helper

        self.ui.close()
