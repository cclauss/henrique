# -*- coding: utf-8 -*-

import sqlite3

class Repository(object):

    def __init__(self, app):
        self.connection = sqlite3.connect(app.dbfile)
