#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore, QtGui, QtWidgets


class SearchPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        super(SearchPresenter, self).__init__()
        self.model = model
        self.view = view
        self.presenter = presenter

        self.highlight = ''

    
        # ------------ String search stuff

    def commit_string_search(self):
        
        self.highlight = self.view.mainwindow.plainTextEdit_StringSearch.toPlainText()

        self.view.mainwindow.calendarWidget.setCircledDates(self.list_of_search_string_dates(self.view.mainwindow.plainTextEdit_StringSearch.toPlainText()))
        
        self.view.mainwindow.calendarWidget.updateCells()
        self.presenter.mainwindow.update_text()

            # Lets set highlight in the plainTextEdit text here!!!
            
            #print self.view.lineEdit_StringSearch.textCursor()
        cursor = self.view.mainwindow.plainTextEdit_StringSearch.textCursor()
            #self.view.lineEdit_StringSearch.end(False)

        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(self.presenter.mainwindow.blue))

        # Select the matched text and apply the desired format
        cursor.setPosition(0)
        
        cursor.movePosition(QtGui.QTextCursor.End, QtGui.QTextCursor.KeepAnchor, 1)
            
        self.ignore = True
            
        cursor.mergeCharFormat(format)
            




    def list_of_search_string_dates(self, astring):
        if not astring == '' and not self.presenter.mainwindow.active_site_name == u'':
            return [date for date, text in self.model.get_historylog_dictionary(self.presenter.mainwindow.active_site_name).items() if astring in text]
        else:
            return []


    def reset_string_search(self):
        
        cursor = self.view.mainwindow.plainTextEdit_StringSearch.textCursor()

        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtCore.Qt.white))
        # Select the matched text and apply the desired format
        cursor.setPosition(0)
        cursor.movePosition(QtGui.QTextCursor.End, QtGui.QTextCursor.KeepAnchor, 1)
        self.ignore = True
        cursor.mergeCharFormat(format)
        
        
        
        self.view.mainwindow.calendarWidget.setCircledDates([])
        self.view.mainwindow.plainTextEdit_StringSearch.setPlainText(u'')
        self.highlight = u''
        self.view.mainwindow.calendarWidget.updateCells()
        self.presenter.mainwindow.update_text()




    def set_next_search_date(self):
        if not self.presenter.mainwindow.active_site_name == u'':
            dates = sorted(self.list_of_search_string_dates(self.view.mainwindow.plainTextEdit_StringSearch.toPlainText()))
            if not len(dates) == 0:
                greater_dates = [date for date in dates if date > self.view.mainwindow.calendarWidget.selectedDate()]

                if len(greater_dates) == 0:
                    new_index = 0
                else:
                    new_index = dates.index(greater_dates[0])
                self.view.mainwindow.calendarWidget.setSelectedDate(dates[new_index])
                self.view.mainwindow.calendarWidget.updateCells()


    def set_previous_search_date(self):
        if not self.presenter.mainwindow.active_site_name == u'':
            dates = sorted(self.list_of_search_string_dates(self.view.mainwindow.plainTextEdit_StringSearch.toPlainText()))
            if not len(dates) == 0:
                lesser_dates = [date for date in dates if date < self.view.mainwindow.calendarWidget.selectedDate()]
                if len(lesser_dates) == 0:
                    new_index = -1
                else:
                    new_index = dates.index(lesser_dates[-1])            
                self.view.mainwindow.calendarWidget.setSelectedDate(dates[new_index])
                self.view.mainwindow.calendarWidget.updateCells()


    def text_changed(self):
        
        if not self.highlight == u'' and not self.ignore:
            
            self.highlight = u''
            self.presenter.mainwindow.update_text()

            self.view.mainwindow.calendarWidget.setCircledDates([])
            self.view.mainwindow.calendarWidget.updateCells()
            
            cursor = self.view.mainwindow.plainTextEdit_StringSearch.textCursor()
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
        self.view.mainwindow.pushButton_CommitStringSearch.animateClick()
        self.view.mainwindow.pushButton_CommitStringSearch.clicked.emit()