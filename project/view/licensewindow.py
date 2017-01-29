#!/usr/bin/env python
# -*- coding: utf-8 -*-


#    Copyright © 2016, 2017 Oscar Franzén <oscarfranzen@yahoo.se>
#
#    This file is part of GCA Analysis Tool.


#import os
#import string
from PySide import QtCore, QtGui
#from coloringcontainer import ColoringContainer
#import textstuff as txt

class MyLicenseWindow(QtGui.QTextBrowser):

    def __init__(self, **kwds):
	super(MyLicenseWindow, self).__init__(**kwds)

        self.setPlainText(u'''
GCA Analysis Tool, v0.9 Trial

This is a trial version of the GCA Analysis Tool. It will be fully usable 
during 2017. For further use, contact me.

Copyright © 2016, 2017 Oscar Franzén <oscarfranzen@protonmail.com>



''')
        self.setGeometry(300, 300, 600, 600)

        self.show()
