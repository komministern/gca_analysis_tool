#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


#import os 
#import string
#import time
from PySide2 import QtCore, QtGui, QtWidgets
from presenter.coloringcontainer import ColoringContainer
import presenter.textstuff as txt
#from presenter.filtercontainer import Filter
#from view.myfilterdialog import MyFilterDialog
#from presenter.eventfilter import EventBlocker




class CalendarPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        super(CalendarPresenter, self).__init__()
        self.model = model
        self.view = view
        self.presenter = presenter

        self.coloring_scheme = 0

        self.view.comboBox_Coloring.addItems([u'Normal/Degraded/Faulted', u'New/Active Faults', 
                                            u'Temporary Faults', u'Transmitter On', u'Shelter Door Open'])

        # These are blocked in presenter.py


    # -------- Calendar stuff


    def new_date_chosen(self):
        self.presenter.update_text()
        self.presenter.update_comment()


    def update_calendar(self):

        #if self.active_site:

        self.view.calendarWidget.setUpperLeftRedDates( self.presenter.presentation_dict[self.presenter.active_site_name].upper_left_red_dates )
        self.view.calendarWidget.setUpperLeftGreenDates( self.presenter.presentation_dict[self.presenter.active_site_name].upper_left_green_dates )
        self.view.calendarWidget.setUpperLeftWhiteDates( self.presenter.presentation_dict[self.presenter.active_site_name].upper_left_white_dates )
        self.view.calendarWidget.setUpperLeftYellowDates( self.presenter.presentation_dict[self.presenter.active_site_name].upper_left_yellow_dates )

        self.view.calendarWidget.setLowerRightRedDates( self.presenter.presentation_dict[self.presenter.active_site_name].lower_right_red_dates )
        self.view.calendarWidget.setLowerRightGreenDates( self.presenter.presentation_dict[self.presenter.active_site_name].lower_right_green_dates )
        self.view.calendarWidget.setLowerRightWhiteDates( self.presenter.presentation_dict[self.presenter.active_site_name].lower_right_white_dates )
        self.view.calendarWidget.setLowerRightYellowDates( self.presenter.presentation_dict[self.presenter.active_site_name].lower_right_yellow_dates )

        self.view.calendarWidget.updateCells()




        

    def set_coloring_scheme(self, index):
        self.coloring_scheme = index
        #self.activate_progressbar(2)
        self.presenter.presentation_dict[self.presenter.active_site_name] = self.colored_dates(self.presenter.active_site_name)
        
        #self.view.progressBar.setValue(1)
        self.update_calendar()
        #self.view.progressBar.setValue(2)
        #self.deactivate_progressbar()

    def set_last_date(self):
        if self.presenter.active_site_name:
            self.set_selected_date(self.model.get_last_entry_date(self.presenter.active_site_name))
            self.update_calendar()

    def set_first_date(self):
        if self.presenter.active_site_name:
            self.set_selected_date(self.model.get_first_entry_date(self.presenter.active_site_name))
            self.update_calendar()

    def set_active_date(self):
        if self.presenter.active_site_name:
            self.view.calendarWidget.setSelectedDate(self.view.calendarWidget.selectedDate())
            self.update_calendar()

    def set_selected_date(self, date):
        self.view.calendarWidget.setSelectedDate(date)


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