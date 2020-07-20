"""
    This file is part of GCA Analysis Tool.

    Copyright (C) 2016-2020  Oscar Franzén  oscarfranzen@protonmail.com

    GCA Analysis Tool is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    GCA Analysis Tool is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with GCA Analysis Tool. If not, see <https://www.gnu.org/licenses/>.

"""

import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import matplotlib
import presenter.graphwindow.graphessentials as gess


from PySide2 import QtCore, QtGui, QtWidgets
#matplotlib.use('Qt5Agg')

#from matplotlib.backends.qt_compat import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
#from matplotlib.widgets import RadioButtons

#from presenter.resultswindow.scrollbarpresenter import ScrollBarPresenter
from view.graphwindow.graphwindow import GraphWindow
#from presenter.graphwindowstuff.scrollbarpresenter import ScrollBarPresenter
#from presenter.graphwindowstuff.graphpresenter import GraphPresenter


class MatPlotLibPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        
        super(MatPlotLibPresenter, self).__init__()

        self.model = model
        self.graphwindowpresenter = presenter
        self.graphwindow = view

        self.x_axis_scope = None

        self.graph_1_y_axis_content = ''
        self.graph_2_y_axis_content = ''
        self.graph_3_y_axis_content = ''




    def update_graphs(self):

        graph_contents = []
        for content in [self.graph_1_y_axis_content, self.graph_2_y_axis_content, self.graph_3_y_axis_content]:
            if content != '':
                graph_contents.append(content)

        self.graphwindow.mplCanvasWidget.fig.clf()

        #self.graphwindow.mplCanvasWidget.fig.suptitle(self.graphwindowpresenter.data['system_name'])#, fontsize=16)

        number_of_graphs = len(graph_contents)

        if number_of_graphs > 0:

            self.axes = self.graphwindow.mplCanvasWidget.fig.subplots(nrows=number_of_graphs, ncols=1, sharex=True)

            if number_of_graphs == 1:
                self.axes = [self.axes]

            for ax, content in zip(self.axes, graph_contents):

                if self.x_axis_scope == 'Day':
                    first_qdate = self.graphwindowpresenter.present_date
                    last_qdate = self.graphwindowpresenter.present_date

                    ax.set_xlim([gess.to_datetime(first_qdate, QtCore.QTime.fromString("0.0", "m.s")), gess.to_datetime(last_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=1) - datetime.timedelta(seconds=1)])
                    ax.xaxis.set_minor_locator(matplotlib.dates.HourLocator())

                    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))
                    for label in ax.get_xticklabels():
                        label.set_ha("right")
                        label.set_rotation(30)

                    self.axes[-1].set_xlabel(first_qdate.toString(f=QtCore.Qt.DefaultLocaleLongDate)) # FIX DIS

                    ax.grid(True, 'major')
                    

                elif self.x_axis_scope == 'Week':
                    first_qdate_in_week = self.graphwindowpresenter.present_date.addDays( -( self.graphwindowpresenter.present_date.dayOfWeek() - 1 ) )

                    first_qdate = first_qdate_in_week
                    last_qdate = first_qdate.addDays(6)

                    ax.set_xlim([gess.to_datetime(first_qdate, QtCore.QTime.fromString("0.0", "m.s")), gess.to_datetime(first_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=7) - datetime.timedelta(seconds=1)])
        
                    #set major ticks every day
                    ax.xaxis.set_major_locator(matplotlib.dates.DayLocator())

                    #set major ticks format
                    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%a, %d %b %H:%M'))

                    for label in ax.get_xticklabels():
                        label.set_ha("right")
                        label.set_rotation(30)

                    week, _ = first_qdate.weekNumber()
                    self.axes[-1].set_xlabel('Week ' + str(week) + ', ' + str(self.graphwindowpresenter.present_date.year()))

                    ax.grid(True)

                    
                elif self.x_axis_scope == 'Month':
                    first_qdate_in_month = self.graphwindowpresenter.present_date.addDays( -( self.graphwindowpresenter.present_date.day() - 1 ) )
                    
                    first_qdate = first_qdate_in_month
                    last_qdate = first_qdate.addDays(first_qdate.daysInMonth())

                    ax.set_xlim([gess.to_datetime(first_qdate, QtCore.QTime.fromString("0.0", "m.s")), gess.to_datetime(first_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=first_qdate.daysInMonth()) - datetime.timedelta(seconds=1)])
        
                    first_thursday_qdate_of_month = first_qdate.addDays( (7 - (first_qdate.dayOfWeek() - 1) + 3 ) % 7)

                    list_of_minor_ticks = []
                    qdate = first_thursday_qdate_of_month
                    while qdate.month() == first_qdate.month():
                        list_of_minor_ticks.append( gess.to_datetime(qdate, QtCore.QTime(12, 00)) )
                        qdate = qdate.addDays(7)
                    ax.set_xticks(list_of_minor_ticks, minor=True)

                    #set minor ticks format
                    ax.xaxis.set_minor_formatter(matplotlib.dates.DateFormatter('%W'))

                    ax.xaxis.set_major_locator(matplotlib.dates.WeekdayLocator( matplotlib.dates.MO))

                    #set major ticks format
                    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%a, %d %b'))
                    for label in ax.get_xticklabels():
                        label.set_ha("right")
                        label.set_rotation(30)

                    self.axes[-1].set_xlabel(QtCore.QDate.longMonthName(first_qdate.month()) + ', ' + str(first_qdate.year()))

                    ax.grid(True, 'major')


                elif self.x_axis_scope == 'Year':
                    first_qdate_in_year = QtCore.QDate(self.graphwindowpresenter.present_date.year(), 1, 1)
                    
                    first_qdate = first_qdate_in_year
                    last_qdate = first_qdate.addDays(first_qdate.daysInYear())

                    ax.set_xlim([gess.to_datetime(first_qdate, QtCore.QTime.fromString("0.0", "m.s")), gess.to_datetime(first_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=first_qdate.daysInYear()) - datetime.timedelta(seconds=1)])
        
                    #set major ticks every month
                    ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator())

                    #set major ticks format
                    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d %b'))

                    for label in ax.get_xticklabels():
                        label.set_ha("right")
                        label.set_rotation(30)

                    self.axes[-1].set_xlabel(str(first_qdate.year()))

                    ax.grid(True)


                if content == 'Temperature':
                    self.plot_temperature_period(first_qdate, last_qdate, ax)
                elif content == 'Autotest Level':
                    self.plot_autotest_period(first_qdate, last_qdate, ax)
                elif content == 'MTI Deviation':
                    self.plot_mti_period(first_qdate, last_qdate, ax)
                elif content == 'Fault Condition':
                    self.plot_fault_condition_period(first_qdate, last_qdate, ax)
                elif content == 'Heater Control':
                    self.plot_heater_control_period(first_qdate, last_qdate, ax)
                elif content == 'Radar On':
                    self.plot_radar_on_off_status_period(first_qdate, last_qdate, ax)
                elif content == 'Tilt Angle':
                    self.plot_tilt_value_period(first_qdate, last_qdate, ax)

        self.draw_graphs()

        if 'MTI Deviation' in graph_contents:
            self.graphwindow.groupBox_Deviation_Parameters.setEnabled(True)
        else:
            self.graphwindow.groupBox_Deviation_Parameters.setEnabled(False)





    def draw_graphs(self):
        self.graphwindow.mplCanvasWidget.fig.tight_layout()
        #self.graphwindow.mplCanvasWidget.draw()
        self.graphwindow.mplCanvasWidget.draw_idle()







    def plot_temperature_period(self, start_qdate, stop_qdate, ax):
        ax.set_title('Temperature')
        ax.set_ylabel('°Celsius')
        t, az_temp = self.graphwindowpresenter.graphpresenter.get_temperature_graph(start_qdate, stop_qdate, 'az')
        ax.plot(t, az_temp,'b--', label='Az')
        t, el_temp = self.graphwindowpresenter.graphpresenter.get_temperature_graph(start_qdate, stop_qdate, 'el')
        ax.plot(t, el_temp, 'r-.', label='El')
        t, shelter_temp = self.graphwindowpresenter.graphpresenter.get_temperature_graph(start_qdate, stop_qdate, 'shelter')
        ax.plot(t, shelter_temp, 'g', label='Shelter')
        ax.legend(loc='best')



    def plot_radar_on_off_status_period(self, start_qdate, stop_qdate, ax):
        ax.set_ylim([-0.2, 1.2])
        ax.set_yticks([0, 1])
        ax.set_yticklabels(['Radar Off', 'Radar On'])
        t, s = self.graphwindowpresenter.graphpresenter.get_radar_on_off_graph(start_qdate, stop_qdate)
        ax.plot(t, s, 'g-')
        ax.set_title('Radar On/Off')



    def plot_mti_period(self, start_qdate, stop_qdate, ax):#, ax2): #, rwy, radar_mode, weather_mode):
        ax.set_title('MTI Deviation')
        ax.set_ylabel('degrees')
        ax.tick_params(axis='y', labelcolor='blue')
        ax2 = ax.twinx()
        ax2.set_ylabel('feet')
        ax2.tick_params(axis='y', labelcolor='red')
        t, az_mti_deviation = self.graphwindowpresenter.graphpresenter.get_mti_deviation_graph(start_qdate, stop_qdate, self.graphwindowpresenter.mti_deviation_parameter_rwy, self.graphwindowpresenter.mti_deviation_parameter_mode, self.graphwindowpresenter.mti_deviation_parameter_weather, 'az')
        ax.scatter(t, az_mti_deviation, c='blue', marker='^', label='Az')
        t, el_mti_deviation = self.graphwindowpresenter.graphpresenter.get_mti_deviation_graph(start_qdate, stop_qdate, self.graphwindowpresenter.mti_deviation_parameter_rwy, self.graphwindowpresenter.mti_deviation_parameter_mode, self.graphwindowpresenter.mti_deviation_parameter_weather, 'el')
        ax.scatter(t, el_mti_deviation, c='blue', marker='o', label='El')
        t, rng_mti_deviation = self.graphwindowpresenter.graphpresenter.get_mti_deviation_graph(start_qdate, stop_qdate, self.graphwindowpresenter.mti_deviation_parameter_rwy, self.graphwindowpresenter.mti_deviation_parameter_mode, self.graphwindowpresenter.mti_deviation_parameter_weather, 'rng')
        ax2.scatter(t, rng_mti_deviation, c='red', marker='s', label='Rng')
        lines, labels = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines + lines2, labels + labels2, loc='best')
        #it seems that the ax2 takes precedence when drawing the x-axis, so we must add the following:
        if start_qdate.daysTo(stop_qdate) > 300:
            ax2.xaxis.set_major_locator( matplotlib.dates.MonthLocator())
            ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d %b'))
        elif start_qdate.daysTo(stop_qdate) > 25:
            ax2.xaxis.set_major_locator( matplotlib.dates.WeekdayLocator( matplotlib.dates.MO ))
            ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%a, %d %b'))
        elif start_qdate.daysTo(stop_qdate) > 1:
            ax2.xaxis.set_major_locator(matplotlib.dates.DayLocator())
            ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%a %b %d %H:%M'))
        else:
            ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))
        


    def plot_autotest_period(self, start_qdate, stop_qdate, ax):
        ax.set_title('Autotest Level')
        ax.set_ylabel('dB')
        t, az_autotests = self.graphwindowpresenter.graphpresenter.get_autotest_level_graph(start_qdate, stop_qdate, 'az')
        ax.plot(t, az_autotests, 'b--', label='Az')
        t, el_autotests = self.graphwindowpresenter.graphpresenter.get_autotest_level_graph(start_qdate, stop_qdate, 'el')
        ax.plot(t, el_autotests, 'r-.', label='El')
        ax.legend(loc='best')
        


    def plot_heater_control_period(self, start_qdate, stop_qdate, ax):
        ax.set_ylim([-2.0, 2.0])
        ax.set_yticks([-1.8, -0.8, -0.5, 0.5, 0.8, 1.8])
        ax.set_yticklabels(['Blower Off', 'Blower On', 'El Heater Off', 'El Heater On', 'Az Heater Off', 'Az Heater On'])
        colors = ['green', 'green', 'red', 'red', 'blue', 'blue']
        for label, color in zip(ax.get_yticklabels(), colors):
            label.set_color(color)
        t, az_heater = self.graphwindowpresenter.graphpresenter.get_heater_control_graph(start_qdate, stop_qdate, 'az')
        ax.plot(t, az_heater, 'b-', label='Az')
        t, el_heater = self.graphwindowpresenter.graphpresenter.get_heater_control_graph(start_qdate, stop_qdate, 'el')
        ax.plot(t, el_heater, 'r-', label='El')
        t, blower = self.graphwindowpresenter.graphpresenter.get_heater_control_graph(start_qdate, stop_qdate, 'blower')
        ax.plot(t, blower, 'g-', label='Blower')
        ax.set_title('Climate Control')
        ax.legend(loc='best')
        #if start_qdate == stop_qdate:
        #    print(t)
        #    print(el_heater)



    def plot_fault_condition_period(self, start_qdate, stop_qdate, ax):
        ax.set_ylim([-1.2, 1.2])
        ax.set_yticks([-1, 0, 1])
        ax.set_yticklabels(['Normal', 'Warning', 'Fault'])
        colors = ['green', 'black', 'red']
        for label, color in zip(ax.get_yticklabels(), colors):
            label.set_color(color)
        default_size = matplotlib.rcParams['lines.markersize'] ** 2
        new_size = default_size * 2
        normal_t, normal_indications = self.graphwindowpresenter.graphpresenter.get_fault_condition_graph(start_qdate, stop_qdate, 'normal')
        warning_t, warning_indications = self.graphwindowpresenter.graphpresenter.get_fault_condition_graph(start_qdate, stop_qdate, 'warning')
        failed_t, failed_indications = self.graphwindowpresenter.graphpresenter.get_fault_condition_graph(start_qdate, stop_qdate, 'failed')
        ax.scatter(failed_t, failed_indications, s=new_size, c='r')
        ax.scatter(warning_t, warning_indications, s=new_size, c='y')
        ax.scatter(normal_t, normal_indications, s=new_size, c='g')
        ax.set_title('Fault Condition')


    def plot_tilt_value_period(self, start_qdate, stop_qdate, ax):
    
        #default_size = matplotlib.rcParams['lines.markersize'] ** 2
        #new_size = default_size * 2
        from matplotlib.ticker import MaxNLocator
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        t, v = self.graphwindowpresenter.graphpresenter.get_tilt_value_graph(start_qdate, stop_qdate)
        
        ax.scatter(t, v)#, s=new_size, c='r')
        
        ax.set_title('Az Tilt Value')




    