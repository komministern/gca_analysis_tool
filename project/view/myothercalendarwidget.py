#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore, QtGui, QtWidgets

class MyOtherCalendarWidget(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)
        
        # This finally did the trick!!! Now the columns in the calendar widget
        # automatically fills the widget, despite the font size.
        self.tableView = self.findChild(QtWidgets.QTableView)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        for i in range(8):
            self.tableView.horizontalHeader().resizeSection(i, 38)
        
        self.setFirstDayOfWeek(QtCore.Qt.DayOfWeek.Monday)
        #self.setHorizontalHeaderFormat(QtGui.QCalendarWidget.SingleLetterDayNames)

        self.from_date = self.selectedDate()
        self.until_date = self.selectedDate()

    def paintCell(self, painter, rect, date):

        if date >= self.from_date and date <= self.until_date:
            painter.fillRect(rect, QtGui.QColor('lightgreen'))
        
        painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))