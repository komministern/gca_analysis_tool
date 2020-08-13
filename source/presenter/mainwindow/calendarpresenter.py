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


#import os 
#import string
#import time
from PySide2 import QtCore, QtGui, QtWidgets

from .localresources.coloringcontainer import ColoringContainer
from .localresources import textstuff as txt


#from presenter.filtercontainer import Filter
#from view.myfilterdialog import MyFilterDialog
#from presenter.eventfilter import EventBlocker




class CalendarPresenter(QtCore.QObject):

    def __init__(self, model, mainwindow, mainwindowpresenter):
        super(CalendarPresenter, self).__init__()
        self.model = model
        #self.view = view
        self.mainwindow = mainwindow
        self.mainwindowpresenter = mainwindowpresenter

        self.coloring_scheme = 0

        self.mainwindow.comboBox_Coloring.addItems([u'Normal/Degraded/Faulted', u'New/Active Faults', 
                                            u'Temporary Faults', u'Transmitter On', u'Shelter Door Open'])


    # Properties
    #selected_date
    #update_calendar


        # These are blocked in presenter.py



    # -------- Calendar stuff

    def new_date_chosen(self):
        self.mainwindowpresenter.update_text()
        self.mainwindowpresenter.update_comment()
        self.mainwindowpresenter.update_menu()


    def update_calendar(self):
        self.mainwindow.calendarWidget.setUpperLeftRedDates( self.mainwindowpresenter.presentation_dict[self.mainwindowpresenter.active_site_name].upper_left_red_dates )
        self.mainwindow.calendarWidget.setUpperLeftGreenDates( self.mainwindowpresenter.presentation_dict[self.mainwindowpresenter.active_site_name].upper_left_green_dates )
        self.mainwindow.calendarWidget.setUpperLeftWhiteDates( self.mainwindowpresenter.presentation_dict[self.mainwindowpresenter.active_site_name].upper_left_white_dates )
        self.mainwindow.calendarWidget.setUpperLeftYellowDates( self.mainwindowpresenter.presentation_dict[self.mainwindowpresenter.active_site_name].upper_left_yellow_dates )

        self.mainwindow.calendarWidget.setLowerRightRedDates( self.mainwindowpresenter.presentation_dict[self.mainwindowpresenter.active_site_name].lower_right_red_dates )
        self.mainwindow.calendarWidget.setLowerRightGreenDates( self.mainwindowpresenter.presentation_dict[self.mainwindowpresenter.active_site_name].lower_right_green_dates )
        self.mainwindow.calendarWidget.setLowerRightWhiteDates( self.mainwindowpresenter.presentation_dict[self.mainwindowpresenter.active_site_name].lower_right_white_dates )
        self.mainwindow.calendarWidget.setLowerRightYellowDates( self.mainwindowpresenter.presentation_dict[self.mainwindowpresenter.active_site_name].lower_right_yellow_dates )

        self.mainwindow.calendarWidget.setIgnoredDates( self.model.get_ignored_dates(self.mainwindowpresenter.active_site_name) )

        self.mainwindow.calendarWidget.updateCells()

    def update_calendar_cells(self):
        self.mainwindow.calendarWidget.updateCells()

    def set_comment_dates(self, dates):
        self.mainwindow.calendarWidget.setTriangleDates(dates)
    
    def set_search_hit_dates(self, dates):
        self.mainwindow.calendarWidget.setCircledDates(dates)

    def set_coloring_scheme(self, index):
        self.coloring_scheme = index
        self.mainwindowpresenter.presentation_dict[self.mainwindowpresenter.active_site_name] = self.colored_dates(self.mainwindowpresenter.active_site_name)
        self.update_calendar()

    def set_last_date(self):
        if self.mainwindowpresenter.active_site_name:
            self.selected_date = self.model.get_last_entry_date(self.mainwindowpresenter.active_site_name)

    def set_first_date(self):
        if self.mainwindowpresenter.active_site_name:
            self.selected_date = self.model.get_first_entry_date(self.mainwindowpresenter.active_site_name)

    def set_active_date(self):
        if self.mainwindowpresenter.active_site_name:
            self.selected_date = self.selected_date


    @property
    def selected_date(self):
        return self.mainwindow.calendarWidget.selectedDate()

    @selected_date.setter
    def selected_date(self, date):
        self.mainwindow.calendarWidget.setSelectedDate(date)
        self.update_calendar()

    

    def colored_dates(self, site_name):

        if site_name == u'':    # All gray!!!!
            
            lower_right_red_dates = []
            lower_right_green_dates = []
 
            upper_left_red_dates = []
            upper_left_green_dates = []

            upper_left_white_dates = []
            upper_left_yellow_dates = []

            lower_right_white_dates = []
            lower_right_yellow_dates = []


        elif self.coloring_scheme == 0:       # Normal/Degraded/Faulted

            red_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if txt.faulted(text)]
            yellow_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if txt.degraded(text) and date not in red_dates]
            green_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if txt.normal(text) and (date not in red_dates) and (date not in yellow_dates)]
            white_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if (date not in red_dates) and (date not in yellow_dates) and (date not in green_dates)]

            lower_right_red_dates = red_dates
            lower_right_green_dates = green_dates
 
            upper_left_red_dates = red_dates
            upper_left_green_dates = green_dates

            upper_left_white_dates = white_dates
            upper_left_yellow_dates = yellow_dates

            lower_right_white_dates = white_dates
            lower_right_yellow_dates = yellow_dates

        elif self.coloring_scheme == 1:     # New Fault/Active Fault
        
            lower_right_red_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if txt.active_fault_in(text)]
            lower_right_green_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if txt.no_active_fault_in(text)]
 
            upper_left_red_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if txt.new_fault_in(text)]
            upper_left_green_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if txt.no_new_fault_in(text)]

            upper_left_white_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if date not in upper_left_red_dates and date not in upper_left_green_dates]
            upper_left_yellow_dates = []
            
            lower_right_white_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if date not in lower_right_red_dates and date not in lower_right_green_dates]
            lower_right_yellow_dates = []

        elif self.coloring_scheme == 2:     # Temporary Faults

            red_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if txt.new_fault_in(text) and 
                            (not txt.degraded(text)) and (not txt.faulted(text))]
            white_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if date not in red_dates]

            lower_right_red_dates = red_dates
            upper_left_red_dates = red_dates
           
            lower_right_green_dates = []
 
            upper_left_green_dates = []

            upper_left_white_dates = white_dates
            upper_left_yellow_dates = []
            
            lower_right_white_dates = white_dates
            lower_right_yellow_dates = []

        elif self.coloring_scheme == 3:     # Transmitter on

            green_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if txt.transmitter_on(text)]
            white_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if date not in green_dates]

            lower_right_red_dates = []
            upper_left_red_dates = []
           
            lower_right_green_dates = green_dates
 
            upper_left_green_dates = green_dates

            upper_left_white_dates = white_dates
            upper_left_yellow_dates = []
            
            lower_right_white_dates = white_dates
            lower_right_yellow_dates = []


        elif self.coloring_scheme == 4:     # Shelter Door Open

            green_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if (u'Shelter Door Open' in text)]
            white_dates = [date for date, text in self.model.get_historylog_dictionary(site_name).items() if date not in green_dates]

            lower_right_red_dates = []
            upper_left_red_dates = []
           
            lower_right_green_dates = green_dates
 
            upper_left_green_dates = green_dates

            upper_left_white_dates = white_dates
            upper_left_yellow_dates = []
            
            lower_right_white_dates = white_dates
            lower_right_yellow_dates = []

        return ColoringContainer(upper_left_red_dates, upper_left_green_dates, 
                                upper_left_yellow_dates, upper_left_white_dates,
                                lower_right_red_dates, lower_right_green_dates, 
                                lower_right_yellow_dates, lower_right_white_dates)