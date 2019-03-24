#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
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




class MenuPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        super(MenuPresenter, self).__init__()
        self.model = model
        self.view = view
        self.presenter = presenter

        self.update_menu()

    # Menu stuff

    # Menu stuff

    def update_menu(self):
        
        if self.presenter.active_site_name == u'':

            self.view.ignoreAction.setEnabled(False)
            self.view.deIgnoreAction.setEnabled(False)

        else:
            self.view.ignoreAction.setEnabled(True)

            if len(self.model.get_ignored_dates(self.presenter.active_site_name)) > 0:
                self.view.deIgnoreAction.setEnabled(True)
            else:
                self.view.deIgnoreAction.setEnabled(False)

