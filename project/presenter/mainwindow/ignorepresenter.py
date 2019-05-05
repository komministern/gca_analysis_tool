#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore, QtGui, QtWidgets


class IgnorePresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        super(IgnorePresenter, self).__init__()
        self.model = model
        self.view = view
        self.presenter = presenter



    def ignore_date(self):
        
        if not self.presenter.mainwindow.active_site_name == u'':
            date = self.view.mainwindow.calendarWidget.selectedDate()

            if (self.model.get_historylog(self.presenter.mainwindow.active_site_name, date) != u'No history log exists for this date.') and (date not in self.ignored_dates(self.presenter.mainwindow.active_site_name)): 
                try:
                    
                    #self.presenter.add_ignored_date(self.presenter.mainwindow.active_site_name, date)
                    self.model.add_ignored_date(self.presenter.mainwindow.active_site_name, date)

                    site_items = [u''] + self.model.get_site_names()
                    index = site_items.index(self.presenter.mainwindow.active_site_name)
                    
                    self.presenter.mainwindow.set_active_site(index)

                    self.presenter.mainwindow.menu.update_menu()

                    

                except Exception as e:

                    self.presenter.mainwindow.message(u'An error occured during ignore operation. Aborting.')
                    print(e)

            else:
                self.presenter.mainwindow.message(u'The active site either has no historylog for this date, or the date has already been put on the ignore list.')


    def ignored_dates(self, site_name):
        return self.model.get_ignored_dates(site_name)


    def jump_to_next_ignored_date(self):

        active_date = self.view.mainwindow.calendarWidget.selectedDate()
        active_site = self.presenter.mainwindow.active_site_name

        if active_site != '' and len(self.ignored_dates(active_site)) > 0:

            c = 0
            for ignored_date in sorted(self.ignored_dates(active_site)):
                print(ignored_date)
                if active_date < ignored_date:
                    self.presenter.mainwindow.calendar.set_selected_date(ignored_date)
                    self.presenter.mainwindow.calendar.update_calendar()
                    break
                else:
                    c += 1
                    print(c)

            if c == len(self.ignored_dates(active_site)):
                self.presenter.mainwindow.calendar.set_selected_date(sorted(self.ignored_dates(active_site))[0])
                self.presenter.mainwindow.calendar.update_calendar()



    def deignore_all_dates(self):
        if not self.presenter.mainwindow.active_site_name == u'':

            try:
                #self.presenter.remove_all_ignored_dates(self.presenter.mainwindow.active_site_name)
                self.model.deignore_all_dates(self.presenter.mainwindow.active_site_name)

                site_items = [u''] + self.model.get_site_names()
                index = site_items.index(self.presenter.mainwindow.active_site_name)
                self.presenter.mainwindow.set_active_site(index)
            
            except Exception as e:
                self.presenter.mainwindow.message(u'An error occured when clearing ignore list. Aborting.')
                #print(e)
        
        self.presenter.mainwindow.menu.update_menu()

    def deignore_date(self):

        date = self.view.mainwindow.calendarWidget.selectedDate()

        if not self.presenter.mainwindow.active_site_name == u'':

            try:
                #self.presenter.remove_all_ignored_dates(self.presenter.mainwindow.active_site_name)
                self.model.deignore_date(self.presenter.mainwindow.active_site_name, date)

                site_items = [u''] + self.model.get_site_names()
                index = site_items.index(self.presenter.mainwindow.active_site_name)
                self.presenter.mainwindow.set_active_site(index)
            
            except Exception as e:
                self.presenter.mainwindow.message(u'An error occured when clearing ignore list. Aborting.')
                #print(e)

        self.presenter.mainwindow.menu.update_menu()