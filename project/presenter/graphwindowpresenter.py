# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


#import datetime
#from datetime import timedelta
#import matplotlib.pyplot as plt
#import matplotlib

from PySide2 import QtCore, QtGui, QtWidgets
#matplotlib.use('Qt5Agg')

#from matplotlib.backends.qt_compat import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
#from matplotlib.figure import Figure
#from matplotlib.widgets import RadioButtons

#from presenter.resultswindow.scrollbarpresenter import ScrollBarPresenter
from view.graphwindow import GraphWindow
from presenter.graphwindowstuff.scrollbarpresenter import ScrollBarPresenter
from presenter.graphwindowstuff.matplotlibpresenter import MatPlotLibPresenter


class GraphWindowPresenter(QtCore.QObject):

    def __init__(self, model, presenter, data):
        
        super(GraphWindowPresenter, self).__init__()

        self.model = model
        self.toppresenter = presenter
        self.graphwindow = GraphWindow( parent=self.toppresenter.view.mainwindow )
        #self.graphwindow.setWindowState(self.graphwindow.windowState() ^ QtCore.Qt.WindowMaximized)
        self.graphwindow.resize( self.toppresenter.view.mainwindow.size() )
        self.graphwindow.setWindowTitle(data['system_name'])

        self.data = data

        #print(data['faults'])

        # Sub presenters
        self.scrollbarpresenter = ScrollBarPresenter(self.model, self.graphwindow, self)
        self.mplpresenter = MatPlotLibPresenter(self.model, self.graphwindow, self)


        # Initialize stuff
        self.draw_date = QtCore.QDate.fromString("20160801", "yyyyMMdd")

        self.present_date = self.draw_date

        comboboxes = [self.graphwindow.comboBox_Y_Subplot_1, self.graphwindow.comboBox_Y_Subplot_2, self.graphwindow.comboBox_Y_Subplot_3]
        self.mplpresenter.y_axis_items = ['', 'Temperature', 'Autotest Level', 'MTI Deviation', 'Fault Condition']
        for each in comboboxes:
            each.addItems(self.mplpresenter.y_axis_items)

        self.graphwindow.radioButton_Rwy_1.setChecked(True)
        self.set_rwy_1()
        #self.mti_deviation_parameter_rwy = 'Rwy1'

        self.graphwindow.radioButton_Par.setChecked(True)
        self.set_par()
        #self.mti_deviation_parameter_mode = 'PAR'

        self.graphwindow.radioButton_Clear.setChecked(True)
        self.set_clear()
        #self.mti_deviation_parameter_weather = 'Clear'

        self.graphwindow.radioButton_X_Day.setChecked(True)
        self.set_x_axis_day()
        #self.x_axis_scope = 'Day'
        self.graphwindow.groupBox_Deviation_Parameters.setEnabled(False)

        self.graphwindow.addToolBar(NavigationToolbar(self.graphwindow.mplCanvasWidget, self.graphwindow))

        self.scrollbarpresenter.update_scrollbar()

        self.connect_signals()

        self.graphwindow.show()


    @property
    def x_axis_scope(self):
        return self.mplpresenter.x_axis_scope

    @x_axis_scope.setter
    def x_axis_scope(self, scope):
        self.mplpresenter.x_axis_scope = scope



    def connect_signals(self):
        self.graphwindow.quit.connect(self.quit)

        self.graphwindow.draw_graph.connect(self.mplpresenter.draw_graphs)

        self.graphwindow.radioButton_X_Day.clicked.connect(self.set_x_axis_day)
        self.graphwindow.radioButton_X_Week.clicked.connect(self.set_x_axis_week)
        self.graphwindow.radioButton_X_Month.clicked.connect(self.set_x_axis_month)
        self.graphwindow.radioButton_X_Year.clicked.connect(self.set_x_axis_year)
        #self.graphwindow.radioButton_X_Custom.clicked.connect(self.set_x_axis_custom)

        self.graphwindow.comboBox_Y_Subplot_1.currentIndexChanged.connect(self.set_graph_1_y_axis_content)
        self.graphwindow.comboBox_Y_Subplot_2.currentIndexChanged.connect(self.set_graph_2_y_axis_content)
        self.graphwindow.comboBox_Y_Subplot_3.currentIndexChanged.connect(self.set_graph_3_y_axis_content)

        self.graphwindow.radioButton_Rwy_1.clicked.connect(self.set_rwy_1)
        self.graphwindow.radioButton_Rwy_2.clicked.connect(self.set_rwy_2)
        self.graphwindow.radioButton_Rwy_3.clicked.connect(self.set_rwy_3)
        self.graphwindow.radioButton_Rwy_4.clicked.connect(self.set_rwy_4)
        self.graphwindow.radioButton_Rwy_5.clicked.connect(self.set_rwy_5)
        self.graphwindow.radioButton_Rwy_6.clicked.connect(self.set_rwy_6)

        self.graphwindow.radioButton_Par.clicked.connect(self.set_par)
        self.graphwindow.radioButton_Combined.clicked.connect(self.set_combined)

        self.graphwindow.radioButton_Clear.clicked.connect(self.set_clear)
        self.graphwindow.radioButton_Rain.clicked.connect(self.set_rain)

        self.graphwindow.horizontalScrollBar.valueChanged.connect(self.scrollbarpresenter.new_slider_value)
        self.graphwindow.horizontalScrollBar.sliderPressed.connect(self.scrollbarpresenter.slider_pressed)
        self.graphwindow.horizontalScrollBar.sliderReleased.connect(self.scrollbarpresenter.slider_released)
        self.graphwindow.horizontalScrollBar.sliderMoved.connect(self.scrollbarpresenter.slider_moved)




    def set_rwy_1(self):
        self.mplpresenter.mti_deviation_parameter_rwy = 'Rwy1'
        self.mplpresenter.draw_graphs()

    def set_rwy_2(self):
        self.mplpresenter.mti_deviation_parameter_rwy = 'Rwy2'
        self.mplpresenter.draw_graphs()
    
    def set_rwy_3(self):
        self.mplpresenter.mti_deviation_parameter_rwy = 'Rwy3'
        self.mplpresenter.draw_graphs()
    
    def set_rwy_4(self):
        self.mplpresenter.mti_deviation_parameter_rwy = 'Rwy4'
        self.mplpresenter.draw_graphs()
    
    def set_rwy_5(self):
        self.mplpresenter.mti_deviation_parameter_rwy = 'Rwy5'
        self.mplpresenter.draw_graphs()
    
    def set_rwy_6(self):
        self.mplpresenter.mti_deviation_parameter_rwy = 'Rwy6'
        self.mplpresenter.draw_graphs()



    def set_par(self):
        self.mplpresenter.mti_deviation_parameter_mode = 'PAR'    # Check
        self.mplpresenter.draw_graphs()

    def set_combined(self):
        self.mplpresenter.mti_deviation_parameter_mode = 'Combined'   # Check
        self.mplpresenter.draw_graphs()
    


    def set_clear(self):
        self.mplpresenter.mti_deviation_parameter_weather = 'Clear'    # Check
        self.mplpresenter.draw_graphs()
    
    def set_rain(self):
        self.mplpresenter.mti_deviation_parameter_weather = 'Rain'   # Check
        self.mplpresenter.draw_graphs()



    def set_x_axis_day(self):
        self.scrollbarpresenter.ignore_new_value_due_to_x_axis_scope_change = True
        self.mplpresenter.x_axis_scope = 'Day'
        self.mplpresenter.draw_graphs()
        self.graphwindow.horizontalScrollBar.setEnabled(True)
        self.scrollbarpresenter.update_scrollbar()
        self.scrollbarpresenter.ignore_new_value_due_to_x_axis_scope_change = False

    def set_x_axis_week(self):
        self.scrollbarpresenter.ignore_new_value_due_to_x_axis_scope_change = True
        self.mplpresenter.x_axis_scope = 'Week'
        self.mplpresenter.draw_graphs()
        self.graphwindow.horizontalScrollBar.setEnabled(True)
        self.scrollbarpresenter.update_scrollbar()
        self.scrollbarpresenter.ignore_new_value_due_to_x_axis_scope_change = False

    def set_x_axis_month(self):
        self.scrollbarpresenter.ignore_new_value_due_to_x_axis_scope_change = True
        self.mplpresenter.x_axis_scope = 'Month'
        self.mplpresenter.draw_graphs()
        self.graphwindow.horizontalScrollBar.setEnabled(True)
        self.scrollbarpresenter.update_scrollbar()
        self.scrollbarpresenter.ignore_new_value_due_to_x_axis_scope_change = False

    def set_x_axis_year(self):
        self.scrollbarpresenter.ignore_new_value_due_to_x_axis_scope_change = True
        self.mplpresenter.x_axis_scope = 'Year'
        self.mplpresenter.draw_graphs()
        self.graphwindow.horizontalScrollBar.setEnabled(True)
        self.scrollbarpresenter.update_scrollbar()
        self.scrollbarpresenter.ignore_new_value_due_to_x_axis_scope_change = False





    def set_graph_1_y_axis_content(self, index):
        self.mplpresenter.graph_1_y_axis_content = self.mplpresenter.y_axis_items[index]
        self.mplpresenter.draw_graphs()
        #print(self.y_axis_items[index])
    
    def set_graph_2_y_axis_content(self, index):
        self.mplpresenter.graph_2_y_axis_content = self.mplpresenter.y_axis_items[index]
        self.mplpresenter.draw_graphs()
        #print(self.y_axis_items[index])
    
    def set_graph_3_y_axis_content(self, index):
        self.mplpresenter.graph_3_y_axis_content = self.mplpresenter.y_axis_items[index]
        self.mplpresenter.draw_graphs()
        #print(self.y_axis_items[index])


    def quit(self):
        self.toppresenter.destroy_graphwindow_presenter(self)
