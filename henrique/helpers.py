# -*- coding: utf-8 -*-

from repositories import ReportRepository

class MainWindowHelper(object):

    def __init__(self, ui, report):
        self.ui = ui
        self.report = report

    def refreshUi(self):
        self.ui.TasksEditor.setText(self.report['content'])
        self.updateStatus()

    def updateStatus(self):
        text = 'This report wasn\'t sent'
        style = 'color: red'

        if self.report['status'] == ReportRepository.STATUS_SENT:
            text = 'This report was already sent'
            style = 'color: green'

        self.ui.StatusLabel.setText(text)
        self.ui.StatusLabel.setStyleSheet(style)
