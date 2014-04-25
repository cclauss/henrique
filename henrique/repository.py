# -*- coding: utf-8 -*-

import sqlite3

class Repository(object):
    def __init__(self, app):
        self.connection = sqlite3.connect(app.dbfile)
        self.connection.row_factory = self.cursorToDictionary

    def cursorToDictionary(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]

        return d

class ReportRepository(Repository):
    STATUS_SENT = 1
    STATUS_NOT_SENT = 0

    def findByDate(self, date):
        query = "SELECT * FROM report WHERE date=date(?)"
        cursor = self.connection.execute(query, (date.isoformat(),))
        return cursor.fetchall()
