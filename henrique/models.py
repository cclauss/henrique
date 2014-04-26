# -*- coding: utf-8 -*-

import sqlite3
from datetime import datetime, date

class Model(object):

    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    DATE_FORMAT = "%Y-%m-%d"
    WRITES_PENDING = 0
    MAX_WRITES_PENDING = 50

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
        return datetime.strptime(datetimestr, self.DATETIME_FORMAT)

    def flagWrite(self):
        self.WRITES_PENDING += 1

        if (self.WRITES_PENDING >= self.MAX_WRITES_PENDING):
            self.connection.commit()
            self.WRITES_PENDING = 0


class ReportModel(Model):
    STATUS_SENT = 1
    STATUS_NOT_SENT = 0

    datetime_fields = ['date', 'create_date', 'update_date']

    def findByDate(self, date):
        query = "SELECT *, strftime('%Y-%m-%d', date) AS report_date FROM report WHERE report_date=(?)"
        cursor = self.connection.execute(query, (date.strftime(self.DATE_FORMAT),))
        reports = cursor.fetchall()
        cursor.close()
        return reports

    def findById(self, id):
        cursor = self.connection.execute("SELECT * FROM report WHERE id=?", (id,))
        report = cursor.fetchone()
        cursor.close()
        return report

    def create(self, date=None, content='', status=0):
        create_date = datetime.now().strftime(self.DATETIME_FORMAT)
        cursor = self.connection.cursor()
        date = date if isinstance(date, datetime) else datetime.combine(date, datetime.min.time())

        query = "INSERT INTO report(date, create_date, update_date, content, status) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (date, create_date, create_date, content, status,))
        cursor.close()

        self.flagWrite()

        return cursor.lastrowid

    def update(self, id, content='', status=0):
        update_date = datetime.now().strftime(self.DATETIME_FORMAT)
        cursor = self.connection.cursor()
        query = "UPDATE report SET update_date=?, content=?, status=? WHERE id=?"
        params = (update_date, content, status, id,)
        cursor.execute(query, params)
        cursor.close()

        self.flagWrite()
