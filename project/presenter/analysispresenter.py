# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


#import os
#import string
#import time
from PySide2 import QtCore, QtGui, QtWidgets
#from presenter.coloringcontainer import ColoringContainer
#import presenter.textstuff as txt
#from presenter.filtercontainer import Filter
from view.myanalysisdialog import MyAnalysisDialog
#from presenter.eventfilter import EventBlocker




class AnalysisPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        super(AnalysisPresenter, self).__init__()
        self.model = model
        self.view = view
        self.presenter = presenter



    def analyze(self):
        #print('ANALYZING!!!!')
        self.presenter.message('This is still to be implemented, if I can find the time and incentive.')


    def show_analysis_dialog(self):
        self.dialog = MyAnalysisDialog(self.view)
        if self.dialog.exec_():
            #print('From:  ' + self.dialog.from_date.toString())
            #print('Until: ' + self.dialog.until_date.toString())
            self.analyze()