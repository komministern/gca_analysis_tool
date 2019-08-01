#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore, QtGui, QtWidgets

class TextPresenter(QtCore.QObject):

    def __init__(self, model, mainwindow, mainwindowpresenter):
        super(TextPresenter, self).__init__()
        self.model = model
        self.mainwindow = mainwindow
        self.mainwindowpresenter = mainwindowpresenter

        self.mainwindow.textBrowser_HistoryLog.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)


    # ---------- Text stuff

    def set_wrap_mode(self):
        self.mainwindow.textBrowser_HistoryLog.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
    
    def set_nowrap_mode(self):
        self.mainwindow.textBrowser_HistoryLog.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)

    
    def update_text(self):

        if self.mainwindowpresenter.active_site_name == u'':
            text = u''
        else:
            text = self.model.get_historylog(self.mainwindowpresenter.active_site_name, self.mainwindowpresenter.selected_date)
                
        self.mainwindow.textBrowser_HistoryLog.setPlainText(self.mainwindowpresenter.filtered_text(text))

        if self.mainwindowpresenter.string_to_highlight != u'' and text != u'No history log exists for this date.' and text != 'This date is in the list of ignored dates. You must deignore it before you can view the contents of the historylog.': 

            text = self.mainwindow.tabWidget_Search.tabText(0)
            if text[-1] != u'*':
                self.mainwindow.tabWidget_Search.setTabText(0, text + u'*')

            cursor = self.mainwindow.textBrowser_HistoryLog.textCursor()
            
            # Setup the desired format for matches
            format = QtGui.QTextCharFormat()
            format.setBackground(QtGui.QBrush(self.mainwindowpresenter.blue))

            pattern = self.mainwindowpresenter.string_to_highlight

            pos = 0
            index = self.mainwindow.textBrowser_HistoryLog.toPlainText().find(pattern)

            while (index != -1):

                # Select the matched text and apply the desired format
                cursor.setPosition(index)
                cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, len(pattern))
                cursor.mergeCharFormat(format)

                # Move to the next match
                pos = index + len(pattern)
                index = self.mainwindow.textBrowser_HistoryLog.toPlainText().find(pattern, pos)
            
        else:

            text = self.mainwindow.tabWidget_Search.tabText(0)
            if text[-1] == u'*':
                self.mainwindow.tabWidget_Search.setTabText(0, text[0:-1])
