# -*- coding: utf-8 -*-

import sqlite3
from datetime import datetime, date

class Model(object):

    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    DATE_FORMAT = "%Y-%m-%d"
    WRITES_PENDING = 0
    MAX_WRITES_PENDING = 50

    datetime_fields = []
    connection = None

    def __init__(self, app):
        self.connect(app)

    @classmethod
    def cursorToDictionary(cls, cursor, row):
        d = {}

        for idx, col in enumerate(cursor.description):
            if col[0] in cls.datetime_fields:
                d[col[0]] = cls.parseDateTime(row[idx])
            else:
                d[col[0]] = row[idx]

        return d

    @classmethod
    def parseDateTime(cls, datetimestr):
        return datetime.strptime(datetimestr, cls.DATETIME_FORMAT)

    @staticmethod
    def connect(app):
        if Model.connection is None:
            Model.connection = sqlite3.connect(app.dbfile)
            Model.connection.row_factory = Model.cursorToDictionary

    @staticmethod
    def flagWrite():
        Model.WRITES_PENDING += 1

        if (Model.WRITES_PENDING >= Model.MAX_WRITES_PENDING):
            Model.connection.commit()
            Model.WRITES_PENDING = 0

class SettingsModel(Model):

    TAG_SMTP = 'smtp'
    SETTINGS_SMTP = {
        'address': '127.0.0.1',
        'port': '25',
        'username': 'henrique@candyland.com',
        'password': '123456',
        'ssl': '0'
    }


    def findSMTPSettings(self):
        cursor = self.connection.execute("SELECT * FROM setting WHERE tag=?", (self.TAG_SMTP,))
        dbsettings = cursor.fetchall()
        cursor.close()

        settings = {}
        validkeys = self.SETTINGS_SMTP.keys()

        for setting in dbsettings:
            if setting['name'] in validkeys:
                settings[setting['name']] = setting['value']

        finalsettings = self.SETTINGS_SMTP.copy()
        finalsettings.update(settings)

        return finalsettings

    def saveSMTPSettings(self, settings):
        self.connection.execute("DELETE FROM setting WHERE tag=?", (self.TAG_SMTP,))

        finalsettings = self.SETTINGS_SMTP.copy()
        finalsettings.update(settings)

        query = "INSERT INTO setting (name, value, tag)" + (" VALUES (?, ?, ?) " * len(finalsettings))
        print query


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
