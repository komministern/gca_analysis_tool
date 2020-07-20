"""
    This file is part of GCA Analysis Tool.

    Copyright (C) 2016-2020  Oscar Franzén  oscarfranzen@protonmail.com

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

#import datetime
#from datetime import timedelta
#import matplotlib.pyplot as plt
#import matplotlib

#from PySide2 import QtCore, QtGui, QtWidgets
#matplotlib.use('Qt5Agg')

from PySide2 import QtCore, QtGui, QtWidgets
#from matplotlib.backends.backend_qt5agg import (
#        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
#from matplotlib.figure import Figure
#from matplotlib.widgets import RadioButtons

#from presenter.resultswindow.scrollbarpresenter import ScrollBarPresenter
#from view.graphwindow import GraphWindow
#from presenter.graphwindowstuff.scrollbarpresenter import ScrollBarPresenter


class ScrollBarPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        
        super(ScrollBarPresenter, self).__init__()

        self.model = model
        self.graphwindowpresenter = presenter
        self.graphwindow = view

        self.slider_down = False
        self.ignore_new_value_due_to_x_axis_scope_change = False
    


    def new_slider_value(self, value):
        #print('------------------')
        #print('method - new_slider_value - entering')
        #print('ignore_new_value_due_to_x_axis_scope_change: ' + str(self.ignore_new_value_due_to_x_axis_scope_change))
        #print('present_date: ' + self.graphwindowpresenter.present_date.toString(f=QtCore.Qt.RFC2822Date))
        #print('new scrollbar value: ' + str(value))
        #print('---')
        

        if not self.slider_down and not self.ignore_new_value_due_to_x_axis_scope_change:
            if self.graphwindowpresenter.x_axis_scope == 'Day':
                first_year_date = QtCore.QDate(self.graphwindowpresenter.present_date.year(), 1, 1)
                self.graphwindowpresenter.present_date = first_year_date.addDays(self.graphwindow.horizontalScrollBar.value() - 1)

            elif self.graphwindowpresenter.x_axis_scope == 'Week':
                previous_week, _ = self.graphwindowpresenter.present_date.weekNumber()
                new_week = value
                if new_week != previous_week:
                    new_present_date = self.graphwindowpresenter.present_date.addDays(7*(new_week - previous_week))
                    self.graphwindowpresenter.present_date = new_present_date

            elif self.graphwindowpresenter.x_axis_scope == 'Month':
                previous_month = self.graphwindowpresenter.present_date.month()
                new_month = value
                if new_month != previous_month:
                    new_present_date = self.graphwindowpresenter.present_date.addMonths(new_month - previous_month)
                    self.graphwindowpresenter.present_date = new_present_date

            elif self.graphwindowpresenter.x_axis_scope == 'Year':
                previous_year = self.graphwindowpresenter.present_date.year()
                new_year = value
                if new_year != previous_year:
                    new_present_date = self.graphwindowpresenter.present_date.addYears(new_year - previous_year)
                    self.graphwindowpresenter.present_date = new_present_date
            
            self.graphwindowpresenter.mplpresenter.update_graphs()

        #print('method - new_slider_value - exiting')
        #print('present_date: ' + self.graphwindowpresenter.present_date.toString(f=QtCore.Qt.RFC2822Date))
        #print('------------------')

        #self.ignore_new_value_due_to_x_axis_scope_change = False
        #self.graphwindowpresenter.draw_graphs()


    def slider_pressed(self):
        self.slider_down = True
        if self.graphwindowpresenter.x_axis_scope == 'Day':
            first_year_date = QtCore.QDate(self.graphwindowpresenter.present_date.year(), 1, 1)
            new_date = first_year_date.addDays(self.graphwindow.horizontalScrollBar.value() - 1)
            text = new_date.toString(f=QtCore.Qt.RFC2822Date)
        elif self.graphwindowpresenter.x_axis_scope == 'Week':
            text = str('Week ' + str(self.graphwindow.horizontalScrollBar.value()))
        elif self.graphwindowpresenter.x_axis_scope == 'Month':
            first_year_date = QtCore.QDate(self.graphwindowpresenter.present_date.year(), 1, 1)
            new_date = first_year_date.addMonths(self.graphwindow.horizontalScrollBar.value() - 1)
            text = new_date.toString('MMMM')
        elif self.graphwindowpresenter.x_axis_scope == 'Year':
            text = str( self.graphwindow.horizontalScrollBar.value() )
        #self.mytooltip = QtWidgets.QToolTip.showText(QtGui.QCursor.pos(), text, self.graphwindow)
        QtWidgets.QToolTip.showText(QtGui.QCursor.pos(), text, self.graphwindow)

    
    def slider_released(self):
        self.slider_down = False
        self.new_slider_value(self.graphwindow.horizontalScrollBar.value())
        #del self.mytooltip
        

    def slider_moved(self, value):
        #del self.mytooltip
        if self.graphwindowpresenter.x_axis_scope == 'Day':
            first_year_date = QtCore.QDate(self.graphwindowpresenter.present_date.year(), 1, 1)
            new_date = first_year_date.addDays(value - 1)
            text = new_date.toString(f=QtCore.Qt.RFC2822Date)
        elif self.graphwindowpresenter.x_axis_scope == 'Week':
            text = 'Week ' + str(value)
        elif self.graphwindowpresenter.x_axis_scope == 'Month':
            first_year_date = QtCore.QDate(self.graphwindowpresenter.present_date.year(), 1, 1)
            new_date = first_year_date.addMonths(value - 1)
            text = new_date.toString('MMMM')
        elif self.graphwindowpresenter.x_axis_scope == 'Year':
            text = str(value)
        else:
            pass
            #text = str(value)
        #self.mytooltip = QtWidgets.QToolTip.showText(QtGui.QCursor.pos(), text, self.graphwindow)
        #QtWidgets.QToolTip.showText(self.graphwindow.horizontalScrollBar., text, self.graphwindow)
        QtWidgets.QToolTip.showText(QtGui.QCursor.pos(), text, self.graphwindow)
        


    def update_scrollbar(self):
        if self.graphwindowpresenter.x_axis_scope == 'Day':
            self.graphwindow.horizontalScrollBar.setMinimum(1)
            self.graphwindow.horizontalScrollBar.setMaximum( self.graphwindowpresenter.present_date.daysInYear() )
            self.graphwindow.horizontalScrollBar.setValue( self.graphwindowpresenter.present_date.dayOfYear() )

        elif self.graphwindowpresenter.x_axis_scope == 'Week':
            self.graphwindow.horizontalScrollBar.setMinimum(1)
            self.graphwindow.horizontalScrollBar.setValue(1)
            last_date_of_year = QtCore.QDate(self.graphwindowpresenter.present_date.year(), 12, 31)
            print('last_date_of_year: ' + str(last_date_of_year))
            last_week_of_year, _ = last_date_of_year.weekNumber()
            if last_week_of_year == 1:
                last_week_of_year, _ = last_date_of_year.addDays(-7).weekNumber()
            print('last_week_of_year: ' + str(last_week_of_year))
            self.graphwindow.horizontalScrollBar.setMaximum( last_week_of_year )
            present_week, _ = self.graphwindowpresenter.present_date.weekNumber()
            print('present week: ' + str(present_week))
            self.graphwindow.horizontalScrollBar.setValue( present_week )

        elif self.graphwindowpresenter.x_axis_scope == 'Month':
            self.graphwindow.horizontalScrollBar.setMinimum(1)
            self.graphwindow.horizontalScrollBar.setValue(1)
            self.graphwindow.horizontalScrollBar.setMaximum(12)
            self.graphwindow.horizontalScrollBar.setValue( self.graphwindowpresenter.present_date.month() )

        elif self.graphwindowpresenter.x_axis_scope == 'Year':
            self.graphwindow.horizontalScrollBar.setMinimum( self.graphwindowpresenter.data['dates'][0].year() )
            self.graphwindow.horizontalScrollBar.setValue( self.graphwindowpresenter.data['dates'][0].year() )
            self.graphwindow.horizontalScrollBar.setMaximum( self.graphwindowpresenter.data['dates'][-1].year() )
            self.graphwindow.horizontalScrollBar.setValue( self.graphwindowpresenter.present_date.year() )

        self.graphwindow.horizontalScrollBar.setSingleStep(1)
        self.graphwindow.horizontalScrollBar.setPageStep(1)