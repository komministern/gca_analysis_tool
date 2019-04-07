# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore, QtGui, QtWidgets
from view.resultswindow.myresultswindow import MyResultsWindow


class MyResultsWindowPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter, app):
        super(MyResultsWindowPresenter, self).__init__()
        self.model = model
        self.view = view
        self.presenter = presenter
        self.app = app

        
    #def create_results_window(self):    # Fix from here
        
        self.resultswindow = MyResultsWindow()

        self.connect_signals()

        self.resultswindow.show()

        self.draw_temp_week()
        
    
    def connect_signals(self):
        self.resultswindow.quit.connect(self.quit)
        self.resultswindow.pushButton.pressed.connect(self.push)



    def draw_temp_week(self):
        self.resultswindow.mplCanvasWidget.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def push(self):
        print('hepp')
    
    def quit(self):
        #print('Jesus lever!')
        del self.resultswindow