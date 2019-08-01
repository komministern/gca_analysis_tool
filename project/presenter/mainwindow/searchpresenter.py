#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore, QtGui, QtWidgets


class SearchPresenter(QtCore.QObject):

    def __init__(self, model, mainwindow, mainwindowpresenter):
        super(SearchPresenter, self).__init__()
        self.model = model
        self.mainwindow = mainwindow
        self.mainwindowpresenter = mainwindowpresenter

        self.string_to_highlight = ''

        self.mainwindow.pushButton_CommitStringSearch.setEnabled(False)
        self.mainwindow.pushButton_PreviousSearch.setEnabled(False)
        self.mainwindow.pushButton_NextSearch.setEnabled(False)

    
        # ------------ String search stuff

    def commit_string_search(self):

        if self.mainwindow.plainTextEdit_StringSearch.toPlainText() != '':
            self.mainwindow.pushButton_NextSearch.setEnabled(True)
            self.mainwindow.pushButton_PreviousSearch.setEnabled(True)

        self.string_to_highlight = self.mainwindow.plainTextEdit_StringSearch.toPlainText()

        self.mainwindowpresenter.set_search_hit_dates(self.list_of_search_string_dates(self.string_to_highlight))
        
        self.mainwindowpresenter.update_calendar_cells()
        self.mainwindowpresenter.update_text()

        cursor = self.mainwindow.plainTextEdit_StringSearch.textCursor()

        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(self.mainwindowpresenter.blue))

        # Select the matched text and apply the desired format
        cursor.setPosition(0)
        
        cursor.movePosition(QtGui.QTextCursor.End, QtGui.QTextCursor.KeepAnchor, 1)
            
        self.ignore = True
            
        cursor.mergeCharFormat(format)



    def list_of_search_string_dates(self, astring):
        if not astring == '' and not self.mainwindowpresenter.active_site_name == u'':
            return [date for date, text in self.model.get_historylog_dictionary(self.mainwindowpresenter.active_site_name).items() if astring in text]
        else:
            return []


    def reset_string_search(self):
        
        cursor = self.mainwindow.plainTextEdit_StringSearch.textCursor()

        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtCore.Qt.white))
        
        # Select the matched text and apply the desired format
        cursor.setPosition(0)
        cursor.movePosition(QtGui.QTextCursor.End, QtGui.QTextCursor.KeepAnchor, 1)
        self.ignore = True
        cursor.mergeCharFormat(format)
        
        self.mainwindowpresenter.set_search_hit_dates([])

        self.mainwindow.plainTextEdit_StringSearch.setPlainText(u'')
        self.string_to_highlight = u''

        self.mainwindowpresenter.update_calendar_cells()
        self.mainwindowpresenter.update_text()




    def set_next_search_date(self):
        if not self.mainwindowpresenter.active_site_name == u'':
            dates = sorted(self.list_of_search_string_dates(self.mainwindow.plainTextEdit_StringSearch.toPlainText()))
            if not len(dates) == 0:
                greater_dates = [date for date in dates if date > self.mainwindow.calendarWidget.selectedDate()]

                if len(greater_dates) == 0:
                    new_index = 0
                else:
                    new_index = dates.index(greater_dates[0])
                
                self.mainwindowpresenter.selected_date = dates[new_index]
                self.mainwindowpresenter.update_calendar_cells()


    def set_previous_search_date(self):
        if not self.mainwindowpresenter.active_site_name == u'':
            dates = sorted(self.list_of_search_string_dates(self.mainwindow.plainTextEdit_StringSearch.toPlainText()))
            if not len(dates) == 0:
                lesser_dates = [date for date in dates if date < self.mainwindow.calendarWidget.selectedDate()]
                if len(lesser_dates) == 0:
                    new_index = -1
                else:
                    new_index = dates.index(lesser_dates[-1])            
                
                self.mainwindowpresenter.selected_date = dates[new_index]
                self.mainwindowpresenter.update_calendar_cells()


    def text_changed(self):
        
        if self.mainwindow.plainTextEdit_StringSearch.toPlainText() != '':
            self.mainwindow.pushButton_CommitStringSearch.setEnabled(True)
        else:
            self.mainwindow.pushButton_CommitStringSearch.setEnabled(False)

        if self.string_to_highlight != u'' and not self.ignore:
            
            self.mainwindow.pushButton_PreviousSearch.setEnabled(False)
            self.mainwindow.pushButton_NextSearch.setEnabled(False)

            self.string_to_highlight = u''
            self.mainwindowpresenter.update_text()

            self.mainwindowpresenter.set_search_hit_dates([])
            self.mainwindowpresenter.update_calendar_cells()
            
            cursor = self.mainwindow.plainTextEdit_StringSearch.textCursor()

            format = QtGui.QTextCharFormat()
            format.setBackground(QtGui.QBrush(QtCore.Qt.white))
        
            # Select the matched text and apply the desired format
            cursor.setPosition(0)
            cursor.movePosition(QtGui.QTextCursor.EndOfLine, QtGui.QTextCursor.KeepAnchor, 1)
            cursor.mergeCharFormat(format)

        self.ignore = False

    def return_pressed(self):
        if self.mainwindow.plainTextEdit_StringSearch.toPlainText() != '':
            self.mainwindow.pushButton_CommitStringSearch.animateClick()
            self.mainwindow.pushButton_CommitStringSearch.clicked.emit()