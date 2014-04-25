# -*- coding: utf-8 -*-

import sqlite3
import datetime

class Repository(object):

    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    DATE_FORMAT = "%Y-%m-%d"

    datetime_fields = []

    def __init__(self, app):
        self.connection = sqlite3.connect(app.dbfile)
        self.connection.row_factory = self.cursorToDictionary

    def cursorToDictionary(self, cursor, row):
        d = {}

        for idx, col in enumerate(cursor.description):
            if col[0] in self.datetime_fields:
                d[col[0]] = self.parseDateTime(row[idx])
            else:
                d[col[0]] = row[idx]

        return d

    def parseDateTime(self, datetimestr):
        return datetime.datetime.strptime(datetimestr, self.DATETIME_FORMAT)


class ReportRepository(Repository):
    STATUS_SENT = 1
    STATUS_NOT_SENT = 0

    datetime_fields = ['date', 'create_date', 'update_date']

    def findByDate(self, date):
        query = "SELECT *, strftime('%Y-%m-%d', date) AS report_date FROM report WHERE report_date=(?)"
        cursor = self.connection.execute(query, (date.strftime(self.DATE_FORMAT),))
        return cursor.fetchall()

    def create(self, date=None, content='', status=0):
        create_date = datetime.datetime.now().strftime(self.DATETIME_FORMAT)

        query = "INSERT INTO report(date, create_date, update_date, content, status) VALUES (?, ?, ?, ?, ?)"
        self.connection.execute(query, (date, create_date, create_date, content, status,))
        self.connection.commit()
