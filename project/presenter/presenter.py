#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore, QtGui, QtWidgets
from presenter.mainwindow.mainwindowpresenter import MyMainWindowPresenter
from presenter.resultswindow.resultswindowpresenter import MyResultsWindowPresenter


class MyPresenter(QtCore.QObject):

    def __init__(self, model, view, app):
        super(MyPresenter, self).__init__()

        # Store view and model.
        self.model = model
        self.view = view
        self.app = app

        # Sub-presenters
        self.mainwindow = MyMainWindowPresenter(model, view, self, app)

        # Initializations
        self.mainwindow.menu.update_menu()

    

    def create_resultswindow(self):
        self.resultswindow = MyResultsWindowPresenter(self.model, self.view, self, self.app)
    
