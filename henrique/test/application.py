# -*- coding: utf-8 -*-

import unittest
from henrique.application import Henrique

class HenriqueTest(unittest.TestCase):

    def test_argument_parsing(self):
        args = ['run.py', '--HOME=/tmp']
        app = Henrique(args)
        self.assertEquals("/tmp", app.home)

        args = ['--HOME=/tmp']
        app = Henrique(args)
        self.assertEquals("/tmp", app.home)
