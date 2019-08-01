#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore, QtGui, QtWidgets


class IgnorePresenter(QtCore.QObject):

    def __init__(self, model, mainwindow, mainwindowpresenter):
        super(IgnorePresenter, self).__init__()
        self.model = model
        self.mainwindow = mainwindow
        self.mainwindowpresenter = mainwindowpresenter



    def ignore_date(self):
        
        if not self.mainwindowpresenter.active_site_name == u'':

            if (self.model.get_historylog(self.mainwindowpresenter.active_site_name, self.mainwindowpresenter.selected_date) != u'No history log exists for this date.') and (self.mainwindowpresenter.selected_date not in self.ignored_dates(self.mainwindowpresenter.active_site_name)): 
                
                try:
                    
                    self.model.add_ignored_date(self.mainwindowpresenter.active_site_name, self.mainwindowpresenter.selected_date)
                    self.mainwindowpresenter.reload_active_site()
                    
                except Exception as e:

                    self.mainwindowpresenter.message(u'An error occured during ignore operation. Aborting.')

            else:
                self.mainwindowpresenter.message(u'The active site either has no historylog for this date, or the date has already been put on the ignore list.')


    def ignored_dates(self, site_name):
        return self.model.get_ignored_dates(site_name)


    def jump_to_next_ignored_date(self):
        if self.mainwindowpresenter.active_site_name != u'' and len(self.ignored_dates(self.mainwindowpresenter.active_site_name)) > 0:

            c = 0
            for ignored_date in sorted(self.ignored_dates(self.mainwindowpresenter.active_site_name)):
                if self.mainwindowpresenter.selected_date < ignored_date:
                    self.mainwindowpresenter.selected_date = ignored_date
                    break
                else:
                    c += 1

            if c == len(self.ignored_dates(self.mainwindowpresenter.active_site_name)):
                self.mainwindowpresenter.selected_date = sorted(self.ignored_dates(self.mainwindowpresenter.active_site_name))[0]


    def deignore_all_dates(self):
        if not self.mainwindowpresenter.active_site_name == u'':

            try:
                self.model.deignore_all_dates(self.mainwindowpresenter.active_site_name)
                self.mainwindowpresenter.reload_active_site()
            
            except Exception as e:

                self.mainwindowpresenter.message(u'An error occured when clearing ignore list. Aborting.')


    def deignore_date(self):

        if not self.mainwindowpresenter.active_site_name == u'':

            try:
                self.model.deignore_date(self.mainwindowpresenter.active_site_name, self.mainwindowpresenter.selected_date)
                self.mainwindowpresenter.reload_active_site()
            
            except Exception as e:

                self.mainwindowpresenter.message(u'An error occured when clearing ignore list. Aborting.')
