#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import sys
    from henrique.application import Henrique

    app = Henrique(sys.argv)
    app.start()
