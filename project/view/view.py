#!/usr/bin/env python
# -*- coding: utf-8 -*-


#    Copyright © 2016, 2017 Oscar Franzén <oscarfranzen@yahoo.se>
#
#    This file is part of GCA Analysis Tool.

import math
from PySide import QtGui, QtCore
from ui_mainwindow import Ui_MainWindow
#from licensewindow import MyLicenseWindow


class MyView(QtGui.QMainWindow, Ui_MainWindow):

    quit = QtCore.Signal()

    def __init__(self, **kwds):
        super(MyView, self).__init__(**kwds)
        
        # This is for the munu to get the right font !?!
        #font = self.font()
        #font.setPointSize(8)
        #pixelsize = math.floor(406.0 / 24)
        #font.setPixelSize(pixelsize)
        #self.setFont(font)
        
        #print font.pixelSize()
        
        self.setupUi(self)
        
        width_of_textedit = self.plainTextEdit_StringSearch.geometry().width()
        pixelsize_standard = int(width_of_textedit / 24.0)
        pixelsize_calendar = int(width_of_textedit / 24.0 * 0.87)

        font = self.font()
        font.setPixelSize(pixelsize_standard)
        self.setFont(font)

        font = self.calendarWidget.font()
        font.setPixelSize(pixelsize_calendar)
        self.calendarWidget.setFont(font)
        
        #font = self.plainTextEdit_StringSearch.font()
        #font.setPointSize(8)
        #width_of_textedit = self.plainTextEdit_StringSearch.geometry().width()
        #font_metrics = QtGui.QFontMetrics(font)
        #width_of_string = font_metrics.width(u'aaaaaaaaaaaaaaaaaaaaaaa')
        #width_of_string = font_metrics.width(u'aaaaaaaaaaaaaaaaaaaaaaa')
        #print width_of_textedit
        #print width_of_string
        
        
        #font = self.calendarWidget.font()
        #font.setPointSize(7)
        #self.calendarWidget.setFont(font)
        
        self.setupMenu()

    def close(self):
        self.quit.emit()

    def closeEvent(self, event):
        event.ignore()
        self.quit.emit() 

    def setupMenu(self):
        
        self.importAction = QtGui.QAction('Import...', self)
        self.importAction.setStatusTip('Import history log from a capturesite file')

        self.ignoreAction = QtGui.QAction('Add active date', self)
        self.ignoreAction.setStatusTip('Place active date in the ignore list')
        self.deIgnoreAction = QtGui.QAction('Remove all dates', self)
        self.deIgnoreAction.setStatusTip('Clear all dates in ignore list')

#        self.aboutAction = QtGui.QAction('&About GCA Analysis Tool', self)
#        self.aboutAction.setStatusTip('About...')

        menubar = self.menuBar()
        
        #menubar.setFont(self.myfont)

        capturesite_menu = menubar.addMenu('Capturesite')
        capturesite_menu.addAction(self.importAction)

        database_menu = menubar.addMenu('Ignorelist')
        database_menu.addAction(self.ignoreAction)
        database_menu.addAction(self.deIgnoreAction)

#        statistics_menu = menubar.addMenu('&Statistics')

        self.aboutAction = QtGui.QAction('this program...', self)
        #menubar.addAction(self.aboutAction)
#        menubar.addAction('Test')
        about_menu = menubar.addMenu('About')
        about_menu.addAction(self.aboutAction)



#menu.addAction(QtGui.QAction('50%', menu, checkable=True))

#        database_menu = menubar.addMenu('&Ignorelist')
#        database_menu.addAction(self.ignoreAction)
#        database_menu.addAction(self.deIgnoreAction)
