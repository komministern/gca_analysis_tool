#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


#import os 
#import string
#import time
from PySide2 import QtCore, QtGui, QtWidgets
#from presenter.coloringcontainer import ColoringContainer
#import presenter.textstuff as txt
#from presenter.filtercontainer import Filter
#from view.myfilterdialog import MyFilterDialog
#from presenter.eventfilter import EventBlocker




class TextPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        super(TextPresenter, self).__init__()
        self.model = model
        self.view = view
        self.presenter = presenter


    # ---------- Text stuff


    def update_text(self):

        date = self.view.mainwindow.calendarWidget.selectedDate()
        if self.presenter.mainwindow.active_site_name == u'':
            text = u''
        else:
            text = self.model.get_historylog(self.presenter.mainwindow.active_site_name, date)
                
        self.view.mainwindow.textBrowser_HistoryLog.setPlainText(self.presenter.mainwindow.format_text(text))

        if self.presenter.mainwindow.highlight != u'' and text != u'No history log exists for this date.': 

            #palette = QtGui.QPalette()
            #palette.setColor(QtGui.QPalette.Base,QtCore.Qt.blue)
            #self.view.lineEdit_StringSearch.setPalette(palette)

            text = self.view.mainwindow.tabWidget_Search.tabText(0)
            if text[-1] != u'*':
                self.view.mainwindow.tabWidget_Search.setTabText(0, text + u'*')

            cursor = self.view.mainwindow.textBrowser_HistoryLog.textCursor()
            
            # Setup the desired format for matches
            format = QtGui.QTextCharFormat()
            format.setBackground(QtGui.QBrush(self.presenter.mainwindow.blue))


            pattern = self.presenter.mainwindow.highlight

            pos = 0
            index = self.view.mainwindow.textBrowser_HistoryLog.toPlainText().find(pattern)

            while (index != -1):

                # Select the matched text and apply the desired format
                cursor.setPosition(index)
                cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, len(pattern))
                cursor.mergeCharFormat(format)

                # Move to the next match
                pos = index + len(pattern)
                index = self.view.mainwindow.textBrowser_HistoryLog.toPlainText().find(pattern, pos)

            # This is a dirty fix for a bizarre problem. If this is omitted, only part of the text will be displayed after a
            # search!!! Weird.
            self.view.mainwindow.textBrowser_HistoryLog.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
            self.view.mainwindow.textBrowser_HistoryLog.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
            
        else:
                
            text = self.view.mainwindow.tabWidget_Search.tabText(0)
            if text[-1] == u'*':
                self.view.mainwindow.tabWidget_Search.setTabText(0, text[0:-1])

        self.presenter.mainwindow.update_comment()   # Here?????????????????????????