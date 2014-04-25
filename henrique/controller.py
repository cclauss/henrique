# -*- coding: utf-8 -*-

import repository

class MainWindowController(object):

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.report_repository = repository.ReportRepository()
