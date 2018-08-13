# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
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




class SearchPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        super(SearchPresenter, self).__init__()
        self.model = model
        self.view = view
        self.presenter = presenter

        self.highlight = ''

    
        # ------------ String search stuff

    def commit_string_search(self):
        
        self.highlight = self.view.plainTextEdit_StringSearch.toPlainText()

        self.view.calendarWidget.setCircledDates(self.list_of_search_string_dates(self.view.plainTextEdit_StringSearch.toPlainText()))
        
        self.view.calendarWidget.updateCells()
        self.presenter.update_text()

            # Lets set highlight in the plainTextEdit text here!!!
            
            #print self.view.lineEdit_StringSearch.textCursor()
        cursor = self.view.plainTextEdit_StringSearch.textCursor()
            #self.view.lineEdit_StringSearch.end(False)

        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(self.presenter.blue))

        # Select the matched text and apply the desired format
        cursor.setPosition(0)
        
        cursor.movePosition(QtGui.QTextCursor.End, QtGui.QTextCursor.KeepAnchor, 1)
            
        self.ignore = True
            
        cursor.mergeCharFormat(format)
            




    def list_of_search_string_dates(self, astring):
        if not astring == '' and not self.presenter.active_site_name == u'':
            return [date for date, text in self.model.get_historylog_dictionary(self.presenter.active_site_name).items() if astring in text]
        else:
            return []


    def reset_string_search(self):
        
        cursor = self.view.plainTextEdit_StringSearch.textCursor()

        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtCore.Qt.white))
        # Select the matched text and apply the desired format
        cursor.setPosition(0)
        cursor.movePosition(QtGui.QTextCursor.End, QtGui.QTextCursor.KeepAnchor, 1)
        self.ignore = True
        cursor.mergeCharFormat(format)
        
        
        
        self.view.calendarWidget.setCircledDates([])
        self.view.plainTextEdit_StringSearch.setPlainText(u'')
        self.highlight = u''
        self.view.calendarWidget.updateCells()
        self.presenter.update_text()




    def set_next_search_date(self):
        if not self.presenter.active_site_name == u'':
            dates = sorted(self.list_of_search_string_dates(self.view.plainTextEdit_StringSearch.toPlainText()))
            if not len(dates) == 0:
                greater_dates = [date for date in dates if date > self.view.calendarWidget.selectedDate()]

                if len(greater_dates) == 0:
                    new_index = 0
                else:
                    new_index = dates.index(greater_dates[0])
                self.view.calendarWidget.setSelectedDate(dates[new_index])
                self.view.calendarWidget.updateCells()


    def set_previous_search_date(self):
        if not self.presenter.active_site_name == u'':
            dates = sorted(self.list_of_search_string_dates(self.view.plainTextEdit_StringSearch.toPlainText()))
            if not len(dates) == 0:
                lesser_dates = [date for date in dates if date < self.view.calendarWidget.selectedDate()]
                if len(lesser_dates) == 0:
                    new_index = -1
                else:
                    new_index = dates.index(lesser_dates[-1])            
                self.view.calendarWidget.setSelectedDate(dates[new_index])
                self.view.calendarWidget.updateCells()


    def text_changed(self):
        
        if not self.highlight == u'' and not self.ignore:
            
            self.highlight = u''
            self.presenter.text_presenter.update_text()

            self.view.calendarWidget.setCircledDates([])
            self.view.calendarWidget.updateCells()
            
            cursor = self.view.plainTextEdit_StringSearch.textCursor()
            #self.view.lineEdit_StringSearch.end(False)

            format = QtGui.QTextCharFormat()
            format.setBackground(QtGui.QBrush(QtCore.Qt.white))
            #print self.test

        
            # Select the matched text and apply the desired format
            cursor.setPosition(0)
            cursor.movePosition(QtGui.QTextCursor.EndOfLine, QtGui.QTextCursor.KeepAnchor, 1)
            cursor.mergeCharFormat(format)

        self.ignore = False

    def return_pressed(self):
        self.view.pushButton_CommitStringSearch.animateClick()
        self.view.pushButton_CommitStringSearch.clicked.emit()