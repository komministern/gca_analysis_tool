#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore, QtGui, QtWidgets


class MyCalendarWidget(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)
        
        #print(parent)

        # This finally did the trick!!! Now the columns in the calendar widget
        # automatically fills the widget, despite the font size.
        #self.tableView = self.findChild(QtWidgets.QTableView)
        #self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        #for i in range(8):
        #    self.tableView.horizontalHeader().resizeSection(i, 38)
        
        self.setFirstDayOfWeek(QtCore.Qt.DayOfWeek.Monday)
        #self.setHorizontalHeaderFormat(QtGui.QCalendarWidget.SingleLetterDayNames)

        self.setCircledDates([])
        self.setTriangleDates([])
        #self.setIgnoredDates([])

        self.upper_left_red_dates = []
        self.upper_left_green_dates = []
        self.upper_left_yellow_dates = []
        self.upper_left_white_dates = []
        self.lower_right_red_dates = []
        self.lower_right_green_dates = []
        self.lower_right_yellow_dates = []
        self.lower_right_white_dates = []

        self.green = QtGui.QColor.fromRgbF(0.248478, 1.000000, 0.431632, 1.000000)
        self.red = QtGui.QColor.fromRgbF(1.000000, 0.343099, 0.419516, 1.000000)
        self.yellow = QtGui.QColor.fromRgbF(1.000000, 0.997757, 0.346044, 1.000000)

        

    def setCircledDates(self, list_of_dates):
        self.circled_dates = list_of_dates

    def setTriangleDates(self, list_of_dates):
        self.triangle_dates = list_of_dates

    #def setIgnoredDates(self, list_of_dates):
    #    self.ignored_dates = list_of_dates

    def setUpperLeftRedDates(self, list_of_dates):
        self.upper_left_red_dates = list_of_dates

    def setUpperLeftGreenDates(self, list_of_dates):
        self.upper_left_green_dates = list_of_dates

    def setUpperLeftYellowDates(self, list_of_dates):
        self.upper_left_yellow_dates = list_of_dates

    def setUpperLeftWhiteDates(self, list_of_dates):
        self.upper_left_white_dates = list_of_dates


    def setLowerRightRedDates(self, list_of_dates):
        self.lower_right_red_dates = list_of_dates

    def setLowerRightGreenDates(self, list_of_dates):
        self.lower_right_green_dates = list_of_dates

    def setLowerRightYellowDates(self, list_of_dates):
        self.lower_right_yellow_dates = list_of_dates

    def setLowerRightWhiteDates(self, list_of_dates):
        self.lower_right_white_dates = list_of_dates



    def paintUpperLeft(self, painter, rect, color, opacity):
        stored_opacity = painter.opacity()
        path = QtGui.QPainterPath()
        path.moveTo(rect.bottomLeft())
        path.lineTo(rect.topLeft())
        path.lineTo(rect.topRight())
        path.lineTo(rect.bottomLeft())
        #painter.setOpacity(opacity)
        painter.fillPath(path, color)
        painter.setOpacity(stored_opacity)
        self.upper_left_painted = True

    def paintLowerRight(self, painter, rect, color, opacity):
        stored_opacity = painter.opacity()
        path = QtGui.QPainterPath()
        path.moveTo(rect.bottomLeft())
        path.lineTo(rect.topRight())
        path.lineTo(rect.bottomRight())
        path.lineTo(rect.bottomLeft())
        #painter.setOpacity(opacity)
        painter.fillPath(path, color)
        painter.setOpacity(stored_opacity)
        self.lower_right_painted = True

    def paintCell(self, painter, rect, date):

        circle_thickness = rect.height() / 40.0 #30.0

        #radius = rect.height() / 2.6
        radius = rect.height() / 2.0 - 4.0 * circle_thickness

        rect_thickness = rect.height() / 15.0

        self.upper_left_painted = False
        self.lower_right_painted = False

        painter.fillRect(rect, QtGui.QColor('white'))
        
        if date in self.upper_left_red_dates:
            self.paintUpperLeft(painter, rect, self.red, 1.0)

        elif date in self.upper_left_green_dates:
            self.paintUpperLeft(painter, rect, self.green, 1.0)

        elif date in self.upper_left_yellow_dates:
            self.paintUpperLeft(painter, rect, self.yellow, 1.0)

        elif date in self.upper_left_white_dates:
            self.paintUpperLeft(painter, rect, QtGui.QColor('white'), 1.0)

        if date in self.lower_right_red_dates:
            self.paintLowerRight(painter, rect, self.red, 1.0)
        elif date in self.lower_right_green_dates:
            self.paintLowerRight(painter, rect, self.green, 1.0)
        elif date in self.lower_right_yellow_dates:
            self.paintLowerRight(painter, rect, self.yellow, 1.0)
        elif date in self.lower_right_white_dates:
            self.paintLowerRight(painter, rect, QtGui.QColor('white'), 1.0)
        
        if not self.upper_left_painted and not self.lower_right_painted:
            self.paintUpperLeft(painter, rect, QtGui.QColor('gray'), 1.0)
            self.paintLowerRight(painter, rect, QtGui.QColor('gray'), 1.0)

        painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))

        if date in self.circled_dates:
            saved_pen = painter.pen()
            modified_pen = painter.pen()
            modified_pen.setWidth(circle_thickness)
            painter.setPen(modified_pen)
            center = rect.center() - QtCore.QPoint(1.0, 0.0)
            #painter.drawEllipse(center - QtCore.QPoint(circle_thickness, circle_thickness), radius, radius)
            #painter.drawEllipse(center - QtCore.QPoint(circle_thickness, 0.0), radius, radius)
            painter.drawEllipse(center, radius, radius)
            painter.setPen(saved_pen)

        if date in self.triangle_dates:
            upper_right = rect.topRight()
            bounding_rect = QtCore.QRect(QtCore.QPoint(upper_right.x()-1-9,upper_right.y()+1), QtCore.QPoint(upper_right.x()-1,upper_right.y()+1+9))
            path = QtGui.QPainterPath()
            path.moveTo(bounding_rect.topRight())
            path.lineTo(bounding_rect.bottomRight())
            path.lineTo(bounding_rect.topLeft())
            path.lineTo(bounding_rect.topRight())
            painter.fillPath(path, QtGui.QBrush(QtGui.QColor('blue')))

        #if date in self.ignored_dates:
        #    upper_left = rect.topLeft()
        #    lower_right = rect.bottomRight()
        #    painter.drawline(center, upper_left, lower_right)
        #    print('IGNORED DATE!!!!!')

        if date == self.selectedDate():
            newUpperLeft = QtCore.QPoint(rect.topLeft().x() + rect_thickness/2.0, rect.topLeft().y() + rect_thickness/2.0)
            newBottomRight = QtCore.QPoint(rect.bottomRight().x() - rect_thickness, rect.bottomRight().y() - rect_thickness)
            new_rect = QtCore.QRect(newUpperLeft, newBottomRight)
            saved_pen = painter.pen()
            modified_pen = painter.pen()
            modified_pen.setWidth(rect_thickness) #3
            modified_pen.setColor(QtGui.QColor('blue'))
            painter.setPen(modified_pen)
            painter.drawRect(new_rect)
            painter.setPen(saved_pen)





