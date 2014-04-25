# -*- coding: utf-8 -*-

import unittest

class TestSuite(object):

    def __init__(self):
        self.suite = unittest.TestSuite()

    def run(self):
        runner = unittest.TextTestRunner()
        runner.run(self.suite)
