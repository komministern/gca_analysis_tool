#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore, QtGui, QtWidgets

class AnalysisPresenter(QtCore.QObject):

    def __init__(self, model, mainwindow, mainwindowpresenter):
        super(AnalysisPresenter, self).__init__()
        self.model = model
        self.mainwindow = mainwindow
        self.mainwindowpresenter = mainwindowpresenter



    def analyze(self):
        active_site_name = self.mainwindowpresenter.active_site_name

        self.mainwindowpresenter.inhibit_mouseclicks()

        collected_data = self.model.get_analysis(active_site_name, self.model.get_first_entry_date(active_site_name), self.model.get_last_entry_date(active_site_name))

        self.mainwindowpresenter.allow_mouseclicks()

        self.mainwindowpresenter.presenter.create_graphwindow_presenter(collected_data)

