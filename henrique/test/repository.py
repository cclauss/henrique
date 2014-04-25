# -*- coding: utf-8 -*-

import unittest
import os
import shutil
import sqlite3
import datetime

from henrique.repository import Repository, ReportRepository
from henrique.application import Henrique
from henrique.application import DATABASE

TEST_DATABASE = '/tmp/henrique_test.db'

class RepositoryTest(unittest.TestCase):

    class AppMock(object):
        dbfile = TEST_DATABASE

    def setUp(self):
        self.create_database()
        self.repository = Repository(self.AppMock())

    def create_database(self):
        if os.path.exists(TEST_DATABASE):
            os.remove(TEST_DATABASE)

        currentpath = os.path.dirname(os.path.realpath(__file__))
        sourcefile = os.path.realpath(os.path.join(currentpath, '..', '..', 'db', DATABASE))
        shutil.copy2(sourcefile, TEST_DATABASE)

    def test_database_connection(self):
        self.assertIsInstance(self.repository.connection, sqlite3.Connection)


class ReportRepositoryTest(RepositoryTest):

    def setUp(self):
        super(ReportRepositoryTest, self).setUp()
        self.seed()
        self.repository = ReportRepository(self.AppMock())

    def seed(self):
        conn = self.repository.connection
        for i in range(1, 10):
            status = ReportRepository.STATUS_SENT if (i % 2) == 0 else ReportRepository.STATUS_NOT_SENT
            query = """INSERT INTO
                            report(date, create_date, update_date, content, status)
                        VALUES
                            (date('now', '{0}'), date('now', '{1}'), date('now', '{2}'), 'Report for -{3} days', {4})
                    """
            params = ["-%d days" % i] * 3
            params.append(i)
            params.append(status)

            query = query.format(*params)
            conn.execute(query)

        conn.commit()

    def test_find_by_date(self):
        date = datetime.date.today() + datetime.timedelta(days=-1)
        reports = self.repository.findByDate(date)

        self.assertEquals(1, len(reports))

        report = reports[0]
        self.assertEquals(date.isoformat(), report['date'])
        self.assertEquals("Report for -1 days", report['content'])
        self.assertEquals(ReportRepository.STATUS_NOT_SENT, report['status'])
