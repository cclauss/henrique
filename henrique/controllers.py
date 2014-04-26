# -*- coding: utf-8 -*-

import models
import datetime
import ui
import helpers

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


class MainWindowController(Controller):

    def __init__(self, app):
        super(MainWindowController, self).__init__(app)
        self.ui = ui.MainWindow(self)
        self.model = models.ReportModel(self.app)
        self.childpid = None

        self.showUi()
        self.onReportDateChange()

    def onReportDateChange(self):
        calendar = self.ui.ReportCalendarWidget
        calendar_date = calendar.selectedDate().toPyDate()
        report = self.model.findByDate(calendar_date)

        if len(report) == 0:
            self.model.create(date=calendar_date)
            report = self.model.findByDate(calendar_date)

        report = report[0]
        self.report = report

        helper = helpers.MainWindowHelper(self.ui, self.report)
        helper.refreshUi()

    def onReportTextChange(self):
        content = self.ui.getReportText()
        self.model.update(self.report['id'], content=content)
