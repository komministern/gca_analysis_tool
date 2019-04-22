# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


import datetime
from datetime import timedelta
import matplotlib.pyplot as plt

from PySide2 import QtCore, QtGui, QtWidgets

#from matplotlib.backends.qt_compat import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from matplotlib.widgets import RadioButtons

from view.resultswindow.myresultswindow import MyResultsWindow


class MyResultsWindowPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter, app, handle, data):
        
        super(MyResultsWindowPresenter, self).__init__()

        self.model = model
        self.view = view
        self.presenter = presenter
        self.app = app
        self.handle = handle

        self.draw_date = QtCore.QDate.fromString("20160801", "yyyyMMdd")

        self.present_date = self.draw_date

        self.data = data

        self.view.create_resultswindow(self.handle)

        self.connect_signals()

        self.x_axis_scope = None
        #self.y_axis_data = None

        self.graph_1_y_axis_content = ''
        self.graph_2_y_axis_content = ''
        self.graph_3_y_axis_content = ''

        comboboxes = [self.view.resultswindows[self.handle].comboBox_Y_Subplot_1, self.view.resultswindows[self.handle].comboBox_Y_Subplot_2, self.view.resultswindows[self.handle].comboBox_Y_Subplot_3]
        self.y_axis_items = ['', 'Temperature', 'Autotest level', 'MTI Deviation']
        for each in comboboxes:
            each.addItems(self.y_axis_items)

        self.view.resultswindows[self.handle].show()

        self.view.resultswindows[self.handle].radioButton_Rwy_1.setChecked(True)
        self.mti_deviation_parameter_rwy = 'Rwy1'

        self.view.resultswindows[self.handle].radioButton_Par.setChecked(True)
        self.mti_deviation_parameter_mode = 'PAR'

        self.view.resultswindows[self.handle].radioButton_Clear.setChecked(True) # Bugfix!
        self.mti_deviation_parameter_weather = 'Clear'

        #self.view.resultswindows[self.handle].show()


        self.view.resultswindows[self.handle].radioButton_X_Day.click() # This works! But not for the previous three buttons!!!!

        #self.view.resultswindows[self.handle].groupBox_Deviation_Parameters.setEnabled(False)


        

        #self.draw_date = QtCore.QDate.fromString("20160801", "yyyyMMdd")



        #self.dates = self.data['dates']

        self.view.resultswindows[self.handle].addToolBar(NavigationToolbar(self.view.resultswindows[self.handle].mplCanvasWidget, self.view.resultswindows[self.handle]))

        self.update_scrollbar()

    #def init_scrollbar(self):
    #    self.day = self.draw_date
    #    self.week = 
    #    self.month =
    #    self.year = 

    #    self.update_scrollbar()



        #self.draw_graphs()

    def update_scrollbar(self):
        if self.x_axis_scope == 'Day':
            self.view.resultswindows[self.handle].horizontalScrollBar.setMinimum(1)
            self.view.resultswindows[self.handle].horizontalScrollBar.setMaximum( self.present_date.daysInYear() )
            self.view.resultswindows[self.handle].horizontalScrollBar.setValue( self.present_date.dayOfYear() )

        elif self.x_axis_scope == 'Week':
            self.view.resultswindows[self.handle].horizontalScrollBar.setMinimum(1)
            last_date_of_year = QtCore.QDate(self.present_date.year(), 12, 31)
            last_week_of_year, _ = last_date_of_year.weekNumber()
            self.view.resultswindows[self.handle].horizontalScrollBar.setMaximum( last_week_of_year )
            present_week, _ = self.present_date.weekNumber()
            self.view.resultswindows[self.handle].horizontalScrollBar.setValue( present_week )

        elif self.x_axis_scope == 'Month':
            self.view.resultswindows[self.handle].horizontalScrollBar.setMinimum(1)
            self.view.resultswindows[self.handle].horizontalScrollBar.setMaximum(12)
            self.view.resultswindows[self.handle].horizontalScrollBar.setValue( self.present_date.month() )

        self.view.resultswindows[self.handle].horizontalScrollBar.setSingleStep(1)
        self.view.resultswindows[self.handle].horizontalScrollBar.setPageStep(1)

        #elif self.x_axis_scope == 'Year':
        #    year_number = 1
        #    first_year = date
        #    last_year = date
        #    number_of_years = 2



    def connect_signals(self):
        self.view.resultswindows[self.handle].quit.connect(self.quit)

        self.view.resultswindows[self.handle].draw_graph.connect(self.draw_graphs)

        self.view.resultswindows[self.handle].radioButton_X_Day.clicked.connect(self.set_x_axis_day)
        self.view.resultswindows[self.handle].radioButton_X_Week.clicked.connect(self.set_x_axis_week)
        self.view.resultswindows[self.handle].radioButton_X_Month.clicked.connect(self.set_x_axis_month)
        self.view.resultswindows[self.handle].radioButton_X_Year.clicked.connect(self.set_x_axis_year)
        self.view.resultswindows[self.handle].radioButton_X_Custom.clicked.connect(self.set_x_axis_custom)

        self.view.resultswindows[self.handle].comboBox_Y_Subplot_1.currentIndexChanged.connect(self.set_graph_1_y_axis_content)
        self.view.resultswindows[self.handle].comboBox_Y_Subplot_2.currentIndexChanged.connect(self.set_graph_2_y_axis_content)
        self.view.resultswindows[self.handle].comboBox_Y_Subplot_3.currentIndexChanged.connect(self.set_graph_3_y_axis_content)

        self.view.resultswindows[self.handle].radioButton_Rwy_1.clicked.connect(self.set_rwy_1)
        self.view.resultswindows[self.handle].radioButton_Rwy_2.clicked.connect(self.set_rwy_2)
        self.view.resultswindows[self.handle].radioButton_Rwy_3.clicked.connect(self.set_rwy_3)
        self.view.resultswindows[self.handle].radioButton_Rwy_4.clicked.connect(self.set_rwy_4)
        self.view.resultswindows[self.handle].radioButton_Rwy_5.clicked.connect(self.set_rwy_5)
        self.view.resultswindows[self.handle].radioButton_Rwy_6.clicked.connect(self.set_rwy_6)

        self.view.resultswindows[self.handle].radioButton_Par.clicked.connect(self.set_par)
        self.view.resultswindows[self.handle].radioButton_Combined.clicked.connect(self.set_combined)

        self.view.resultswindows[self.handle].radioButton_Clear.clicked.connect(self.set_clear)
        self.view.resultswindows[self.handle].radioButton_Rain.clicked.connect(self.set_rain)





    def set_rwy_1(self):
        self.mti_deviation_parameter_rwy = 'Rwy1'
        self.draw_graphs()

    def set_rwy_2(self):
        self.mti_deviation_parameter_rwy = 'Rwy2'
        self.draw_graphs()
    
    def set_rwy_3(self):
        self.mti_deviation_parameter_rwy = 'Rwy3'
        self.draw_graphs()
    
    def set_rwy_4(self):
        self.mti_deviation_parameter_rwy = 'Rwy4'
        self.draw_graphs()
    
    def set_rwy_5(self):
        self.mti_deviation_parameter_rwy = 'Rwy5'
        self.draw_graphs()
    
    def set_rwy_6(self):
        self.mti_deviation_parameter_rwy = 'Rwy6'
        self.draw_graphs()



    def set_par(self):
        self.mti_deviation_parameter_mode = 'PAR'    # Check
        self.draw_graphs()
        #print(self.mti_deviation_parameter_mode)
    
    def set_combined(self):
        self.mti_deviation_parameter_mode = 'Combined'   # Check
        self.draw_graphs()
    


    def set_clear(self):
        self.mti_deviation_parameter_weather = 'Clear'    # Check
        self.draw_graphs()
    
    def set_rain(self):
        self.mti_deviation_parameter_weather = 'Rain'   # Check
        self.draw_graphs()



    def set_x_axis_day(self):
        self.x_axis_scope = 'Day'
        self.draw_graphs()
        self.view.resultswindows[self.handle].horizontalScrollBar.setEnabled(True)
        self.update_scrollbar()

    def set_x_axis_week(self):
        self.x_axis_scope = 'Week'
        self.draw_graphs()
        self.view.resultswindows[self.handle].horizontalScrollBar.setEnabled(True)
        self.update_scrollbar()

    def set_x_axis_month(self):
        self.x_axis_scope = 'Month'
        self.draw_graphs()
        self.view.resultswindows[self.handle].horizontalScrollBar.setEnabled(True)
        self.update_scrollbar()

    def set_x_axis_year(self):
        pass

    def set_x_axis_custom(self):
        self.x_axis_scope = 'Custom'
        self.view.resultswindows[self.handle].horizontalScrollBar.setEnabled(False)



    def set_graph_1_y_axis_content(self, index):
        self.graph_1_y_axis_content = self.y_axis_items[index]
        self.draw_graphs()
        #print(self.y_axis_items[index])
    
    def set_graph_2_y_axis_content(self, index):
        self.graph_2_y_axis_content = self.y_axis_items[index]
        self.draw_graphs()
        #print(self.y_axis_items[index])
    
    def set_graph_3_y_axis_content(self, index):
        self.graph_3_y_axis_content = self.y_axis_items[index]
        self.draw_graphs()
        #print(self.y_axis_items[index])









    def draw_graphs(self):

        graph_contents = []
        for content in [self.graph_1_y_axis_content, self.graph_2_y_axis_content, self.graph_3_y_axis_content]:
            if content != '':
                graph_contents.append(content)

        self.view.resultswindows[self.handle].mplCanvasWidget.fig.clf()

        #self.view.resultswindows[self.handle].mplCanvasWidget.fig.suptitle(self.data['system_name'])#, fontsize=16)

        number_of_graphs = len(graph_contents)

        if number_of_graphs > 0:

            qdate = self.present_date
            start_qdate = self.draw_date

            self.axes = self.view.resultswindows[self.handle].mplCanvasWidget.fig.subplots(nrows=number_of_graphs, ncols=1, sharex=True)

            if number_of_graphs == 1:
                self.axes = [self.axes]

            for ax, content in zip(self.axes, graph_contents):

                if self.x_axis_scope == 'Day':
                    self.draw_day_(self.present_date, ax, content)
                elif self.x_axis_scope == 'Week':
                    first_date_in_week = self.present_date.addDays( -( self.present_date.dayOfWeek() - 1 ) )
                    self.draw_week_(first_date_in_week, ax, content)
                elif self.x_axis_scope == 'Month':
                    first_date_in_month = self.present_date.addDays( -( self.present_date.day() - 1 ) )
                    self.draw_month_(first_date_in_month, ax, content)

            if self.x_axis_scope == 'Day':
                self.axes[-1].set_xlabel(qdate.toString())
            elif self.x_axis_scope == 'Week':
                week, _ = start_qdate.weekNumber()
                self.axes[-1].set_xlabel('Week ' + str(week))
            elif self.x_axis_scope == 'Month':
                self.axes[-1].set_xlabel(start_qdate.longMonthName(start_qdate.month()))

        self.view.resultswindows[self.handle].mplCanvasWidget.fig.tight_layout()
        
        self.view.resultswindows[self.handle].mplCanvasWidget.draw()

        if self.y_axis_items[3] in graph_contents:      # MTI Deviations
            self.view.resultswindows[self.handle].groupBox_Deviation_Parameters.setEnabled(True)
        else:
            self.view.resultswindows[self.handle].groupBox_Deviation_Parameters.setEnabled(False)






    def draw_day_(self, qdate, ax, content):

        if content == self.y_axis_items[1]:  # Temperature

            self.plot_temperature_period(qdate, qdate, ax)

            ax.set_title('Temperature')
            ax.set_xlim([self.to_datetime(qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=1)])
            
            import matplotlib.dates as mdates
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

            # beautify the x-labels
            ax.legend(loc='best')

            ax.set_ylabel('°Celsius')

            for label in ax.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            ax.grid()

        elif content == self.y_axis_items[2]:  # Autotest

            self.plot_autotest_period(qdate, qdate, ax)

            ax.set_title('Autotest Level')
            ax.set_xlim([self.to_datetime(qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=1)])
            
            import matplotlib.dates as mdates
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

            # beautify the x-labels
            ax.legend(loc='best')

            ax.set_ylabel('dB')

            for label in ax.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

        elif content == self.y_axis_items[3]:  # MTI Deviation

            self.plot_mti_period(qdate, qdate, ax, self.mti_deviation_parameter_rwy, self.mti_deviation_parameter_mode, self.mti_deviation_parameter_weather)

            #ax.set_title('MTI Deviation')
            ax.set_xlim([self.to_datetime(qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=1)])
            
            import matplotlib.dates as mdates
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

            # beautify the x-labels
            #ax.legend(loc='best')

            #ax.set_ylabel('radians')

            #for label in ax.get_xticklabels():
            #    label.set_ha("right")
            #    label.set_rotation(30)


            ax.grid()


            

    def draw_week_(self, start_qdate, ax, content):

        end_qdate = start_qdate.addDays(6)

        if content == self.y_axis_items[1]:  # Temperature

            #end_qdate = start_qdate.addDays(6)

            self.plot_temperature_period(start_qdate, end_qdate, ax)

            ax.set_title('Temperature')
            ax.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=7)])

            # beautify the x-labels
            ax.legend(loc='best')
            
            ax.set_ylabel('°Celsius')

            for label in ax.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            ax.grid()
            

        elif content == self.y_axis_items[2]:  # Autotest

            #end_qdate = start_qdate.addDays(6)

            self.plot_autotest_period(start_qdate, end_qdate, ax)

            ax.set_title('Autotest Level')
            ax.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=7)])

            # beautify the x-labels
            ax.legend(loc='best')
            #week, _ = start_qdate.weekNumber()
            #ax.set_xlabel('Week ' + str(week))
            ax.set_ylabel('dB')

            for label in ax.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            ax.grid()
            
        elif content == self.y_axis_items[3]:  # MTI Deviations

            self.plot_mti_period(start_qdate, end_qdate, ax, self.mti_deviation_parameter_rwy, self.mti_deviation_parameter_mode, self.mti_deviation_parameter_weather)

            #ax.set_title('MTI Deviation')
            ax.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=7)])

            # beautify the x-labels
            #ax.legend(loc='best')
            #ax.set_ylabel('radians')

            #for label in ax.get_xticklabels():
            #    label.set_ha("right")
            #    label.set_rotation(30)

            ax.grid()


    def draw_month_(self, start_qdate, ax, content):

        if content == self.y_axis_items[1]:  # Temperature

            end_qdate = start_qdate.addDays(start_qdate.daysInMonth())

            self.plot_temperature_period(start_qdate, end_qdate, ax)

            ax.set_title('Temperature')
            ax.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=start_qdate.daysInMonth())])

            # beautify the x-labels
            ax.legend(loc='best')
            #week, _ = start_qdate.weekNumber()
            #ax.set_xlabel(start_qdate.longMonthName(start_qdate.month()))
            ax.set_ylabel('°Celsius')

            for label in ax.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            ax.grid()
            

        elif content == self.y_axis_items[2]:  # Autotest

            end_qdate = start_qdate.addDays(start_qdate.daysInMonth())

            self.plot_autotest_period(start_qdate, end_qdate, ax)

            ax.set_title('Autotest Levels')
            ax.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=start_qdate.daysInMonth())])

            # beautify the x-labels
            ax.legend(loc='best')
            #week, _ = start_qdate.weekNumber()
            #ax.set_xlabel(start_qdate.longMonthName(start_qdate.month()))
            ax.set_ylabel('dB')

            for label in ax.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            ax.grid()

        elif content == self.y_axis_items[3]:  # MTI Deviations

            end_qdate = start_qdate.addDays(start_qdate.daysInMonth())

            self.plot_mti_period(start_qdate, end_qdate, ax, self.mti_deviation_parameter_rwy, self.mti_deviation_parameter_mode, self.mti_deviation_parameter_weather)

            ax.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=start_qdate.daysInMonth())])

            ax.grid()











 






    def partition(self, datetimes):

        current_partition = []
        partitioned_datetimes = []
        previous_datetime = None

        for datetime in datetimes:

            if previous_datetime == None:

                previous_datetime = datetime

                current_partition.append(datetime)

            else:

                #from datetime import timedelta

                if datetime < previous_datetime:

                    #current_partition.append(datetime + timedelta(days=1))
                    datetime += timedelta(days=1)


                elif (datetime - previous_datetime) < timedelta(seconds=5000):

                    current_partition.append(datetime)
                
                else:

                    partitioned_datetimes.append(current_partition)

                    current_partition = []
                    
                    current_partition.append(datetime)

            previous_datetime = datetime

        if len(current_partition) > 0:

            partitioned_datetimes.append(current_partition)

        return partitioned_datetimes







    def plot_temperature_period(self, start_qdate, stop_qdate, ax):

        qdates = []
        qdate = start_qdate

        while qdate <= stop_qdate:
            qdates.append(qdate)
            qdate = qdate.addDays(1)

        datetimes = []
        az_temperatures = []
        el_temperatures = []
        shelter_temperatures = []

        for qdate in qdates:

            try:
                temp_qtimes = self.data['temperatures'][qdate].keys()

                temp_az_temperatures = [self.data['temperatures'][qdate][qtime]['az'] for qtime in temp_qtimes]
                temp_el_temperatures = [self.data['temperatures'][qdate][qtime]['el'] for qtime in temp_qtimes]
                temp_shelter_temperatures = [self.data['temperatures'][qdate][qtime]['shelter'] for qtime in temp_qtimes]
            
                temp_datetimes = [self.to_datetime(qdate, qtime) for qtime in temp_qtimes]

                datetimes.extend(temp_datetimes)

                az_temperatures.extend(temp_az_temperatures)
                el_temperatures.extend(temp_el_temperatures)
                shelter_temperatures.extend(temp_shelter_temperatures)
            except KeyError:
                pass

        partitioned_datetimes = self.partition(datetimes)
            
        new_datetimes = []
        new_az_temperatures = []
        new_el_temperatures = []
        new_shelter_temperatures = []

        i = 0
        for partition in partitioned_datetimes:

            new_datetimes.extend(partition)
            new_az_temperatures.extend(az_temperatures[i:i+len(partition)])
            new_el_temperatures.extend(el_temperatures[i:i+len(partition)])
            new_shelter_temperatures.extend(shelter_temperatures[i:i+len(partition)])

            new_datetimes.append(partition[-1] + datetime.timedelta(seconds=5000))
            new_az_temperatures.append(None)
            new_el_temperatures.append(None)
            new_shelter_temperatures.append(None)

            i += len(partition)
            
        if len(new_datetimes) > 1:

            del new_datetimes[-1]
            del new_az_temperatures[-1]
            del new_el_temperatures[-1]
            del new_shelter_temperatures[-1]

        #self.view.resultswindows[self.handle].mplCanvasWidget.fig.clf()
        
        #self.axes = self.view.resultswindows[self.handle].mplCanvasWidget.fig.add_subplot(111)

        ax.plot(new_datetimes, new_az_temperatures, 'b--', label='Az')
        ax.plot(new_datetimes, new_el_temperatures, 'r-.', label='El')
        ax.plot(new_datetimes, new_shelter_temperatures, 'g', label='Shelter')

    


    def plot_autotest_period(self, start_qdate, stop_qdate, ax):#, axes):

        qdates = []
        qdate = start_qdate

        while qdate <= stop_qdate:
            qdates.append(qdate)
            qdate = qdate.addDays(1)

        datetimes = []
        az_autotests = []
        el_autotests = []

        for qdate in qdates:

            try:
                temp_qtimes = self.data['autotest_levels'][qdate].keys()

                temp_az_autotests = [self.data['autotest_levels'][qdate][qtime]['az'] for qtime in temp_qtimes]
                temp_el_autotests = [self.data['autotest_levels'][qdate][qtime]['el'] for qtime in temp_qtimes]
            
                temp_datetimes = [self.to_datetime(qdate, qtime) for qtime in temp_qtimes]

                datetimes.extend(temp_datetimes)

                az_autotests.extend(temp_az_autotests)
                el_autotests.extend(temp_el_autotests)

            except KeyError:
                pass

        partitioned_datetimes = self.partition(datetimes)

        new_datetimes = []
        new_az_autotests = []
        new_el_autotests = []

        i = 0
        for partition in partitioned_datetimes:

            new_datetimes.extend(partition)
            new_az_autotests.extend(az_autotests[i:i+len(partition)])
            new_el_autotests.extend(el_autotests[i:i+len(partition)])

            new_datetimes.append(partition[-1] + datetime.timedelta(seconds=5000))
            new_az_autotests.append(None)
            new_el_autotests.append(None)
            
            i += len(partition)
            
        if len(new_datetimes) > 1:

            del new_datetimes[-1]
            del new_az_autotests[-1]
            del new_el_autotests[-1]
            
        #self.view.resultswindows[self.handle].mplCanvasWidget.fig.clf()
        #self.axes = self.view.resultswindows[self.handle].mplCanvasWidget.fig.add_subplot(111)

        ax.plot(new_datetimes, new_el_autotests, 'r-.', label='El')
        ax.plot(new_datetimes, new_az_autotests, 'b--', label='Az')
        





    def plot_mti_period(self, start_qdate, stop_qdate, ax, rwy, radar_mode, weather_mode):

        #print(self.data['mti_deviations'])

        #axcolor = 'lightgoldenrodyellow'
        #rax = plt.axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
        #radio = RadioButtons(rax, ('2 Hz', '4 Hz', '8 Hz'))

        #radio = RadioButtons(ax, ('rwy1', 'rwy2', 'rwy3'))

        qdates = []
        qdate = start_qdate

        while qdate <= stop_qdate:
            qdates.append(qdate)
            qdate = qdate.addDays(1)

        datetimes = []
        az_mti_deviations = []
        el_mti_deviations = []
        rng_mti_deviations = []

        for qdate in qdates:

            try:
                temp_qtimes = self.data['mti_deviations'][qdate].keys()

                temp_az_mti_deviations = [self.data['mti_deviations'][qdate][qtime]['mti_deviation']['az'] for qtime in temp_qtimes if 
                                            (self.data['mti_deviations'][qdate][qtime]['rwy'] == rwy and
                                            self.data['mti_deviations'][qdate][qtime]['radar_mode'] == radar_mode and
                                            self.data['mti_deviations'][qdate][qtime]['weather_mode'] == weather_mode)]
                
                temp_el_mti_deviations = [self.data['mti_deviations'][qdate][qtime]['mti_deviation']['el'] for qtime in temp_qtimes if 
                                            (self.data['mti_deviations'][qdate][qtime]['rwy'] == rwy and
                                            self.data['mti_deviations'][qdate][qtime]['radar_mode'] == radar_mode and
                                            self.data['mti_deviations'][qdate][qtime]['weather_mode'] == weather_mode)]

                temp_rng_mti_deviations = [self.data['mti_deviations'][qdate][qtime]['mti_deviation']['rng'] for qtime in temp_qtimes if 
                                            (self.data['mti_deviations'][qdate][qtime]['rwy'] == rwy and
                                            self.data['mti_deviations'][qdate][qtime]['radar_mode'] == radar_mode and
                                            self.data['mti_deviations'][qdate][qtime]['weather_mode'] == weather_mode)]
            
                temp_datetimes = [self.to_datetime(qdate, qtime) for qtime in temp_qtimes if 
                                            (self.data['mti_deviations'][qdate][qtime]['rwy'] == rwy and
                                            self.data['mti_deviations'][qdate][qtime]['radar_mode'] == radar_mode and
                                            self.data['mti_deviations'][qdate][qtime]['weather_mode'] == weather_mode)]

                datetimes.extend(temp_datetimes)

                az_mti_deviations.extend(temp_az_mti_deviations)
                el_mti_deviations.extend(temp_el_mti_deviations)
                rng_mti_deviations.extend(temp_rng_mti_deviations)

            except Exception as e:
                print(e)

        

        ax.scatter(datetimes, az_mti_deviations, c='blue', marker='^', label='Az')#, 'b', label='Az')
        ax.scatter(datetimes, el_mti_deviations, c='blue', marker='o', label='El')#, 'r.', label='El')

        ax2 = ax.twinx()
        ax2.set_ylabel('feet')#, color='red')  # we already handled the x-label with ax1
        
        ax2.scatter(datetimes, rng_mti_deviations, c='red', marker='s', label='Rng')

        ax2.tick_params(axis='y', labelcolor='red')

        ax.tick_params(axis='y', labelcolor='blue')

        lines, labels = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='best')


        ax.set_ylabel('radians')#, color='blue')

        ax.set_title('MTI Deviation')

        for label in ax.get_xticklabels():
            label.set_ha("right")
            label.set_rotation(30)
        #ax.plot(new_datetimes, new_rng_mti_deviations, 'g', label='Rng')

#lines, labels = ax.get_legend_handles_labels()
#lines2, labels2 = ax2.get_legend_handles_labels()
#ax2.legend(lines + lines2, labels + labels2, loc='best')

#lns = lns1+lns2+lns3
#labs = [l.get_label() for l in lns]
#ax.legend(lns, labs, loc=0)







    def to_datetime(self, qdate, qtime):
        year = qdate.year()
        month = qdate.month()
        day = qdate.day()
        hour = qtime.hour()
        minute = qtime.minute()
        second = qtime.second()
        return datetime.datetime(year, month, day, hour, minute, second)


    def quit(self):
        self.view.destroy_resultswindow(self.handle)
        print('now destroying self')
        del self
        #del self.resultswindow