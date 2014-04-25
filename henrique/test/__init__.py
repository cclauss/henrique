# -*- coding: utf-8 -*-

import unittest
import utils

class TestSuite(object):

    def __init__(self):
        self.suite = unittest.TestSuite()
        self.suite.addTest(utils.UiFactoryTest())

    def run(self):
        runner = unittest.TextTestRunner()
        runner.run(self.suite)
