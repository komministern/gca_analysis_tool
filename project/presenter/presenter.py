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

        self.handlecounter = 0
        self.resultswindows = {}

        self.create_mainwindowpresenter()

        # Sub-presenters
        #self.mainwindow = MyMainWindowPresenter(model, view, self, app)
        #self.resultswindow = MyResultsWindowPresenter(model, view, self, app)

        # Initializations
        #self.mainwindow.menu.update_menu()

        # Show mainwindow
        #self.view.mainwindow.show()


    # Sub-presenters
    def create_mainwindowpresenter(self):
        self.mainwindow = MyMainWindowPresenter(self.model, self.view, self, self.app)
        self.mainwindow.menu.update_menu()
        self.view.mainwindow.show()
    
    def create_resultswindowpresenter(self, data):
        handle = self.get_new_handle()
        resultswindowpresenter = MyResultsWindowPresenter(self.model, self.view, self, self.app, handle, data)
        
        #resultswindowpresenter.set_data(data)

        self.resultswindows[handle] = resultswindowpresenter
        self.view.resultswindows[handle].show()

    def destroy_resultwindowpresenter(self, handle):
        del self.resultswindows[handle]

    def get_new_handle(self):
        new_handle = self.handlecounter
        self.handlecounter += 1
        return new_handle
