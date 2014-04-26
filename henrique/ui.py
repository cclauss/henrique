# -*- coding: utf-8 -*-

from qtdesigner.henrique import Ui_Henrique

class BaseUi(object):

    def __init__(self, controller):
        self.controller = controller


class MainWindow(Ui_Henrique, BaseUi):

    def bindEvents(self):
        self.ReportCalendarWidget.selectionChanged.connect(self.controller.onReportDateChange)
        self.ReportText.textChanged.connect(self.controller.onReportTextChange)

    def getReportText(self):
        return str(self.ReportText.toPlainText())
