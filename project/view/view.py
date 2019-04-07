#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


#import math
#import os
from PySide2 import QtGui, QtCore, QtWidgets
from view.mainwindow.mymainwindow import MyMainWindow
#from ui_mainwindow import Ui_MainWindow
#from view.ui_mainwindow import Ui_MainWindow
#from view.ui_menu import setupMenu
#from licensewindow import MyLicenseWindow


class MyView(QtCore.QObject):

    def __init__(self, **kwds):
        super(MyView, self).__init__(**kwds)

        self.mainwindow = MyMainWindow()
                
