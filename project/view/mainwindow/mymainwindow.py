#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


#import math
import os
from PySide2 import QtGui, QtCore, QtWidgets
#from ui_mainwindow import Ui_MainWindow
from view.ui.ui_mainwindow import Ui_MainWindow
#from view.ui_menu import setupMenu
#from licensewindow import MyLicenseWindow


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    quit = QtCore.Signal()

    def __init__(self, **kwds):
        super(MyMainWindow, self).__init__(**kwds)
                
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('gca.ico'))
        
        #width_of_textedit = self.plainTextEdit_StringSearch.geometry().width()
        #self.pixelsize_standard = int(round(width_of_textedit / 24.0) * 0.9)
        #self.pixelsize_calendar = int(width_of_textedit / 24.0 * 0.81)
        #self.pixelsize_calendar = int(round(width_of_textedit / 24.0 * 0.78))

        #font = self.font()
        #font.setPixelSize(self.pixelsize_standard)
        #self.setFont(font)

        #font = self.calendarWidget.font()
        #font.setPixelSize(self.pixelsize_calendar)
        #self.calendarWidget.setFont(font)
        
        #view.comboBox_ActiveSite.setFixedWidth(comboBox_Coloring_width * 2.0 / 3.0)
        #print(self.comboBox_ActiveSite.sizePolicy())
        #self.comboBox_ActiveSite.sizePolicy().setWidthForHeight(True)
        #print(self.comboBox_ActiveSite.sizePolicy().hasWidthForHeight())

        
        
        self.setupMenu()

        

    #def mousePressEvent(self, event):
    #    print 'clicked'
        


    #def close(self):
    #    self.quit.emit()

    def closeEvent(self, event):
        event.ignore()
        self.quit.emit() 

    def setupMenu(self):
        
        self.importAction = QtWidgets.QAction('Import...', self)
        self.importAction.setStatusTip('Import history log from a capturesite file')

        self.ignoreAction = QtWidgets.QAction('Add active date', self)
        self.ignoreAction.setStatusTip('Place active date in the ignore list')

        self.deIgnoreAction = QtWidgets.QAction('Remove all dates', self)
        self.deIgnoreAction.setStatusTip('Clear all dates in ignore list')

        self.analysisAction = QtWidgets.QAction('Graph analyzer...', self)
        self.analysisAction.setStatusTip('Analyze history log between two dates')

        self.wrapActionGroup = QtWidgets.QActionGroup(self)
        self.wrapAction = QtWidgets.QAction('Wrap', self.wrapActionGroup)
        self.noWrapAction = QtWidgets.QAction('No Wrap', self.wrapActionGroup)
        

#        self.aboutAction = QtGui.QAction('&About GCA Analysis Tool', self)
#        self.aboutAction.setStatusTip('About...')

        menubar = self.menuBar()
        
        #font = menubar.font()
        #font.setPixelSize(self.pixelsize_standard)     # This does not work!!!
        #font.setPointSize(9)
        #menubar.setFont(font)
        
        #menubar.setFont(self.myfont)

        file_menu = menubar.addMenu('File')
        file_menu.addAction(self.importAction)

        tools_menu = menubar.addMenu('Tools')
        tools_menu.addAction(self.analysisAction)

        view_menu = menubar.addMenu('View')

        text_menu = view_menu.addMenu('Text')
        text_menu.addAction(self.noWrapAction)
        text_menu.addAction(self.wrapAction)


        ignore_menu = QtWidgets.QMenu('Ignore list')
        ignore_menu.addAction(self.ignoreAction)
        ignore_menu.addAction(self.deIgnoreAction)

        tools_menu.addMenu(ignore_menu)

        #database_menu.addAction(self.ignoreAction)
        #database_menu.addAction(self.deIgnoreAction)

#        statistics_menu = menubar.addMenu('&Statistics')

        self.aboutAction = QtWidgets.QAction('About GCA Analysis Tool', self)

        #menubar.addAction(self.aboutAction)
#        menubar.addAction('Test')
        help_menu = menubar.addMenu('Help')
        help_menu.addAction(self.aboutAction)



#menu.addAction(QtGui.QAction('50%', menu, checkable=True))

#        database_menu = menubar.addMenu('&Ignorelist')
#        database_menu.addAction(self.ignoreAction)
#        database_menu.addAction(self.deIgnoreAction)
