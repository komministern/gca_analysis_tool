#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


#import math
#import os
from PySide2 import QtGui, QtCore, QtWidgets
from view.mainwindow.mymainwindow import MyMainWindow
from view.resultswindow.myresultswindow import MyResultsWindow
#from ui_mainwindow import Ui_MainWindow
#from view.ui_mainwindow import Ui_MainWindow
#from view.ui_menu import setupMenu
#from licensewindow import MyLicenseWindow


class MyView(QtCore.QObject):

    def __init__(self, **kwds):
        super(MyView, self).__init__(**kwds)

        self.resultswindows = {}

        # Create mainwindow
    def create_mainwindow(self):
        self.mainwindow = MyMainWindow()
        print('created mainwindow')

        # Create a resultswindow
    def create_resultswindow(self, handle):
        self.resultswindows[handle] = MyResultsWindow()
        print('created window ' + str(handle))

    def destroy_resultswindow(self, handle):
        self.resultswindows[handle].destroy()
        del self.resultswindows[handle]
        print('destroyed window ' + str(handle))
                
    