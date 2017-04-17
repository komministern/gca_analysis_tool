#!/usr/bin/env python
# -*- coding: utf-8 -*-


#    Copyright � 2016, 2017 Oscar Franz�n <oscarfranzen@yahoo.se>
#
#    This file is part of GCA Analysis Tool.


#import os
#import string
from PySide import QtCore, QtGui
#from coloringcontainer import ColoringContainer
#import textstuff as txt


class Filter(QtCore.QObject):

    SUPPRESS = 0
    SHOWONLY = 1

    def __init__(self):
        super(Filter, self).__init__()

        self.content = []
        self.state = self.SUPPRESS

        self.name = u''


