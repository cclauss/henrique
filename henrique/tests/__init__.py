# -*- coding: utf-8 -*-

import unittest
import application
import models

class TestSuite(object):

    def __init__(self):
        self.suite = unittest.TestSuite()
        self.suite.addTest(unittest.findTestCases(application))
        self.suite.addTest(unittest.findTestCases(models))

    def run(self):
        runner = unittest.TextTestRunner()
        runner.run(self.suite)
