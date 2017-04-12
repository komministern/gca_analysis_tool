#!/usr/bin/env python
# -*- coding: utf-8 -*-


#    Copyright © 2016, 2017 Oscar Franzén <oscarfranzen@yahoo.se>
#
#    This file is part of GCA Analysis Tool.


import os
import string
from PySide import QtCore, QtGui
from coloringcontainer import ColoringContainer
import textstuff as txt
from filtercontainer import Filter


class MyPresenter(QtCore.QObject):

    def __init__(self, model, view, **kwds):
	super(MyPresenter, self).__init__(**kwds)

        # Store view and model.
        self._model = model
        self._view = view


        #print self.trial_has_ended

        # Setup all signals.
        self.connect_signals()

        # Initialize properties
#        self.suppressed_codes = []

#        self.filters = [u'', u'1', u'2']
#        self.view.comboBox_ChooseFilter.addItems(self.filters)
        

        #self.current_filter = 

        self.highlight = ''
        self.presentation_dict = {}
        self.active_site = None
        self.coloring_scheme = 0

        self.comment_text_changed = False


        # Colors
        self.green = QtGui.QColor.fromRgbF(0.248478, 1.000000, 0.431632, 1.000000)
        self.red = QtGui.QColor.fromRgbF(1.000000, 0.343099, 0.419516, 1.000000)
        self.yellow = QtGui.QColor.fromRgbF(1.000000, 0.997757, 0.346044, 1.000000)
        self.blue = QtGui.QColor.fromRgbF(0.509743, 0.734401, 1.000000, 1.000000)

        self.view.comboBox_Coloring.addItems([u'Normal/Degraded/Faulted', u'New Fault/Active Fault', 
                                            u'Temporary Faults (< 1 min per day)', u'Transmitter On'])


        self.filter0 = Filter()
        
        self.filter1 = Filter()
        self.filter1.content = [u'(23)']
        self.filter1.state = 1
        self.filter1.name = u'show filter 1'
        
        self.filter2 = Filter()
        self.filter2.state = 0
        self.filter2.content = [u'(23)', u'(24)', u'(23)', u'(24)', u'(23)', u'(24)', u'(23)', u'(24)']
        self.filter2.name = u'suppress filter 2'

        self.filters = [self.filter0, self.filter1, self.filter2]
        self.current_filter = self.filters[0]
        
        self.view.comboBox_ChooseFilter.addItems([each.name for each in self.filters])


        # The first element in the items list above will be initially selected
        self.color_all_dates()

        self.trial_has_ended = False
        if len(self.get_site_names()) > 0:

            # Check if trial is up
            #self.trial_has_ended = False
            for site_name in self.get_site_names():
                if self.get_third_last_entry_date(site_name).year() > 2017:
                    self.trial_has_ended = True

            self.view.comboBox_ActiveSite.addItems(self.get_site_names())
            self.active_site = self.get_site_names()[0]

        self.update_calendar()
        self.update_text()
        self.update_comment()

        self.update_menu()

#        if self.trial_has_ended:
#           self.message('Trial has ended.')
#           print 'dddddddddd'
#           self.view.quit.emit()



    # --------- Coloring the dates


    def color_all_dates(self):
        for site_name in self.get_site_names():
            self.presentation_dict[site_name] = self.colored_dates(site_name)


    def colored_dates(self, site_name):

        if self.coloring_scheme == 0:       # Normal/Degraded/Faulted

            red_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if txt.faulted(text)]
            yellow_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if txt.degraded(text) and date not in red_dates]
            green_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if txt.normal(text) and (date not in red_dates) and (date not in yellow_dates)]
            white_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if (date not in red_dates) and (date not in yellow_dates) and (date not in green_dates)]

            lower_right_red_dates = red_dates
            lower_right_green_dates = green_dates
 
            upper_left_red_dates = red_dates
            upper_left_green_dates = green_dates

            upper_left_white_dates = white_dates
            upper_left_yellow_dates = yellow_dates

            lower_right_white_dates = white_dates
            lower_right_yellow_dates = yellow_dates

        elif self.coloring_scheme == 1:     # New Fault/Active Fault
        
            lower_right_red_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if txt.active_fault_in(text)]
            lower_right_green_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if txt.no_active_fault_in(text)]
 
            upper_left_red_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if txt.new_fault_in(text)]
            upper_left_green_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if txt.no_new_fault_in(text)]

            upper_left_white_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if date not in upper_left_red_dates and date not in upper_left_green_dates]
            upper_left_yellow_dates = []
            
            lower_right_white_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if date not in lower_right_red_dates and date not in lower_right_green_dates]
            lower_right_yellow_dates = []

        elif self.coloring_scheme == 2:     # Temporary Faults

            red_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if txt.new_fault_in(text) and 
                            (not txt.degraded(text)) and (not txt.faulted(text))]
            white_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if date not in red_dates]

            lower_right_red_dates = red_dates
            upper_left_red_dates = red_dates
           
            lower_right_green_dates = []
 
            upper_left_green_dates = []

            upper_left_white_dates = white_dates
            upper_left_yellow_dates = []
            
            lower_right_white_dates = white_dates
            lower_right_yellow_dates = []

        elif self.coloring_scheme == 3:     # Transmitter on

            green_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if txt.transmitter_on(text)]
            white_dates = [date for date, text in self.get_historylog_dictionary(site_name).items() if date not in green_dates]

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

        if self.active_site:

            self.view.calendarWidget.setUpperLeftRedDates( self.presentation_dict[self.active_site].upper_left_red_dates )
            self.view.calendarWidget.setUpperLeftGreenDates( self.presentation_dict[self.active_site].upper_left_green_dates )
            self.view.calendarWidget.setUpperLeftWhiteDates( self.presentation_dict[self.active_site].upper_left_white_dates )
            self.view.calendarWidget.setUpperLeftYellowDates( self.presentation_dict[self.active_site].upper_left_yellow_dates )

            self.view.calendarWidget.setLowerRightRedDates( self.presentation_dict[self.active_site].lower_right_red_dates )
            self.view.calendarWidget.setLowerRightGreenDates( self.presentation_dict[self.active_site].lower_right_green_dates )
            self.view.calendarWidget.setLowerRightWhiteDates( self.presentation_dict[self.active_site].lower_right_white_dates )
            self.view.calendarWidget.setLowerRightYellowDates( self.presentation_dict[self.active_site].lower_right_yellow_dates )

            self.view.calendarWidget.updateCells()

    def set_active_site(self, index):
        self.active_site = self.get_site_names()[index]
        self.commit_string_search()     # self.update_text() is called in this procedure.
        #self.update_text()
        self.update_calendar()

        self.update_comment()
        self.update_menu()

    def set_coloring_scheme(self, index):
        self.coloring_scheme = index
        self.color_all_dates()
        self.update_calendar() 

    def set_last_date(self):
        if self.active_site:
            self.set_selected_date(self.get_last_entry_date(self.active_site))
            self.update_calendar()

    def set_first_date(self):
        if self.active_site:
            self.set_selected_date(self.get_first_entry_date(self.active_site))
            self.update_calendar()

    def set_active_date(self):
        self.view.calendarWidget.setSelectedDate(self.view.calendarWidget.selectedDate())
        self.update_calendar()

    def set_selected_date(self, date):
        self.view.calendarWidget.setSelectedDate(date)



    # ---------- Text stuff


    def update_text(self):

        if self.active_site:
            date = self.view.calendarWidget.selectedDate()
            text = self.get_historylog(self.active_site, date)
            self.view.textBrowser_HistoryLog.setPlainText(self.format_text(text))

            if self.highlight != '' and text != u'No history log exists for this date.': 

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

            self.update_comment()   # Here?????????????????????????




    # ----------- Filter stuff


    def format_text(self, text):
        if text != u'No history log exists for this date.':
            if self.current_filter.state == 1 and self.current_filter.content:  # Show Only
                return '\n'.join([s for s in text.splitlines() if s[0:4] in self.current_filter.content])
            elif self.current_filter.state == 0:        # Suppress
                return '\n'.join([s for s in text.splitlines() if not s[0:4] in self.current_filter.content])
        return text



    def show_filter_dialog(self, initial_filter):
        from view.myfilterdialog import MyFilterDialog
        self.dialog = MyFilterDialog(initial_filter)
        if self.dialog.exec_():
            print self.dialog.get_final_filter().name
#        self.wid = QtGui.QWidget()
#        self.wid.resize(250, 150)
#        self.wid.setWindowTitle('NewWindow')
#        self.wid.show()



    def new_filter(self):
        self.show_filter_dialog(Filter())

    def edit_filter(self):
        self.show_filter_dialog(self.current_filter)

    def delete_filter(self):
        print 'delete filter'

    def choose_filter(self, index):
        if index == 0:
            self.view.pushButton_EditFilter.setEnabled(False)
            self.view.pushButton_DeleteFilter.setEnabled(False)
        else:
            self.view.pushButton_EditFilter.setEnabled(True)
            self.view.pushButton_DeleteFilter.setEnabled(True)
            
        self.current_filter = self.filters[index]
        self.update_text()


    # ------------ String search stuff


    def commit_string_search(self):
        if self.active_site:
            self.highlight = self.view.lineEdit_StringSearch.text()

            self.view.calendarWidget.setCircledDates(self.list_of_search_string_dates(self.view.lineEdit_StringSearch.text()))
        
            self.view.calendarWidget.updateCells()
            self.update_text()


    def list_of_search_string_dates(self, astring):
        if not astring == '':
            return [date for date, text in self.get_historylog_dictionary(self.active_site).items() if astring in text]
        else:
            return []


    def reset_string_search(self):
        self.view.calendarWidget.setCircledDates([])
        self.view.lineEdit_StringSearch.setText('')
        self.highlight = ''
        self.view.calendarWidget.updateCells()
        self.update_text()


    def set_next_search_date(self):
        if self.active_site:
            dates = sorted(self.list_of_search_string_dates(self.view.lineEdit_StringSearch.text()))
            if not len(dates) == 0:
                greater_dates = [date for date in dates if date > self.view.calendarWidget.selectedDate()]

                if len(greater_dates) == 0:
                    new_index = 0
                else:
                    new_index = dates.index(greater_dates[0])
                self.view.calendarWidget.setSelectedDate(dates[new_index])
                self.view.calendarWidget.updateCells()


    def set_previous_search_date(self):
        if self.active_site:
            dates = sorted(self.list_of_search_string_dates(self.view.lineEdit_StringSearch.text()))
            if not len(dates) == 0:
                lesser_dates = [date for date in dates if date < self.view.calendarWidget.selectedDate()]
                if len(lesser_dates) == 0:
                    new_index = -1
                else:
                    new_index = dates.index(lesser_dates[-1])            
                self.view.calendarWidget.setSelectedDate(dates[new_index])
                self.view.calendarWidget.updateCells()


    def text_changed(self):
        if not self.highlight == '':
            
            self.highlight = ''
            self.update_text()

            self.view.calendarWidget.setCircledDates([])
            self.view.calendarWidget.updateCells()
            

    def return_pressed(self):
        self.view.pushButton_CommitStringSearch.animateClick()
        self.view.pushButton_CommitStringSearch.clicked.emit()




    # ---------- Import a capturesite file


    def import_capturesite(self):

        capturesite_filename, test = QtGui.QFileDialog.getOpenFileName(self.view, u'Capturesite', self.model.home_directory, u'Capturesite (*tar.gz)')
        #apturesite_filename, test = QtGui.QFileDialog.getOpenFileName(self.view, u'Capturesite', os.path.expanduser(u'~'), u'Capturesite (*tar.gz)')

        if capturesite_filename:

            temp_site_name = u'_TEMP'

            self.create_site(capturesite_filename, temp_site_name)

            temp_dates = sorted(self.model.get_historylog_dictionary(temp_site_name).keys())
            #print temp_dates


#            temp_first_date = self.get_first_entry_date(temp_site_name)
#            temp_first_date_text = self.model.get_historylog(temp_site_name, temp_first_date)
#            temp_last_date = self.get_last_entry_date(temp_site_name)

            self.model.remove_site_from_disc(temp_site_name)

#            possible_candidates = [site_name for site_name in self.get_site_names() if 
                    
                    
#                    self.model.get_historylog(site_name, temp_first_date) == temp_first_date_text and 
#                    self.model.get_historylog(site_name, self.get_last_entry_date(site_name)) == 
#                        self.model.get_historylog(temp_site_name, self.get_last_entry_date(site_name))
#                    ]

            possible_candidates = []

            for site_name in self.get_site_names():

                # Create list of all site dates, including the ignored dates
                site_dates = self.model.get_historylog_dictionary(site_name).keys()
                site_dates.extend(self.model.get_ignored_dates(site_name))
                site_dates = sorted(site_dates)     # UGLY

                #print site_name
                #print ( set(site_dates) ^ set(temp_dates) )
                #print '\n\n\n'

                #print site_dates

                # If all historylog dates are in site_name's history log
                #print temp_dates
                if len(temp_dates) >= len(site_dates) and (set(temp_dates) >= set(site_dates)): # and (temp_dates[0] == site_dates[0]):
                    possible_candidates.append(site_name)
                    #print site_name
                    #print site_dates[10]
                    #print temp_dates[10]

                elif len(temp_dates) < len(site_dates) and (set(temp_dates) <= set(site_dates)):
                    possible_candidates.append(site_name)
                    #print '_' + site_name
                    



            if len(possible_candidates) > 1:

                print u'Rethink the way you check uniqueness of sites!!!'
                print u'This must never happen!!!!!!'

            elif len(possible_candidates) == 1:

                site_to_be_updated = possible_candidates[0]

                site_to_be_updated_dates = self.model.get_historylog_dictionary(site_to_be_updated).keys()
                site_to_be_updated_dates.extend(self.model.get_ignored_dates(site_to_be_updated))

                if len(site_to_be_updated_dates) > len(temp_dates):
                    self.message(u'The capturesite file seems to be affiliated with the already existing ' + site_to_be_updated + ' site, but it contains fewer history log entries and thus probably predates it. Aborting import.')

                elif len(site_to_be_updated_dates) == len(temp_dates):

                    clicked = self.message_with_cancel_choice(u'The capturesite file seems to be affiliated with the already existing ' +
                                                            site_to_be_updated + u' site. However, the number of entries in ' +
                                                            u'the capturesite file is the same as in your database. No new information will be added.', 
                                                            u'Do you still want to update ' + site_to_be_updated + '?',
                                                            QtGui.QMessageBox.Cancel)
                    if clicked == QtGui.QMessageBox.Ok:
                        self.update_site(site_to_be_updated, capturesite_filename)

                else:
                    clicked = self.message_with_cancel_choice(u'The capturesite file seems to be affiliated with the already existing ' + site_to_be_updated + ' site.', 
                                                            'Update ' + site_to_be_updated + '?', QtGui.QMessageBox.Ok)
                    if clicked == QtGui.QMessageBox.Ok:
                        self.update_site(site_to_be_updated, capturesite_filename)

            else:

                self.create_new_site(capturesite_filename)

            self.model.remove_site_from_memory(temp_site_name)      # This could happen earlier!?!?!?!?!



    # Update an existing site


    def update_site(self, site_name, capturesite_filename):
#        print u'Updating ' + site_name + u' with ' + capturesite_filename
        self.model.update_site(capturesite_filename, site_name)

        del self.presentation_dict[site_name]
        
        self.presentation_dict[site_name] = self.colored_dates(site_name)

    # Create a new site from scratch


    def create_new_site(self, capturesite_filename):
        site_name, ok = QtGui.QInputDialog.getText(self.view, u'New Site', u'This capturesite file does not seem to be associated with any of the existing sites. Please name the new site:') 

        if ok:

            allowed_chars = u'abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789-_ '
            allowed_set = set(allowed_chars)
 
            if set(site_name) <= allowed_set and site_name != '':

                if site_name in self.get_site_names():
                    self.message(u'Site name already exists. Aborting.')

                else:
                    
                    try:
                        self.model.create_new_site(capturesite_filename, site_name)

                        self.presentation_dict[site_name] = self.colored_dates(site_name)

                        # Remove all items from comboBox
                        self.view.comboBox_ActiveSite.clear()

                        # Repopulate comboBox
                        self.view.comboBox_ActiveSite.addItems(self.get_site_names())

                        new_index = self.get_site_names().index(site_name)
                    
                        self.view.comboBox_ActiveSite.setCurrentIndex(new_index)    # This also triggers the set_active_site method and makes the new site active!!!!

                    except Exception:

                        self.message(u'An unexpected error occured. Aborting.')

            else:

                self.message(u'Site name may only contain letters, numbers, -_ and space. Aborting.')

        else:

            pass



    # Messaging the user stuff

    def message(self, text):
        msgBox = QtGui.QMessageBox()
        msgBox.setText(text)
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
        
        if not self.active_site:

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

 #       self.view.checkBox_Temperature.stateChanged.connect(self.temperature_filter)
 #       self.view.checkBox_HeaterControl.stateChanged.connect(self.heatercontrol_filter)
 #       self.view.checkBox_Transmitter.stateChanged.connect(self.transmitter_filter)
 #       self.view.checkBox_AntennaDrive.stateChanged.connect(self.antennadrive_filter)

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
        
#self.view.aboutAction.triggered.connect(self.view.about)
        self.view.aboutAction.triggered.connect(self.about)

        self.view.pushButton_FirstEntry.clicked.connect(self.set_first_date)
        self.view.pushButton_LastEntry.clicked.connect(self.set_last_date)
        self.view.pushButton_Today.clicked.connect(self.set_active_date)

        self.view.pushButton_NextSearch.clicked.connect(self.set_next_search_date)
        self.view.pushButton_PreviousSearch.clicked.connect(self.set_previous_search_date)

        self.view.lineEdit_StringSearch.textChanged.connect(self.text_changed)
        self.view.lineEdit_StringSearch.returnPressed.connect(self.return_pressed)

        self.view.pushButton_SaveComment.clicked.connect(self.save_comment)
        self.view.pushButton_DeleteComment.clicked.connect(self.delete_comment)

        self.view.pushButton_NextComment.clicked.connect(self.set_next_comment_date)
        self.view.pushButton_PreviousComment.clicked.connect(self.set_previous_comment_date)





    # Ignore stuff

    def ignore_date(self):
        
        if self.active_site:
            date = self.view.calendarWidget.selectedDate()

            if (self.get_historylog(self.active_site, date) != u'No history log exists for this date.') and (date not in self.ignored_dates(self.active_site)): 
                try:

                    self.model.add_ignored_date(self.active_site, date)

                    self.model.remove_site_from_memory(self.active_site)
                    self.model.read_site_to_memory(self.active_site)

            
                    self.color_all_dates()
                    self.commit_string_search()
                    self.update_calendar()
                    #self.update_text()
                    self.update_menu()

                except Exception:

                    self.message(u'An error occured during ignore operation. Aborting.')

            else:
                self.message(u'The active site either has no historylog for this date, or the date has already been put on the ignore list.')


    def ignored_dates(self, site_name):
        return self.model.get_ignored_dates(site_name)


    def deignore_all_dates(self):
        if self.active_site:

            try:
                self.model.deignore_all_dates(self.active_site)
            except Exception:
                self.message(u'An error occured when clearing ignore list. Aborting.')

            self.model.remove_site_from_memory(self.active_site)
            self.model.read_site_to_memory(self.active_site)

            self.color_all_dates()
            self.commit_string_search()
            self.update_calendar()
            #self.update_text()
            self.update_menu()



    # Comments stuff


    def active_date(self):                                          # Move this method
        return self.view.calendarWidget.selectedDate()


    def save_comment(self):
        if self.active_site:
            commented_dates = [date for date in self.get_comment_dictionary(self.active_site).keys()]
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
        if self.active_site:
            commented_dates = [date for date in self.get_comment_dictionary(self.active_site).keys()]
            if self.active_date() in commented_dates:
        
                clicked = self.message_with_cancel_choice(u'Comment will be removed from the database.', u'Continue?', QtGui.QMessageBox.Cancel)
                if clicked == QtGui.QMessageBox.Ok:
                    self.model.delete_comment(self.active_site, self.active_date())
                    self.update_comment()
                    self.update_calendar()

            else:

                self.update_comment()


    def update_comment(self):
        if self.active_site:
            date = self.view.calendarWidget.selectedDate()
            text = self.model.get_comment(self.active_site, self.view.calendarWidget.selectedDate())
            if text:
                self.view.plainTextEdit_Comment.setPlainText(text)
            else:
                self.view.plainTextEdit_Comment.clear()

            comment_dates = [date for date in self.get_comment_dictionary(self.active_site).keys()]
            self.view.calendarWidget.setTriangleDates(comment_dates)


    def set_next_comment_date(self):
        if self.active_site:
            dates = sorted([date for date, _ in self.get_comment_dictionary(self.active_site).items()])
            if not len(dates) == 0:
                greater_dates = [date for date in dates if date > self.active_date()]
                if len(greater_dates) == 0:
                    new_index = 0
                else:
                    new_index = dates.index(greater_dates[0])
                self.view.calendarWidget.setSelectedDate(dates[new_index])
                self.view.calendarWidget.updateCells()



    def set_previous_comment_date(self):
        if self.active_site:
            dates = sorted([date for date, _ in self.get_comment_dictionary(self.active_site).items()])
            if not len(dates) == 0:
                lesser_dates = [date for date in dates if date < self.active_date()]
                if len(lesser_dates) == 0:
                    new_index = -1
                else:
                    new_index = dates.index(lesser_dates[-1])
                self.view.calendarWidget.setSelectedDate(dates[new_index])
                self.view.calendarWidget.updateCells()









# --------- Methods accessing the model (remove altogether???)

    def create_site(self, capturesite_filename, site_name):
        self.model.create_new_site(capturesite_filename, site_name)


    def remove_site(self, site_name):
        self.model.remove_site_from_memory(site_name)
        self.model.remove_site_from_disc(site_name)


    def get_site_names(self):
        return self.model.get_site_names()


    def get_historylog(self, site_name, date):
        return self.model.get_historylog(site_name, date)


    def get_historylog_dictionary(self, site_name):
        return self.model.get_historylog_dictionary(site_name)

    
    def get_comment_dictionary(self, site_name):
        return self.model.get_comment_dictionary(site_name)


    def get_first_entry_date(self, site_name):
        return self.model.get_first_entry_date(site_name)


    def get_last_entry_date(self, site_name):
        return self.model.get_last_entry_date(site_name)


    def get_third_last_entry_date(self, site_name):
        return self.model.get_third_last_entry_date(site_name)



    def about(self):

        self.message(u'''
GCA Analysis Tool, v0.92 Trial

Copyright © 2016, 2017 Oscar Franzén <oscarfranzen@protonmail.com>

This is a trial version of the GCA Analysis Tool. It will be fully functional until January 2018, and may during this time be copied freely and used without restrictions.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Third party software used:
PySide 1.2.4, LGPL version 2.1
Qt 4.8.6, LGPL version 3
''')

