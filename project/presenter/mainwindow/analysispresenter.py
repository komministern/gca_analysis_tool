#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


#import os
#import string
#import time
import copy
from PySide2 import QtCore, QtGui, QtWidgets
#from presenter.coloringcontainer import ColoringContainer
#import presenter.textstuff as txt
#from presenter.filtercontainer import Filter
from view.mainwindow.localwidgets.myanalysisdialog import MyAnalysisDialog

#from view.myresultswindow import MyResultsWindow



#from presenter.eventfilter import EventBlocker


class AnalysisPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        super(AnalysisPresenter, self).__init__()
        self.model = model
        self.view = view
        self.presenter = presenter



    def analyze(self, start_date, end_date):
        active_site_name = self.presenter.mainwindow.active_site_name

        #self.model.analyze(active_site_name, start_date, end_date)

        collected_data = self.model.get_analysis(active_site_name, start_date, end_date)

        collected_data = self.model.get_analysis(active_site_name, self.model.get_first_entry_date(active_site_name), self.model.get_last_entry_date(active_site_name))

        self.presenter.create_resultswindowpresenter(collected_data)



        #self.result_window = MyResultsWindow(self.view)
        #self.result_window.show()
        #if self.form.exec_():
            #print('From:  ' + self.dialog.from_date.toString())
            #print('Until: ' + self.dialog.until_date.toString())
            #self.analyze(self.dialog.from_date, self.dialog.until_date)
        
        #self.presenter.message('This is still to be implemented, if I can find the time and incentive.')



    def show_analysis_dialog(self):
        self.dialog = MyAnalysisDialog(self.view.mainwindow)
        if self.dialog.exec_():
            #print('From:  ' + self.dialog.from_date.toString())
            #print('Until: ' + self.dialog.until_date.toString())
            self.analyze(self.dialog.from_date, self.dialog.until_date)