# -*- coding: utf-8 -*-

import repository
import datetime

class Controller(object):

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.ui = event_manager.ui
        self.app = event_manager.app
        self.showUi()

    def showUi(self):
        self.ui.setupUi(self.app.main_window)

        if not self.app.main_window.isVisible():
            self.app.main_window.show()
        else:
            self.app.main_window.update()


class MainWindowController(Controller):

    def __init__(self, event_manager):
        super(MainWindowController, self).__init__(event_manager)
        self.report_repository = repository.ReportRepository(self.app)
        self.onReportDateChange()

    def onReportDateChange(self):
        calendar = self.ui.ReportCalendarWidget
        calendar_date = calendar.selectedDate().toPyDate()
        report = self.report_repository.findByDate(calendar_date)

        if not report:
            self.report_repository.create(date=calendar_date)
            report = self.report_repository.findByDate(calendar_date)

        self.report = report
        self.refreshUi()

    def refreshUi(self):
        if not getattr(self, 'report'):
            raise RuntimeError('Cannot refresh the MainWindow UI if there\'s no report loaded')

        print self.report
