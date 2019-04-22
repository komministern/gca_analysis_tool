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

from view.resultswindow.myresultswindow import MyResultsWindow


class MyResultsWindowPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter, app, handle, data):
        
        super(MyResultsWindowPresenter, self).__init__()

        self.model = model
        self.view = view
        self.presenter = presenter
        self.app = app
        self.handle = handle

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

        self.view.resultswindows[self.handle].radioButton_X_Day.click()





        self.draw_date = QtCore.QDate.fromString("20160801", "yyyyMMdd")



        self.dates = self.data['dates']

        self.view.resultswindows[self.handle].addToolBar(NavigationToolbar(self.view.resultswindows[self.handle].mplCanvasWidget, self.view.resultswindows[self.handle]))





    def connect_signals(self):
        self.view.resultswindows[self.handle].quit.connect(self.quit)
        self.view.resultswindows[self.handle].radioButton_X_Day.pressed.connect(self.set_x_axis_day)
        self.view.resultswindows[self.handle].radioButton_X_Week.pressed.connect(self.set_x_axis_week)
        self.view.resultswindows[self.handle].radioButton_X_Month.pressed.connect(self.set_x_axis_month)
        self.view.resultswindows[self.handle].radioButton_X_Custom.pressed.connect(self.set_x_axis_custom)

        self.view.resultswindows[self.handle].comboBox_Y_Subplot_1.currentIndexChanged.connect(self.set_graph_1_y_axis_content)
        self.view.resultswindows[self.handle].comboBox_Y_Subplot_2.currentIndexChanged.connect(self.set_graph_2_y_axis_content)
        self.view.resultswindows[self.handle].comboBox_Y_Subplot_3.currentIndexChanged.connect(self.set_graph_3_y_axis_content)


        #self.view.resultswindows[self.handle].radioButton_Temp.pressed.connect(self.set_y_axis_temp)
        #self.view.resultswindows[self.handle].radioButton_Autotest.pressed.connect(self.set_y_axis_autotest)
        #self.view.resultswindows[self.handle].radioButton_MTI.pressed.connect(self.set_y_axis_mti)



    


    #def draw_init_graph(self):
    #    self.view.resultswindows[self.handle].mplCanvasWidget.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')


    def set_x_axis_day(self):
        self.x_axis_scope = 'Day'
        self.draw_graphs()
        self.view.resultswindows[self.handle].horizontalScrollBar.setEnabled(True)

    def set_x_axis_week(self):
        self.x_axis_scope = 'Week'
        self.draw_graphs()
        self.view.resultswindows[self.handle].horizontalScrollBar.setEnabled(True)

    def set_x_axis_month(self):
        self.x_axis_scope = 'Month'
        self.draw_graphs()
        self.view.resultswindows[self.handle].horizontalScrollBar.setEnabled(True)

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

            qdate = self.draw_date
            start_qdate = self.draw_date

            self.axes = self.view.resultswindows[self.handle].mplCanvasWidget.fig.subplots(nrows=number_of_graphs, ncols=1, sharex=True)

            if number_of_graphs == 1:
                self.axes = [self.axes]

            for ax, content in zip(self.axes, graph_contents):

                if self.x_axis_scope == 'Day':
                    self.draw_day_(qdate, ax, content)
                elif self.x_axis_scope == 'Week':
                    self.draw_week_(qdate, ax, content)
                elif self.x_axis_scope == 'Month':
                    self.draw_month_(qdate, ax, content)

            if self.x_axis_scope == 'Day':
                self.axes[-1].set_xlabel(qdate.toString())
            elif self.x_axis_scope == 'Week':
                week, _ = start_qdate.weekNumber()
                self.axes[-1].set_xlabel('Week ' + str(week))
            elif self.x_axis_scope == 'Month':
                self.axes[-1].set_xlabel(start_qdate.longMonthName(start_qdate.month()))

        self.view.resultswindows[self.handle].mplCanvasWidget.fig.tight_layout()
        
        self.view.resultswindows[self.handle].mplCanvasWidget.draw()




    def draw_day_(self, qdate, ax, content):

        if content == self.y_axis_items[1]:  # Temperature

            self.plot_temperature_period(qdate, qdate, ax)

            ax.set_title('Temperatures')
            ax.set_xlim([self.to_datetime(qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=1)])
            
            import matplotlib.dates as mdates
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

            # beautify the x-labels
            ax.legend(loc='best')

            ax.set_ylabel('Degrees Celsius')

            for label in ax.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            ax.grid()

        elif content == self.y_axis_items[2]:  # Autotest

            self.plot_autotest_period(qdate, qdate, ax)

            ax.set_title('Autotest Levels')
            ax.set_xlim([self.to_datetime(qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=1)])
            
            import matplotlib.dates as mdates
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

            # beautify the x-labels
            ax.legend(loc='best')

            ax.set_ylabel('dB')

            for label in ax.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            ax.grid()


            

    def draw_week_(self, start_qdate, ax, content):

        if content == self.y_axis_items[1]:  # Temperature

            end_qdate = start_qdate.addDays(6)

            self.plot_temperature_period(start_qdate, end_qdate, ax)

            ax.set_title('Temperatures')
            ax.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=7)])

            # beautify the x-labels
            ax.legend(loc='best')
            #week, _ = start_qdate.weekNumber()
            #ax.set_xlabel('Week ' + str(week))
            ax.set_ylabel('Degrees Celsius')

            for label in ax.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            ax.grid()
            

        elif content == self.y_axis_items[2]:  # Autotest

            end_qdate = start_qdate.addDays(6)

            self.plot_autotest_period(start_qdate, end_qdate, ax)

            ax.set_title('Autotest Levels')
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
            



    def draw_month_(self, start_qdate, ax, content):

        if content == self.y_axis_items[1]:  # Temperature

            end_qdate = start_qdate.addDays(start_qdate.daysInMonth())

            self.plot_temperature_period(start_qdate, end_qdate, ax)

            ax.set_title('Temperatures')
            ax.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=start_qdate.daysInMonth())])

            # beautify the x-labels
            ax.legend(loc='best')
            #week, _ = start_qdate.weekNumber()
            #ax.set_xlabel(start_qdate.longMonthName(start_qdate.month()))
            ax.set_ylabel('Degrees Celsius')

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
















    def set_y_axis_temp(self):
        self.y_axis_data = 'temp'
        self.draw_plot()


    def set_y_axis_autotest(self):
        self.y_axis_data = 'autotest'
        self.draw_plot()


    def set_y_axis_mti(self):
        self.y_axis_data = 'mti'
        self.draw_plot()

    
    def draw_plot(self):
        if self.x_axis_scope and self.y_axis_data:
            if self.x_axis_scope == 'day':
                self.draw_day(self.draw_date)
            elif self.x_axis_scope == 'week':
                self.draw_week(self.draw_date)
            elif self.x_axis_scope == 'month':
                self.draw_month(self.draw_date)



 






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
        





    def plot_mti_period(self, start_qdate, stop_qdate):#, axes):

        print(self.data['mti_deviations'])

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
                temp_qtimes = self.data['temperatures'][qdate].keys()

                temp_az_mti_deviations = [self.data['mti_deviations'][qdate][qtime]['az'] for qtime in temp_qtimes]
                temp_el_mti_deviations = [self.data['mti_deviations'][qdate][qtime]['el'] for qtime in temp_qtimes]
                temp_rng_mti_deviations = [self.data['mti_deviations'][qdate][qtime]['rng'] for qtime in temp_qtimes]
            
                temp_datetimes = [self.to_datetime(qdate, qtime) for qtime in temp_qtimes]

                datetimes.extend(temp_datetimes)

                az_mti_deviations.extend(temp_az_mti_deviations)
                el_mti_deviations.extend(temp_el_mti_deviations)
                rng_mti_deviations.extend(temp_rng_mti_deviations)
            except KeyError:
                pass

        partitioned_datetimes = self.partition(datetimes)
            
        new_datetimes = []
        new_az_mti_deviations = []
        new_el_mti_deviations = []
        new_rng_mti_deviations = []

        i = 0
        for partition in partitioned_datetimes:

            new_datetimes.extend(partition)
            new_az_mti_deviations.extend(az_mti_deviations[i:i+len(partition)])
            new_el_mti_deviations.extend(el_mti_deviations[i:i+len(partition)])
            new_rng_mti_deviations.extend(rng_mti_deviations[i:i+len(partition)])

            new_datetimes.append(partition[-1] + datetime.timedelta(seconds=5000))
            new_az_mti_deviations.append(None)
            new_el_mti_deviations.append(None)
            new_rng_mti_deviations.append(None)

            i += len(partition)
            
        if len(new_datetimes) > 1:

            del new_datetimes[-1]
            del new_az_mti_deviations[-1]
            del new_el_mti_deviations[-1]
            del new_rng_mti_deviations[-1]

        self.view.resultswindows[self.handle].mplCanvasWidget.fig.clf()
        self.axes = self.view.resultswindows[self.handle].mplCanvasWidget.fig.add_subplot(111)

        self.axes.plot(new_datetimes, new_az_mti_deviations, 'b--', label='Az')
        self.axes.plot(new_datetimes, new_el_mti_deviations, 'r-.', label='El')
        self.axes.plot(new_datetimes, new_rng_mti_deviations, 'g', label='Rng')










    def draw_day(self, start_qdate):

        if self.y_axis_data == 'temp':

            self.plot_temperature_period(start_qdate, start_qdate)

            self.axes.set_title(self.data['system_name'] + ' - Temperatures')
            self.axes.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=1)])
            
            import matplotlib.dates as mdates
            self.axes.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

            # beautify the x-labels
            self.axes.legend(loc='best')

            self.axes.set_xlabel(start_qdate.toString())
            self.axes.set_ylabel('Degrees Celsius')

            for label in self.axes.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            self.axes.grid()
            self.view.resultswindows[self.handle].mplCanvasWidget.fig.tight_layout()
            self.view.resultswindows[self.handle].mplCanvasWidget.draw()

        
        elif self.y_axis_data == 'autotest':

            self.plot_autotest_period(start_qdate, start_qdate)

            self.axes.set_title(self.data['system_name'] + ' - Autotest Levels')
            self.axes.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=1)])
            
            import matplotlib.dates as mdates
            self.axes.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

            # beautify the x-labels
            self.axes.legend(loc='best')

            self.axes.set_xlabel(start_qdate.toString())
            self.axes.set_ylabel('dB')

            for label in self.axes.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            self.axes.grid()
            self.view.resultswindows[self.handle].mplCanvasWidget.fig.tight_layout()
            self.view.resultswindows[self.handle].mplCanvasWidget.draw()







    def draw_week(self, start_qdate):

        if self.y_axis_data == 'temp':

            end_qdate = start_qdate.addDays(6)

            self.plot_temperature_period(start_qdate, end_qdate)

            self.axes.set_title(self.data['system_name'] + ' - Temperatures')
            self.axes.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=7)])

            # beautify the x-labels
            self.axes.legend(loc='best')
            week, _ = start_qdate.weekNumber()
            self.axes.set_xlabel('Week ' + str(week))
            self.axes.set_ylabel('Degrees Celsius')

            for label in self.axes.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            self.axes.grid()
            self.view.resultswindows[self.handle].mplCanvasWidget.fig.tight_layout()
            self.view.resultswindows[self.handle].mplCanvasWidget.draw()

        elif self.y_axis_data == 'autotest':

            end_qdate = start_qdate.addDays(6)

            self.plot_autotest_period(start_qdate, end_qdate)

            self.axes.set_title(self.data['system_name'] + ' - Autotest Levels')
            self.axes.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=7)])

            # beautify the x-labels
            self.axes.legend(loc='best')
            week, _ = start_qdate.weekNumber()
            self.axes.set_xlabel('Week ' + str(week))
            self.axes.set_ylabel('dB')

            for label in self.axes.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            self.axes.grid()
            self.view.resultswindows[self.handle].mplCanvasWidget.fig.tight_layout()
            self.view.resultswindows[self.handle].mplCanvasWidget.draw()
        
        elif self.y_axis_data == 'mti':

            end_qdate = start_qdate.addDays(6)

            self.plot_mti_period(start_qdate, end_qdate)

            self.axes.set_title(self.data['system_name'] + ' - MTI Deviations')
            self.axes.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=7)])

            # beautify the x-labels
            self.axes.legend(loc='best')
            week, _ = start_qdate.weekNumber()
            self.axes.set_xlabel('Week ' + str(week))
            self.axes.set_ylabel('?')

            for label in self.axes.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            self.axes.grid()
            self.view.resultswindows[self.handle].mplCanvasWidget.fig.tight_layout()
            self.view.resultswindows[self.handle].mplCanvasWidget.draw()









    def draw_month(self, start_qdate):

        if self.y_axis_data == 'temp':

            end_qdate = start_qdate.addDays(start_qdate.daysInMonth())

            self.plot_temperature_period(start_qdate, end_qdate)

            self.axes.set_title(self.data['system_name'] + ' - Temperatures')
            self.axes.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=start_qdate.daysInMonth())])

            # beautify the x-labels
            self.axes.legend(loc='best')
            #week, _ = start_qdate.weekNumber()
            self.axes.set_xlabel(start_qdate.longMonthName(start_qdate.month()))
            self.axes.set_ylabel('Degrees Celsius')

            for label in self.axes.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            self.axes.grid()
            self.view.resultswindows[self.handle].mplCanvasWidget.fig.tight_layout()
            self.view.resultswindows[self.handle].mplCanvasWidget.draw()

        elif self.y_axis_data == 'autotest':

            end_qdate = start_qdate.addDays(start_qdate.daysInMonth())

            self.plot_autotest_period(start_qdate, end_qdate)

            self.axes.set_title(self.data['system_name'] + ' - Autotest Levels')
            self.axes.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=start_qdate.daysInMonth())])

            # beautify the x-labels
            self.axes.legend(loc='best')
            #week, _ = start_qdate.weekNumber()
            self.axes.set_xlabel(start_qdate.longMonthName(start_qdate.month()))
            self.axes.set_ylabel('dB')

            for label in self.axes.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

            self.axes.grid()
            self.view.resultswindows[self.handle].mplCanvasWidget.fig.tight_layout()
            self.view.resultswindows[self.handle].mplCanvasWidget.draw()






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