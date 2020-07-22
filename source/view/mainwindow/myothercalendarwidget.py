"""
    This file is part of GCA Analysis Tool.

    Copyright (C) 2020 Oscar Franzén <oscarfranzen@protonmail.com>

    GCA Analysis Tool is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    GCA Analysis Tool is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with GCA Analysis Tool. If not, see <https://www.gnu.org/licenses/>.

"""


from PySide2 import QtCore, QtGui, QtWidgets

class MyOtherCalendarWidget(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)
        
        # This finally did the trick!!! Now the columns in the calendar widget
        # automatically fills the widget, despite the font size.
        #self.tableView = self.findChild(QtWidgets.QTableView)
        #self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        #for i in range(8):
        #    self.tableView.horizontalHeader().resizeSection(i, 38)
        
        self.setFirstDayOfWeek(QtCore.Qt.DayOfWeek.Monday)
        #self.setHorizontalHeaderFormat(QtGui.QCalendarWidget.SingleLetterDayNames)

        self.from_date = self.selectedDate()
        self.until_date = self.selectedDate()

    def paintCell(self, painter, rect, date):

        if date >= self.from_date and date <= self.until_date:
            painter.fillRect(rect, QtGui.QColor('lightgreen'))
        
        painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))