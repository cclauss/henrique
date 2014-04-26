# -*- coding: utf-8 -*-

import repositories
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
        self.report_repository = repositories.ReportRepository(self.app)

        self.showUi()
        self.onReportDateChange()

    def onReportDateChange(self):
        calendar = self.ui.ReportCalendarWidget
        calendar_date = calendar.selectedDate().toPyDate()
        report = self.report_repository.findByDate(calendar_date)

        if len(report) == 0:
            self.report_repository.create(date=calendar_date)
            report = self.report_repository.findByDate(calendar_date)

        report = report[0]
        self.report = report
        helper = helpers.MainWindowHelper(self.ui, self.report)
        helper.refreshUi()
