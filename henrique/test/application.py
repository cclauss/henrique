# -*- coding: utf-8 -*-

import unittest
import os
from henrique.application import Henrique
from henrique.application import DATABASE

class HenriqueTest(unittest.TestCase):

    def test_argument_parsing(self):
        args = ['run.py', '--home-dir=/tmp']
        app = Henrique(args)
        self.assertEquals("/tmp", app.home)

        app = Henrique([])
        self.assertNotEquals(app.home, None)

    def test_create_database(self):
        args = ['run.py', '--home-dir=/tmp']
        app = Henrique(args)

        dbfile = os.path.realpath(os.path.join("/tmp", DATABASE))
        self.assertTrue(os.path.exists(dbfile), "Failed asserting that the database file exists")
