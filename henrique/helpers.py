# -*- coding: utf-8 -*-

from models import ReportModel

class MainWindowHelper(object):

    def __init__(self, ui, report):
        self.ui = ui
        self.report = report

    def refreshUi(self):
        self.ui.ReportText.setText(self.report['content'])
        self.updateStatus()

    def updateStatus(self):
        text = 'This report wasn\'t sent'
        style = 'color: red'

        if self.report['status'] == ReportModel.STATUS_SENT:
            text = 'This report was already sent'
            style = 'color: green'

        self.ui.StatusLabel.setText(text)
        self.ui.StatusLabel.setStyleSheet(style)

class InvalidEmailSetings(ValueError):
    pass

class EmailHelper(object):

    def __init__(self, smtp_settings, email_settings):
        self.smtp_settings = smtp_settings
        self.email_settings = email_settings

    def sendReport(self, report):
        print report
