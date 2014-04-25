# -*- coding: utf-8 -*-

import unittest
import os
import shutil
import sqlite3

from henrique.repository import Repository
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
