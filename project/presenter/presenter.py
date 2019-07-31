#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.

from PySide2 import QtCore, QtGui, QtWidgets
from presenter.mainwindow.mainwindowpresenter import MyMainWindowPresenter
from presenter.graphwindow.graphwindowpresenter import GraphWindowPresenter

class Presenter(QtCore.QObject):

    def __init__(self, model, app):
        super(Presenter, self).__init__()

        self.model = model
        self.app = app

        self.mainwindowpresenter = None
        self.graphwindowpresenters = []

        self.create_mainwindow_presenter()

    # Sub-presenters
    def create_mainwindow_presenter(self):
        self.mainwindowpresenter = MyMainWindowPresenter(self.model, self, self.app)
    
    def create_graphwindow_presenter(self, data):
        self.graphwindowpresenters.append(GraphWindowPresenter(self.model, self, data))

    def destroy_graphwindow_presenter(self, obj):
        self.graphwindowpresenters.remove(obj)
        del obj
