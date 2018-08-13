# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


#import os 
#import string
#import time
from PySide2 import QtCore, QtGui, QtWidgets
#from presenter.coloringcontainer import ColoringContainer
#import presenter.textstuff as txt
#from presenter.filtercontainer import Filter
#from view.myfilterdialog import MyFilterDialog
#from presenter.eventfilter import EventBlocker

class IgnorePresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        super(IgnorePresenter, self).__init__()
        self.model = model
        self.view = view
        self.presenter = presenter



    # Ignore stuff

    def ignore_date(self):
        
        if not self.presenter.active_site_name == u'':
            date = self.view.calendarWidget.selectedDate()

            if (self.model.get_historylog(self.presenter.active_site_name, date) != u'No history log exists for this date.') and (date not in self.ignored_dates(self.presenter.active_site_name)): 
                try:
                    
                    
                    self.model.add_ignored_date(self.presenter.active_site_name, date)
                    self.model.remove_site_from_memory(self.presenter.active_site_name)
                    self.model.read_site_to_memory(self.presenter.active_site_name)

                    site_items = [u''] + self.model.get_site_names()
                    index = site_items.index(self.presenter.active_site_name)
                    
                    self.presenter.set_active_site(index)
            
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

                    self.presenter.message(u'An error occured during ignore operation. Aborting.')

            else:
                self.presenter.message(u'The active site either has no historylog for this date, or the date has already been put on the ignore list.')


    def ignored_dates(self, site_name):
        return self.model.get_ignored_dates(site_name)


    def deignore_all_dates(self):
        if not self.presenter.active_site_name == u'':

            try:
                self.model.deignore_all_dates(self.presenter.active_site_name)
            except Exception:
                self.message(u'An error occured when clearing ignore list. Aborting.')

            self.model.remove_site_from_memory(self.presenter.active_site_name)
            self.model.read_site_to_memory(self.presenter.active_site_name)

            site_items = [u''] + self.model.get_site_names()
            index = site_items.index(self.presenter.active_site_name)
            self.presenter.set_active_site(index)

            #self.color_all_dates()
            #self.commit_string_search()
            #self.update_calendar()
            ##self.update_text()
            #self.update_menu()

