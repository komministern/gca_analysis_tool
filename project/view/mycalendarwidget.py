#!/usr/bin/env python
# -*- coding: utf-8 -*-


#    Copyright © 2016, 2017 Oscar Franzén <oscarfranzen@yahoo.se>
#
#    This file is part of GCA Analysis Tool.


from PySide import QtCore, QtGui


class MyCalendarWidget(QtGui.QCalendarWidget):
    def __init__(self, parent=None):
        QtGui.QCalendarWidget.__init__(self, parent)
        
        self.setFirstDayOfWeek(QtCore.Qt.DayOfWeek.Monday)

        self.setCircledDates([])
        self.setTriangleDates([])

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
            center = rect.center()
            painter.drawEllipse(center, 12, 12)

        if date in self.triangle_dates:
            upper_right = rect.topRight()
            bounding_rect = QtCore.QRect(QtCore.QPoint(upper_right.x()-1-9,upper_right.y()+1), QtCore.QPoint(upper_right.x()-1,upper_right.y()+1+9))
            path = QtGui.QPainterPath()
            path.moveTo(bounding_rect.topRight())
            path.lineTo(bounding_rect.bottomRight())
            path.lineTo(bounding_rect.topLeft())
            path.lineTo(bounding_rect.topRight())
            painter.fillPath(path, QtGui.QBrush(QtGui.QColor('blue')))

        if date == self.selectedDate():
            newUpperLeft = QtCore.QPoint(rect.topLeft().x() + 1, rect.topLeft().y() + 1)
            newBottomRight = QtCore.QPoint(rect.bottomRight().x() - 2, rect.bottomRight().y() - 2)
            new_rect = QtCore.QRect(newUpperLeft, newBottomRight)
            saved_pen = painter.pen()
            modified_pen = painter.pen()
            modified_pen.setWidth(2) #3
            modified_pen.setColor(QtGui.QColor('blue'))
            painter.setPen(modified_pen)
            painter.drawRect(new_rect)
            painter.setPen(saved_pen)





