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


class Filter(QtCore.QObject):

    def __init__(self):
        super(Filter, self).__init__()

        self.suppress = []
        self.show = []

        self.name = u''


