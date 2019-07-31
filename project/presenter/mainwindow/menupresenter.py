#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore, QtGui, QtWidgets


class MenuPresenter(QtCore.QObject):

    def __init__(self, model, mainwindow, mainwindowpresenter):
        super(MenuPresenter, self).__init__()
        self.model = model
        self.mainwindow = mainwindow
        self.mainwindowpresenter = mainwindowpresenter

        self.mainwindow.noWrapAction.setCheckable(True)
        self.mainwindow.wrapAction.setCheckable(True)
        self.mainwindow.noWrapAction.setChecked(True)


    def update_menu(self):
        
        if self.mainwindowpresenter.active_site_name == u'':

            self.mainwindow.ignoreAction.setEnabled(False)
            self.mainwindow.deIgnoreAction.setEnabled(False)
            self.mainwindow.deIgnoreAllAction.setEnabled(False)
            self.mainwindow.nextIgnoredDateAction.setEnabled(False)

            self.mainwindow.analysisAction.setEnabled(False)

        else:

            self.mainwindow.analysisAction.setEnabled(True)

            if self.mainwindowpresenter.active_date not in self.model.get_ignored_dates(self.mainwindowpresenter.active_site_name):

                self.mainwindow.deIgnoreAction.setEnabled(False)
                
                text = self.model.get_historylog(self.mainwindowpresenter.active_site_name, self.mainwindowpresenter.active_date)
                if text != 'No history log exists for this date.':
                    self.mainwindow.ignoreAction.setEnabled(True)

            else:
                self.mainwindow.ignoreAction.setEnabled(False)
                self.mainwindow.deIgnoreAction.setEnabled(True)


            if len(self.model.get_ignored_dates(self.mainwindowpresenter.active_site_name)) > 0:
                self.mainwindow.deIgnoreAllAction.setEnabled(True)
                self.mainwindow.nextIgnoredDateAction.setEnabled(True)
            else:
                self.mainwindow.deIgnoreAllAction.setEnabled(False)
                self.mainwindow.nextIgnoredDateAction.setEnabled(False)

