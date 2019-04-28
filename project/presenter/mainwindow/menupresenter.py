#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore, QtGui, QtWidgets


class MenuPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        super(MenuPresenter, self).__init__()
        self.model = model
        self.view = view
        self.presenter = presenter

        self.view.mainwindow.noWrapAction.setCheckable(True)
        self.view.mainwindow.wrapAction.setCheckable(True)
        self.view.mainwindow.noWrapAction.setChecked(True)


    def update_menu(self):
        
        if self.presenter.mainwindow.active_site_name == u'':

            self.view.mainwindow.ignoreAction.setEnabled(False)
            self.view.mainwindow.deIgnoreAction.setEnabled(False)
            self.view.mainwindow.analysisAction.setEnabled(False)

        else:
            self.view.mainwindow.ignoreAction.setEnabled(True)
            self.view.mainwindow.analysisAction.setEnabled(True)

            if len(self.model.get_ignored_dates(self.presenter.mainwindow.active_site_name)) > 0:
                self.view.mainwindow.deIgnoreAction.setEnabled(True)
            else:
                self.view.mainwindow.deIgnoreAction.setEnabled(False)

