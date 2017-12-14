#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


import os
import string
from PySide import QtCore, QtGui
from coloringcontainer import ColoringContainer
import textstuff as txt
from filtercontainer import Filter
from view.myfilterdialog import MyFilterDialog

import time


class MyPresenter(QtCore.QObject):

    def __init__(self, model, view, **kwds):
        super(MyPresenter, self).__init__(**kwds)

        self.test = False

        # Store view and model.
        self._model = model
        self._view = view


        # Setup all signals.
        #self.connect_signals()


        self.highlight = ''
        self.presentation_dict = {}
        self.active_site = None
        
        self.active_site_name = None
        
        self.coloring_scheme = 0

        self.comment_text_changed = False


        # Colors
        self.green = QtGui.QColor.fromRgbF(0.248478, 1.000000, 0.431632, 1.000000)
        self.red = QtGui.QColor.fromRgbF(1.000000, 0.343099, 0.419516, 1.000000)
        self.yellow = QtGui.QColor.fromRgbF(1.000000, 0.997757, 0.346044, 1.000000)
        self.blue = QtGui.QColor.fromRgbF(0.509743, 0.734401, 1.000000, 1.000000)

        self.start_app()

        self.connect_signals()


    def start_app(self):

        #if test == False:
        #    site_names = self.model.get_site_names()
        #elif test == True:
        #    site_names = []
            
        #i = 0
        #n = len(site_names)
        
        #self.progress = QtGui.QProgressDialog(u"Reading history logs...", u"Abort", 0, n, self.view)
        #self.progress.setWindowModality(QtCore.Qt.WindowModal)

        
        #if n > 0: 
            #self.progress = QtGui.QProgressDialog(u"Reading history logs...", u"Abort", 0, n, self.view)
            #self.progress.setWindowModality(QtCore.Qt.WindowModal)

        #for site_name in site_names:
        #    self.model.read_site_to_memory(site_name)
        #    i += 1
        #    self.progress.setValue(i)

        #    if self.progress.wasCanceled():
        #        break
        
        #print 'progress dialog done'
    
        #if not self.progress.wasCanceled():
            
        #    if test == False:
        #        self.model.read_filters_to_memory()

        self.view.comboBox_Coloring.addItems([u'Normal/Degraded/Faulted', u'New Fault/Active Fault', 
                                            u'Temporary Faults (< 1 min per day)', u'Transmitter On', u'Shelter Door Open'])

        
        self.current_filter = self.model.filter_list[0]
        self.view.comboBox_ChooseFilter.addItems([each.name for each in self.model.filter_list])
        
        self.view.pushButton_EditFilter.setEnabled(False)
        self.view.pushButton_DeleteFilter.setEnabled(False)
        
        #    if test == False:
        #        self.color_all_dates()

        self.trial_has_ended = False    # To be removed I guess
            
        #    if len(site_names) > 0:

                # Check if trial is up
                #self.trial_has_ended = False
        
        # Should this test be removed?
        #for site_name in self.model.get_site_names():
                
        #    if (self.model.get_third_last_entry_date(site_name).year() >= 2018) and (self.model.get_third_last_entry_date(site_name).month() >= 7):
        #        self.trial_has_ended = True

        site_items = [u''] + self.model.get_site_names()
        self.view.comboBox_ActiveSite.addItems(site_items)
        
        self.active_site = site_items[0]
        
        self.active_site = u''
        self.active_site_name = u''

        self.update_menu()

        #    if test == False:
        #        self.update_calendar()
        #        self.update_text()
        #        self.update_comment()

        #        self.update_menu()



    # --------- Coloring the dates


#    def color_all_dates(self):
        
        
        
#        for site_name in self.model.get_site_names():
#            self.presentation_dict[site_name] = self.colored_dates(site_name)


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




    # --------- Properties


    @property
    def model(self):
        return self._model

    @property
    def view(self):
        return self._view


    # -------- Calendar stuff


    def update_calendar(self):

        #if self.active_site:

        self.view.calendarWidget.setUpperLeftRedDates( self.presentation_dict[self.active_site].upper_left_red_dates )
        self.view.calendarWidget.setUpperLeftGreenDates( self.presentation_dict[self.active_site].upper_left_green_dates )
        self.view.calendarWidget.setUpperLeftWhiteDates( self.presentation_dict[self.active_site].upper_left_white_dates )
        self.view.calendarWidget.setUpperLeftYellowDates( self.presentation_dict[self.active_site].upper_left_yellow_dates )

        self.view.calendarWidget.setLowerRightRedDates( self.presentation_dict[self.active_site].lower_right_red_dates )
        self.view.calendarWidget.setLowerRightGreenDates( self.presentation_dict[self.active_site].lower_right_green_dates )
        self.view.calendarWidget.setLowerRightWhiteDates( self.presentation_dict[self.active_site].lower_right_white_dates )
        self.view.calendarWidget.setLowerRightYellowDates( self.presentation_dict[self.active_site].lower_right_yellow_dates )

        self.view.calendarWidget.updateCells()



    def activate_progressbar(self, max_ticks):
        self.view.progressBar.setMaximum(max_ticks)
        self.progressbar_activated = True
    
    def deactivate_progressbar(self):
        time.sleep(0.1)                         # Just for the feeling
        self.progressbar_activated = False
        self.view.progressBar.setValue(0)
        
#    def progress_tick(self):
#        if self.progressbar_activated:
#            old_value = self.view.progressBar.value()
#            if old_value < self.progressBar.maximum():
#                self.view.progressBar.setValue(old_value + 1)

    def set_active_site(self, index):
        
        site_items = [u''] + self.model.get_site_names()
        self.active_site = site_items[index]
        
        if not self.active_site == u'':
            #print 'tjo'
            #progress = QtGui.QProgressDialog(u"Reading history logs...", u"Abort", 0, 1, self.view)
            #progress.setWindowModality(QtCore.Qt.WindowModal)
            #progress.setCancelButton(None)
        
        #if n > 0: 
            
            #print 'progress window'
        
            #self.progress = QtGui.QProgressDialog(parent=self.view)
            #self.progress.setWindowModality(QtCore.Qt.WindowModal)
            #self.progress.setMinimum(0)
            #self.progress.setMaximum(1)
            #self.progress.setMinimumDuration(1000)
            #self.progress.setLabelText(u'Testing...')
            #self.progress.setValue(0)

        #for site_name in site_names:
        #    self.model.read_site_to_memory(site_name)
        #    i += 1
        #    self.progress.setValue(i)

        #    if self.progress.wasCanceled():
        #        break
            
            #self.view.progressBar.setValue(50)
            
            
            self.activate_progressbar(2)
            self.view.progressBar.setValue(1)
            self.model.read_site_to_memory(self.active_site)
            self.view.progressBar.setValue(2)
            self.deactivate_progressbar()

        self.activate_progressbar(5)
        self.presentation_dict[self.active_site] = self.colored_dates(self.active_site)
        self.view.progressBar.setValue(1)
        self.commit_string_search()     # self.update_text() is called in this procedure
        self.view.progressBar.setValue(2)
        self.update_calendar()
        self.view.progressBar.setValue(3)
        self.update_comment()
        self.view.progressBar.setValue(4)
        self.update_menu()
        self.view.progressBar.setValue(5)
        self.deactivate_progressbar()

    def set_coloring_scheme(self, index):
        self.coloring_scheme = index
        self.activate_progressbar(2)
        self.presentation_dict[self.active_site] = self.colored_dates(self.active_site)
        #self.color_all_dates()
        self.view.progressBar.setValue(1)
        self.update_calendar()
        self.view.progressBar.setValue(2)
        self.deactivate_progressbar()

    def set_last_date(self):
        if self.active_site:
            self.set_selected_date(self.model.get_last_entry_date(self.active_site))
            self.update_calendar()

    def set_first_date(self):
        if self.active_site:
            self.set_selected_date(self.model.get_first_entry_date(self.active_site))
            self.update_calendar()

    def set_active_date(self):
        self.view.calendarWidget.setSelectedDate(self.view.calendarWidget.selectedDate())
        self.update_calendar()

    def set_selected_date(self, date):
        self.view.calendarWidget.setSelectedDate(date)



    # ---------- Text stuff


    def update_text(self):

        
        if True:
        #if not self.active_site == u'':
            
            date = self.view.calendarWidget.selectedDate()
            if self.active_site == u'':
                text = u''
            else:
                text = self.model.get_historylog(self.active_site, date)
                
            self.view.textBrowser_HistoryLog.setPlainText(self.format_text(text))

            if self.highlight != u'' and text != u'No history log exists for this date.': 

                #palette = QtGui.QPalette()
                #palette.setColor(QtGui.QPalette.Base,QtCore.Qt.blue)
                #self.view.lineEdit_StringSearch.setPalette(palette)

                text = self.view.tabWidget.tabText(0)
                if text[-1] != u'*':
                    self.view.tabWidget.setTabText(0, text + u'*')

                cursor = self.view.textBrowser_HistoryLog.textCursor()
            
                # Setup the desired format for matches
                format = QtGui.QTextCharFormat()
                format.setBackground(QtGui.QBrush(self.blue))


                pattern = self.highlight

                pos = 0
                index = self.view.textBrowser_HistoryLog.toPlainText().find(pattern)

                while (index != -1):

                    # Select the matched text and apply the desired format
                    cursor.setPosition(index)
                    cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, len(pattern))
                    cursor.mergeCharFormat(format)

                    # Move to the next match
                    pos = index + len(pattern)
                    index = self.view.textBrowser_HistoryLog.toPlainText().find(pattern, pos)

                # This is a dirty fix for a bizarre problem. If this is omitted, only part of the text will be displayed after a
                # search!!! Weird.
                self.view.textBrowser_HistoryLog.setLineWrapMode(QtGui.QTextEdit.NoWrap)
                self.view.textBrowser_HistoryLog.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)

            else:
                
                text = self.view.tabWidget.tabText(0)
                if text[-1] == u'*':
                    self.view.tabWidget.setTabText(0, text[0:-1])

            self.update_comment()   # Here?????????????????????????




    # ----------- Filter stuff


    def format_text(self, text):
        if text != u'No history log exists for this date.':
            if self.current_filter.state == 1 and self.current_filter.content:  # Show Only
                return '\n'.join([s for s in text.splitlines() if s[0:4] in self.current_filter.content])
            elif self.current_filter.state == 0:        # Suppress
                return '\n'.join([s for s in text.splitlines() if not s[0:4] in self.current_filter.content])
        return text



    def show_filter_dialog(self, initial_filter, name_editable = True):
        self.dialog = MyFilterDialog(initial_filter, name_editable, self.view)
        if self.dialog.exec_():
            filter = self.dialog.get_final_filter()
            self.save_filter(filter)
            
    def save_filter(self, filter):
        if filter.name in set([each.name for each in self.model.filter_list]):
            for index in range(len(self.model.filter_list)):
                if self.model.filter_list[index].name == filter.name:
                    break
            del self.model.filter_list[index]
            
        self.model.filter_list.append(filter)
        
        self.model.filter_list.sort(key = lambda x: x.name)
        self.model.update_filters()
        
        self.view.comboBox_ChooseFilter.clear()
        self.view.comboBox_ChooseFilter.addItems([each.name for each in self.model.filter_list])

        for index in range(len(self.model.filter_list)):
            if self.model.filter_list[index].name == filter.name:
                break
 
        self.view.comboBox_ChooseFilter.setCurrentIndex(index)


    def new_filter(self):
        self.show_filter_dialog(Filter())

    def edit_filter(self):
        self.show_filter_dialog(self.current_filter, name_editable = False)
        

    def delete_filter(self):
        clicked = self.message_with_cancel_choice(u'Delete ' + self.current_filter.name + '?', u'This will completely remove the filter.', QtGui.QMessageBox.Cancel)
        if clicked == QtGui.QMessageBox.Ok:
            self.model.filter_list.remove(self.current_filter)
            self.model.update_filters()
            self.view.comboBox_ChooseFilter.clear()
            self.view.comboBox_ChooseFilter.addItems([each.name for each in self.model.filter_list])
        
            self.choose_filter(0)
        
        

    def choose_filter(self, index):
        
        if index == 0:
            text = self.view.tabWidget.tabText(1)
            if text[-1] == u'*':
                self.view.tabWidget.setTabText(1, text[0:-1])
                
            self.view.pushButton_EditFilter.setEnabled(False)
            self.view.pushButton_DeleteFilter.setEnabled(False)
        else:
            
            text = self.view.tabWidget.tabText(1)
            if text[-1] != u'*':
                self.view.tabWidget.setTabText(1, text + u'*')
                
            self.view.pushButton_EditFilter.setEnabled(True)
            self.view.pushButton_DeleteFilter.setEnabled(True)
            
        self.current_filter = self.model.filter_list[index]
        self.update_text()



    # ------------ String search stuff


    def commit_string_search(self):
        #if True:
        #if self.active_site:
        
            #self.test = 1
        
        self.highlight = self.view.plainTextEdit_StringSearch.toPlainText()

        self.view.calendarWidget.setCircledDates(self.list_of_search_string_dates(self.view.plainTextEdit_StringSearch.toPlainText()))
        
        self.view.calendarWidget.updateCells()
        self.update_text()
            
            #self.test = 2
            
            # Lets set highlight in the plainTextEdit text here!!!
            
            #print self.view.lineEdit_StringSearch.textCursor()
        cursor = self.view.plainTextEdit_StringSearch.textCursor()
            #self.view.lineEdit_StringSearch.end(False)

            #self.test = 3

        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(self.blue))

            # Select the matched text and apply the desired format
        cursor.setPosition(0)
            
            #self.test = 4
        
        cursor.movePosition(QtGui.QTextCursor.End, QtGui.QTextCursor.KeepAnchor, 1)
            
            #self.test = 5
            
        self.ignore = True
            
        cursor.mergeCharFormat(format)
            
            #self.test = 6




    def list_of_search_string_dates(self, astring):
        if not astring == '' and not self.active_site == u'':
            return [date for date, text in self.model.get_historylog_dictionary(self.active_site).items() if astring in text]
        else:
            return []


    def reset_string_search(self):
        
        cursor = self.view.plainTextEdit_StringSearch.textCursor()

        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtCore.Qt.white))
        # Select the matched text and apply the desired format
        cursor.setPosition(0)
        cursor.movePosition(QtGui.QTextCursor.End, QtGui.QTextCursor.KeepAnchor, 1)
        self.ignore = True
        cursor.mergeCharFormat(format)
        
        
        
        self.view.calendarWidget.setCircledDates([])
        self.view.plainTextEdit_StringSearch.setPlainText(u'')
        self.highlight = u''
        self.view.calendarWidget.updateCells()
        self.update_text()




    def set_next_search_date(self):
        if not self.active_site == u'':
            dates = sorted(self.list_of_search_string_dates(self.view.plainTextEdit_StringSearch.toPlainText()))
            if not len(dates) == 0:
                greater_dates = [date for date in dates if date > self.view.calendarWidget.selectedDate()]

                if len(greater_dates) == 0:
                    new_index = 0
                else:
                    new_index = dates.index(greater_dates[0])
                self.view.calendarWidget.setSelectedDate(dates[new_index])
                self.view.calendarWidget.updateCells()


    def set_previous_search_date(self):
        if not self.active_site == u'':
            dates = sorted(self.list_of_search_string_dates(self.view.plainTextEdit_StringSearch.toPlainText()))
            if not len(dates) == 0:
                lesser_dates = [date for date in dates if date < self.view.calendarWidget.selectedDate()]
                if len(lesser_dates) == 0:
                    new_index = -1
                else:
                    new_index = dates.index(lesser_dates[-1])            
                self.view.calendarWidget.setSelectedDate(dates[new_index])
                self.view.calendarWidget.updateCells()


    def text_changed(self):
        
        #print self.test
        
        if not self.highlight == u'' and not self.ignore:
            
            self.highlight = u''
            self.update_text()

            self.view.calendarWidget.setCircledDates([])
            self.view.calendarWidget.updateCells()
            
            cursor = self.view.plainTextEdit_StringSearch.textCursor()
            #self.view.lineEdit_StringSearch.end(False)

            format = QtGui.QTextCharFormat()
            format.setBackground(QtGui.QBrush(QtCore.Qt.white))
            #print self.test

        
            # Select the matched text and apply the desired format
            cursor.setPosition(0)
            cursor.movePosition(QtGui.QTextCursor.EndOfLine, QtGui.QTextCursor.KeepAnchor, 1)
            cursor.mergeCharFormat(format)
            
#            self.test = False
        self.ignore = False

    def return_pressed(self):
        self.view.pushButton_CommitStringSearch.animateClick()
        self.view.pushButton_CommitStringSearch.clicked.emit()


    # ---------- Import a capturesite file

    def import_capturesite(self):

        capturesite_filename, _ = QtGui.QFileDialog.getOpenFileName(self.view, u'Choose capturesite file to import', self.model.home_directory, u'Capturesite (*tar.gz *TAR.Z)')

        if capturesite_filename[-2:] == '.Z':
            
            if not self.model.exist_7z():
                
                self.message(u'To decompress this Capturesite file, the application 7z needs to be installed. Either this is not the case, or it is installed in a non default location. Please enter the location of the file 7z.exe.')

                path_to_7z, _ = QtGui.QFileDialog.getOpenFileName(self.view, u'Path to 7z.exe', self.model.home_directory, u'7z console application (7z.exe)')
                self.model.set_path_to_7z(path_to_7z)

        
        if capturesite_filename and self.model.exist_7z():

            temp_site_name = u'_TEMP'

            try:
            
                self.activate_progressbar(2)
                
                self.view.progressBar.setValue(1)
            
                # Create a temporary site _TEMP
                # The self.mode.create_site decompresses and copies all historylog files to temp_site_name
                # and (!) reads all these in to memory
                self.model.create_new_site(capturesite_filename, temp_site_name)

                # List all the dates of the historylog files (sorted not needed?!?)
                #temp_dates = sorted(self.model.get_historylog_dictionary(temp_site_name).keys())
                temp_dates = self.model.get_historylog_dictionary(temp_site_name).keys()
                
                # Delete the site on disc. It is still in memory though!!!!
                self.model.remove_site_from_disc(temp_site_name)

                # Now let's check if the capturesite file is an update of an existing site
                possible_candidates = []

                self.view.progressBar.setValue(2)
                self.deactivate_progressbar()

                self.activate_progressbar(len(self.model.get_site_names()))
                i = 0

                for site_name in self.model.get_site_names():
                    
                    # For this code to work, all sites must be read to memory first.
                    self.model.read_site_to_memory(site_name)
                    
                    # Create a sorted (why sorted?) list of all site dates, including the ignored dates
                    site_dates = self.model.get_historylog_dictionary(site_name).keys()
                    site_dates.extend(self.model.get_ignored_dates(site_name))
                    #site_dates = sorted(site_dates)     # UGLY

                    T = set(temp_dates)
                    S = set(site_dates)

                    # If the difference between the set of site dates and the intersection of the set of temporary dates and the set of site dates is empty,
                    # this temporary site most probably is an update of the site.
                    if len( S - (T & S) ) == 0 or len( T - (T & S) ) == 0:
                        possible_candidates.append(site_name)
                    
                    i += 1
                    self.view.progressBar.setValue(i)
    
                self.deactivate_progressbar()
                
                if len(possible_candidates) > 1:

                    print u'Rethink the way you check uniqueness of sites!!!'
                    print u'This must never ever ever happen!!!!!!'

                elif len(possible_candidates) == 1:

                    site_to_be_updated = possible_candidates[0]

                    site_to_be_updated_dates = self.model.get_historylog_dictionary(site_to_be_updated).keys()
                    site_to_be_updated_dates.extend(self.model.get_ignored_dates(site_to_be_updated))

                    if len(site_to_be_updated_dates) > len(temp_dates):
                        self.message(u'The capturesite file seems to be affiliated with the already existing ' + 
                                     site_to_be_updated + u' site, but it contains fewer history log entries and thus ' +
                                     u'probably predates it. Aborting import.')

                    elif len(site_to_be_updated_dates) == len(temp_dates):
                        self.message(u'The capturesite file seems to be affiliated with the already existing ' + 
                                     site_to_be_updated + u' site. However, the number of entries in ' + 
                                     u'the capturesite file is the same as in your database. No new information will ' +
                                     u'be added. Aborting import.')
                    else:
                        clicked = self.message_with_cancel_choice(u'The capturesite file seems to be affiliated with the already existing ' + site_to_be_updated + ' site.', 
                                                            'Update ' + site_to_be_updated + '?', QtGui.QMessageBox.Ok)
                        if clicked == QtGui.QMessageBox.Ok:
                            self.update_site(site_to_be_updated, capturesite_filename)

                else:

                    self.create_new_site(capturesite_filename)

                self.model.remove_site_from_memory(temp_site_name)      # This could happen earlier!?!?!?!?!

                self.deactivate_progressbar()


            except Exception, e:
                self.message('Import failed.\n' + repr(e))
                #print 'Something went haywire when importint Capturesite.\n' + repr(e)
                self.deactivate_progressbar()


    # Update an existing site
    def update_site(self, site_name, capturesite_filename):
        
        self.activate_progressbar(3)
        self.view.progressBar.setValue(1)
        
        self.model.update_site(capturesite_filename, site_name)

        self.view.progressBar.setValue(2)

        del self.presentation_dict[site_name]
        self.presentation_dict[site_name] = self.colored_dates(site_name)
        
        self.view.progressBar.setValue(3)
        self.deactivate_progressbar()
        
        # Change the active_site to the site that just got updated. This also
        # updates the calendar!!!
        site_items = [u''] + self.model.get_site_names()
        new_index = site_items.index(site_name)
        self.view.comboBox_ActiveSite.setCurrentIndex(new_index)
        
        # If the new_index is the current actual index, the calendar will not get updated.
        # So, a bit ugly, here I force another update_calendar()!!!
        
        self.activate_progressbar(2)
        self.view.progressBar.setValue(1)
        self.update_calendar()
        self.update_menu()
        self.view.progressBar.setValue(2)
        self.deactivate_progressbar()

    # Create a new site from scratch
    def create_new_site(self, capturesite_filename):
        site_name, ok = QtGui.QInputDialog.getText(self.view, u'Enter a name for the new site', u'This capturesite file does not seem to be associated with any of the existing sites. Please name the new site:') 

        if ok:

            allowed_chars = u'abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789-_ '
            allowed_set = set(allowed_chars)
 
            if set(site_name) <= allowed_set and site_name != '':

                if site_name in self.model.get_site_names():
                    self.message(u'Site name already exists. Aborting.')

                else:
                    
                    try:
                        
                        self.activate_progressbar(3)
                        self.view.progressBar.setValue(1)
                        
                        self.model.create_new_site(capturesite_filename, site_name)

                        self.view.progressBar.setValue(2)

                        self.presentation_dict[site_name] = self.colored_dates(site_name)

                        self.view.progressBar.setValue(3)
                        self.deactivate_progressbar()

                        # Remove all items from comboBox
                        self.view.comboBox_ActiveSite.clear()

                        # Repopulate comboBox
                        site_items = [u''] + self.model.get_site_names()
                        self.view.comboBox_ActiveSite.addItems(site_items)

                        new_index = site_items.index(site_name)
                        self.view.comboBox_ActiveSite.setCurrentIndex(new_index)    # This also triggers the set_active_site method and makes the new site active!!!!
                        
                        self.active_site_name = site_name

                    except Exception, e:

                        self.message(u'An unexpected error occured during import. Aborting.')
                        self.deactivate_progressbar()

            else:

                self.message(u'Site name may only contain letters, numbers, -_ and space. Aborting.')
                self.deactivate_progressbar()

        #else:

        #    pass




    # Messaging the user stuff

    def message(self, text, title_text=''):
        msgBox = QtGui.QMessageBox(parent=self.view)
        msgBox.setText(text)
        if title_text:
            msgBox.setWindowTitle(title_text)
        msgBox.exec_()
        
    def message_with_cancel_choice(self, text, informative_text, default_button):
        msgBox = QtGui.QMessageBox()
        msgBox.setText(text)
        msgBox.setInformativeText(informative_text)
        msgBox.setStandardButtons(QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Ok)
        msgBox.setDefaultButton(default_button)
        return msgBox.exec_()
    




    # Menu stuff

    def update_menu(self):
        
        if self.active_site == u'':

            self.view.ignoreAction.setEnabled(False)
            self.view.deIgnoreAction.setEnabled(False)

        else:
            self.view.ignoreAction.setEnabled(True)

            if len(self.model.get_ignored_dates(self.active_site)) > 0:
                self.view.deIgnoreAction.setEnabled(True)
            else:
                self.view.deIgnoreAction.setEnabled(False)



    # ---------- Signals


    def new_date_chosen(self):
        self.update_text()
        self.update_comment()



    def connect_signals(self):
 
        self.view.quit.connect(self.model.quit)

        self.view.calendarWidget.selectionChanged.connect(self.new_date_chosen)

        self.view.pushButton_NewFilter.clicked.connect(self.new_filter)
        self.view.pushButton_EditFilter.clicked.connect(self.edit_filter)
        self.view.pushButton_DeleteFilter.clicked.connect(self.delete_filter)
        self.view.comboBox_ChooseFilter.currentIndexChanged.connect(self.choose_filter)

        self.view.pushButton_CommitStringSearch.clicked.connect(self.commit_string_search)
        self.view.pushButton_ResetStringSearch.clicked.connect(self.reset_string_search)

        self.view.comboBox_ActiveSite.currentIndexChanged.connect(self.set_active_site)
        self.view.comboBox_Coloring.currentIndexChanged.connect(self.set_coloring_scheme)

        self.view.importAction.triggered.connect(self.import_capturesite)
        self.view.ignoreAction.triggered.connect(self.ignore_date)
        self.view.deIgnoreAction.triggered.connect(self.deignore_all_dates)
        
        self.view.aboutAction.triggered.connect(self.about)

        self.view.pushButton_FirstEntry.clicked.connect(self.set_first_date)
        self.view.pushButton_LastEntry.clicked.connect(self.set_last_date)
        self.view.pushButton_Today.clicked.connect(self.set_active_date)

        self.view.pushButton_NextSearch.clicked.connect(self.set_next_search_date)
        self.view.pushButton_PreviousSearch.clicked.connect(self.set_previous_search_date)

        self.view.plainTextEdit_StringSearch.textChanged.connect(self.text_changed)
        self.view.plainTextEdit_StringSearch.returnPressed.connect(self.return_pressed)

        self.view.pushButton_SaveComment.clicked.connect(self.save_comment)
        self.view.pushButton_DeleteComment.clicked.connect(self.delete_comment)

        self.view.pushButton_NextComment.clicked.connect(self.set_next_comment_date)
        self.view.pushButton_PreviousComment.clicked.connect(self.set_previous_comment_date)





    # Ignore stuff

    def ignore_date(self):
        
        if not self.active_site == u'':
            date = self.view.calendarWidget.selectedDate()

            if (self.model.get_historylog(self.active_site, date) != u'No history log exists for this date.') and (date not in self.ignored_dates(self.active_site)): 
                try:
                    
                    
                    self.model.add_ignored_date(self.active_site, date)
                    self.model.remove_site_from_memory(self.active_site)
                    self.model.read_site_to_memory(self.active_site)

                    site_items = [u''] + self.model.get_site_names()
                    index = site_items.index(self.active_site)
                    self.set_active_site(index)
            
                    #del self.presentation_dict[self.active_site]
                    #self.presentation_dict[self.active_site] = self.colored_dates(self.active_site)
            
                    #self.color_all_dates()
                    #print 'e'
                    #self.commit_string_search()
                    #print 'f'
                    #self.update_calendar()
                    #print 'g'
                    #self.update_text()
                    #self.update_menu()
                    #print 'h'

                except Exception:

                    self.message(u'An error occured during ignore operation. Aborting.')

            else:
                self.message(u'The active site either has no historylog for this date, or the date has already been put on the ignore list.')


    def ignored_dates(self, site_name):
        return self.model.get_ignored_dates(site_name)


    def deignore_all_dates(self):
        if not self.active_site == u'':

            try:
                self.model.deignore_all_dates(self.active_site)
            except Exception:
                self.message(u'An error occured when clearing ignore list. Aborting.')

            self.model.remove_site_from_memory(self.active_site)
            self.model.read_site_to_memory(self.active_site)

            site_items = [u''] + self.model.get_site_names()
            index = site_items.index(self.active_site)
            self.set_active_site(index)

            #self.color_all_dates()
            #self.commit_string_search()
            #self.update_calendar()
            ##self.update_text()
            #self.update_menu()



    # Comments stuff


    def active_date(self):                                          # Move this method
        return self.view.calendarWidget.selectedDate()


    def save_comment(self):
        if not self.active_site == u'':
            commented_dates = [date for date in self.model.get_comment_dictionary(self.active_site).keys()]
            if self.active_date() in commented_dates:

            # Does comment exist for this date?
            #if self.model.get_comment(self.active_site, self.active_date()):

                # Has the text been changed?
                #if self.comment_text_changed:

                clicked = self.message_with_cancel_choice(u'Comment already exists for this date.', u'Overwrite?', QtGui.QMessageBox.Ok)

                if clicked == QtGui.QMessageBox.Ok:
                    # Save it
                    text_to_save = self.view.plainTextEdit_Comment.toPlainText()
                    self.model.save_comment(self.active_site, self.view.calendarWidget.selectedDate(), text_to_save)
            else:
                # Just save it
                text_to_save = self.view.plainTextEdit_Comment.toPlainText()
                self.model.save_comment(self.active_site, self.view.calendarWidget.selectedDate(), text_to_save)
            #text_to_save = self.view.plainTextEdit_Comment.toPlainText()
            #self.model.save_comment(self.active_site, self.view.calendarWidget.selectedDate(), text_to_save)
            self.update_comment()
            self.update_calendar()


    def delete_comment(self):
        if not self.active_site == u'':
            commented_dates = [date for date in self.model.get_comment_dictionary(self.active_site).keys()]
            if self.active_date() in commented_dates:
        
                clicked = self.message_with_cancel_choice(u'Comment will be removed from the database.', u'Continue?', QtGui.QMessageBox.Cancel)
                if clicked == QtGui.QMessageBox.Ok:
                    self.model.delete_comment(self.active_site, self.active_date())
                    self.update_comment()
                    self.update_calendar()

            else:

                self.update_comment()


    def update_comment(self):
        
        date = self.view.calendarWidget.selectedDate()
            
        if self.active_site == u'':
            text = u''
        else:
            text = self.model.get_comment(self.active_site, self.view.calendarWidget.selectedDate())
            
        if text:
            self.view.plainTextEdit_Comment.setPlainText(text)
        else:
            self.view.plainTextEdit_Comment.clear()

        if self.active_site == u'':
            comment_dates = []
        else:
            comment_dates = [date for date in self.model.get_comment_dictionary(self.active_site).keys()]
            
        self.view.calendarWidget.setTriangleDates(comment_dates)


    def set_next_comment_date(self):
        if not self.active_site == u'':
            dates = sorted([date for date, _ in self.model.get_comment_dictionary(self.active_site).items()])
            if not len(dates) == 0:
                greater_dates = [date for date in dates if date > self.active_date()]
                if len(greater_dates) == 0:
                    new_index = 0
                else:
                    new_index = dates.index(greater_dates[0])
                self.view.calendarWidget.setSelectedDate(dates[new_index])
                self.view.calendarWidget.updateCells()



    def set_previous_comment_date(self):
        if not self.active_site == u'':
            dates = sorted([date for date, _ in self.model.get_comment_dictionary(self.active_site).items()])
            if not len(dates) == 0:
                lesser_dates = [date for date in dates if date < self.active_date()]
                if len(lesser_dates) == 0:
                    new_index = -1
                else:
                    new_index = dates.index(lesser_dates[-1])
                self.view.calendarWidget.setSelectedDate(dates[new_index])
                self.view.calendarWidget.updateCells()











    def about(self):

#        QtGui.QMessageBox.about(self.view, u'About', u'''
#GCA Analysis Tool, v1.29 Trial
#
#Copyright © 2016, 2017 Oscar Franzén <oscarfranzen@protonmail.com>
#
#This is a trial version of the GCA Analysis Tool. It is fully functional, but will only display dates prior to July 2, 2018.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#Software used:
#Python 2.7.14, PSF License
#PySide 1.2.4, LGPL version 2.1
#Qt 4.8.6, LGPL version 3
#''')

        self.message(u'''
GCA Analysis Tool, v1.60 (trial version)

Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>

This is a trial version of the GCA Analysis Tool. The trial version is fully functional, but will only display dates prior to July 2, 2018. It may be copied freely.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Software used:
Python 2.7.14, PSF License
PySide 1.2.4, LGPL version 2.1
Qt 4.8.6, LGPL version 3
''', u'About GCA Analysis Tool')


#    def about(self):

#        self.message(u'''
#<a rel="license" href="http://creativecommons.org/licenses/by-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nd/4.0/">Creative Commons Attribution-NoDerivatives 4.0 International License</a>.
#''')