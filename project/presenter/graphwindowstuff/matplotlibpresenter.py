import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import matplotlib


from PySide2 import QtCore, QtGui, QtWidgets
#matplotlib.use('Qt5Agg')

#from matplotlib.backends.qt_compat import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
#from matplotlib.widgets import RadioButtons

#from presenter.resultswindow.scrollbarpresenter import ScrollBarPresenter
from view.graphwindow import GraphWindow
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




    def draw_graphs(self):

        graph_contents = []
        for content in [self.graph_1_y_axis_content, self.graph_2_y_axis_content, self.graph_3_y_axis_content]:
            if content != '':
                graph_contents.append(content)

        self.graphwindow.mplCanvasWidget.fig.clf()

        #self.graphwindow.mplCanvasWidget.fig.suptitle(self.graphwindowpresenter.data['system_name'])#, fontsize=16)

        number_of_graphs = len(graph_contents)

        if number_of_graphs > 0:

            #qdate = self.graphwindowpresenter.present_date
            #start_qdate = self.graphwindowpresenter.draw_date   # ------------------ ?????????????????

            self.axes = self.graphwindow.mplCanvasWidget.fig.subplots(nrows=number_of_graphs, ncols=1, sharex=True)

            if number_of_graphs == 1:
                self.axes = [self.axes]

            for ax, content in zip(self.axes, graph_contents):

                if self.x_axis_scope == 'Day':
                    self.draw_day_(self.graphwindowpresenter.present_date, ax, content)
                elif self.x_axis_scope == 'Week':
                    first_date_in_week = self.graphwindowpresenter.present_date.addDays( -( self.graphwindowpresenter.present_date.dayOfWeek() - 1 ) )
                    self.draw_week_(first_date_in_week, ax, content)
                elif self.x_axis_scope == 'Month':
                    first_date_in_month = self.graphwindowpresenter.present_date.addDays( -( self.graphwindowpresenter.present_date.day() - 1 ) )
                    self.draw_month_(first_date_in_month, ax, content)
                elif self.x_axis_scope == 'Year':
                    first_date_in_year = QtCore.QDate(self.graphwindowpresenter.present_date.year(), 1, 1)
                    self.draw_year_(first_date_in_year, ax, content)


        self.graphwindow.mplCanvasWidget.fig.tight_layout()
        self.graphwindow.mplCanvasWidget.draw()

        if self.y_axis_items[3] in graph_contents:      # MTI Deviations
            self.graphwindow.groupBox_Deviation_Parameters.setEnabled(True)
        else:
            self.graphwindow.groupBox_Deviation_Parameters.setEnabled(False)



    def draw_day_(self, qdate, ax, content):

        #print(self.graphwindowpresenter.data['fault_condition'][QtCore.QDate(2016, 8, 2)])

        ax.set_xlim([self.to_datetime(qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=1) - datetime.timedelta(seconds=1)])
        ax.xaxis.set_minor_locator(matplotlib.dates.HourLocator())

        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))
        for label in ax.get_xticklabels():
                label.set_ha("right")
                label.set_rotation(30)

        self.axes[-1].set_xlabel(qdate.toString(f=QtCore.Qt.DefaultLocaleLongDate)) # FIX DIS

        ax.grid(True, 'major')

        if content == self.y_axis_items[1]:  # Temperature

            self.plot_temperature_period(qdate, qdate, ax)

            ax.set_title('Temperature')
            ax.set_ylabel('°Celsius')
            ax.legend(loc='best')
            
        elif content == self.y_axis_items[2]:  # Autotest

            self.plot_autotest_period(qdate, qdate, ax)

            ax.set_title('Autotest Level')
            ax.set_ylabel('dB')
            ax.legend(loc='best')

        elif content == self.y_axis_items[3]:  # MTI Deviation

            ax.set_title('MTI Deviation')
            ax.set_ylabel('degrees')
            
            ax.tick_params(axis='y', labelcolor='blue')

            ax2 = ax.twinx()
            ax2.set_ylabel('feet')
            ax2.tick_params(axis='y', labelcolor='red')

            self.plot_mti_period(qdate, qdate, ax, ax2, self.mti_deviation_parameter_rwy, self.mti_deviation_parameter_mode, self.mti_deviation_parameter_weather)

            lines, labels = ax.get_legend_handles_labels()
            lines2, labels2 = ax2.get_legend_handles_labels()
            ax.legend(lines + lines2, labels + labels2, loc='best')

            #it seems that the ax2 takes precedence when drawing the x-axis, so we must add the following:
            ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))

        elif content == self.y_axis_items[4]:  # Fault Condition

            ax.set_ylim([-1.2, 1.2])
            ax.set_yticks([-1, 0, 1])
            ax.set_yticklabels(['Normal', 'Warning', 'Fault'])

            colors = ['green', 'black', 'red']
            for label, color in zip(ax.get_yticklabels(), colors):
                label.set_color(color)

            self.plot_fault_condition_period(qdate, qdate, ax)

            ax.set_title('Fault Condition')
            #ax.set_ylabel('dB')
            #ax.legend(loc='best')




    def draw_week_(self, start_qdate, ax, content):

        end_qdate = start_qdate.addDays(6)

        ax.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=7) - datetime.timedelta(seconds=1)])
        
        #set major ticks every day
        ax.xaxis.set_major_locator(matplotlib.dates.DayLocator())

        #set major ticks format
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%a, %d %b %H:%M'))

        for label in ax.get_xticklabels():
            label.set_ha("right")
            label.set_rotation(30)

        week, _ = start_qdate.weekNumber()
        self.axes[-1].set_xlabel('Week ' + str(week) + ', ' + str(self.graphwindowpresenter.present_date.year()))

        ax.grid(True)

        if content == self.y_axis_items[1]:  # Temperature

            self.plot_temperature_period(start_qdate, end_qdate, ax)

            ax.set_title('Temperature')
            ax.set_ylabel('°Celsius')
            
            ax.legend(loc='best')
            
        elif content == self.y_axis_items[2]:  # Autotest

            self.plot_autotest_period(start_qdate, end_qdate, ax)

            ax.set_title('Autotest Level')
            ax.set_ylabel('dB')
            
            ax.legend(loc='best')
            
        elif content == self.y_axis_items[3]:  # MTI Deviations

            ax.set_title('MTI Deviation')
            ax.set_ylabel('degrees')
            
            ax.tick_params(axis='y', labelcolor='blue')

            ax2 = ax.twinx()
            ax2.set_ylabel('feet')
            ax2.tick_params(axis='y', labelcolor='red')

            self.plot_mti_period(start_qdate, end_qdate, ax, ax2, self.mti_deviation_parameter_rwy, self.mti_deviation_parameter_mode, self.mti_deviation_parameter_weather)

            lines, labels = ax.get_legend_handles_labels()
            lines2, labels2 = ax2.get_legend_handles_labels()
            ax.legend(lines + lines2, labels + labels2, loc='best')

            #it seems that the ax2 takes precedence when drawing the x-axis, so we must add the following:
            #set ticks every week
            ax2.xaxis.set_major_locator(matplotlib.dates.DayLocator())
            #set major ticks format
            ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%a %b %d %H:%M'))

        elif content == self.y_axis_items[4]:  # Fault Condition

            ax.set_ylim([-1.2, 1.2])
            ax.set_yticks([-1, 0, 1])
            ax.set_yticklabels(['Normal', 'Warning', 'Fault'])

            colors = ['green', 'black', 'red']
            for label, color in zip(ax.get_yticklabels(), colors):
                label.set_color(color)

            self.plot_fault_condition_period(start_qdate, end_qdate, ax)

            ax.set_title('Fault Condition')



    def draw_month_(self, start_qdate, ax, content):

        end_qdate = start_qdate.addDays( start_qdate.daysInMonth() )

        ax.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=start_qdate.daysInMonth()) - datetime.timedelta(seconds=1)])
        
        first_thursday_qdate_of_month = start_qdate.addDays( (7 - (start_qdate.dayOfWeek() - 1) + 3 ) % 7)

        list_of_minor_ticks = []
        qdate = first_thursday_qdate_of_month
        while qdate.month() == start_qdate.month():
            list_of_minor_ticks.append( self.to_datetime(qdate, QtCore.QTime(12, 00)) )
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

        self.axes[-1].set_xlabel(QtCore.QDate.longMonthName(start_qdate.month()) + ', ' + str(start_qdate.year()))

        ax.grid(True, 'major')
        


        if content == self.y_axis_items[1]:  # Temperature

            self.plot_temperature_period(start_qdate, end_qdate, ax)

            ax.set_title('Temperature')
            ax.set_ylabel('°Celsius')
            
            ax.legend(loc='best')
            

        elif content == self.y_axis_items[2]:  # Autotest

            self.plot_autotest_period(start_qdate, end_qdate, ax)

            ax.set_title('Autotest Level')
            ax.set_ylabel('dB')
            
            ax.legend(loc='best')
            

        elif content == self.y_axis_items[3]:  # MTI Deviations

            ax.set_title('MTI Deviation')
            ax.set_ylabel('degrees')

            ax.tick_params(axis='y', labelcolor='blue')

            ax2 = ax.twinx()
            ax2.set_ylabel('feet')
            ax2.tick_params(axis='y', labelcolor='red')

            self.plot_mti_period(start_qdate, end_qdate, ax, ax2, self.mti_deviation_parameter_rwy, self.mti_deviation_parameter_mode, self.mti_deviation_parameter_weather)

            lines, labels = ax.get_legend_handles_labels()
            lines2, labels2 = ax2.get_legend_handles_labels()
            ax.legend(lines + lines2, labels + labels2, loc='best')

            ax2.xaxis.set_major_locator( matplotlib.dates.WeekdayLocator( matplotlib.dates.MO ))
            ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%a, %d %b'))

        elif content == self.y_axis_items[4]:  # Fault Condition

            ax.set_ylim([-1.2, 1.2])
            ax.set_yticks([-1, 0, 1])
            ax.set_yticklabels(['Normal', 'Warning', 'Fault'])

            colors = ['green', 'black', 'red']
            for label, color in zip(ax.get_yticklabels(), colors):
                label.set_color(color)

            self.plot_fault_condition_period(start_qdate, end_qdate, ax)

            ax.set_title('Fault Condition')




    def draw_year_(self, start_qdate, ax, content):

        end_qdate = start_qdate.addDays(start_qdate.daysInYear())

        ax.set_xlim([self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")), self.to_datetime(start_qdate, QtCore.QTime.fromString("0.0", "m.s")) + datetime.timedelta(days=start_qdate.daysInYear()) - datetime.timedelta(seconds=1)])
        
        #set major ticks every month
        ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator())

        #set major ticks format
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d %b'))

        for label in ax.get_xticklabels():
            label.set_ha("right")
            label.set_rotation(30)

        self.axes[-1].set_xlabel(str(start_qdate.year()))

        ax.grid(True)



        if content == self.y_axis_items[1]:  # Temperature

            self.plot_temperature_period(start_qdate, end_qdate, ax)

            ax.set_title('Temperature')
            ax.set_ylabel('°Celsius')
            
            ax.legend(loc='best')
            

        elif content == self.y_axis_items[2]:  # Autotest

            self.plot_autotest_period(start_qdate, end_qdate, ax)

            ax.set_title('Autotest Levels')
            ax.set_ylabel('dB')
            
            ax.legend(loc='best')
            

        elif content == self.y_axis_items[3]:  # MTI Deviations

            ax.set_title('MTI Deviation')
            ax.set_ylabel('degrees')

            ax.tick_params(axis='y', labelcolor='blue')

            ax2 = ax.twinx()
            ax2.set_ylabel('feet')
            ax2.tick_params(axis='y', labelcolor='red')

            self.plot_mti_period(start_qdate, end_qdate, ax, ax2, self.mti_deviation_parameter_rwy, self.mti_deviation_parameter_mode, self.mti_deviation_parameter_weather)

            lines, labels = ax.get_legend_handles_labels()
            lines2, labels2 = ax2.get_legend_handles_labels()
            ax.legend(lines + lines2, labels + labels2, loc='best')

            ax2.xaxis.set_major_locator( matplotlib.dates.MonthLocator())
            ax2.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d %b'))

        elif content == self.y_axis_items[4]:  # Fault Condition

            ax.set_ylim([-1.2, 1.2])
            ax.set_yticks([-1, 0, 1])
            ax.set_yticklabels(['Normal', 'Warning', 'Fault'])

            colors = ['green', 'black', 'red']
            for label, color in zip(ax.get_yticklabels(), colors):
                label.set_color(color)

            self.plot_fault_condition_period(start_qdate, end_qdate, ax)

            ax.set_title('Fault Condition')


 
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
                temp_qtimes = self.graphwindowpresenter.data['temperatures'][qdate].keys()

                temp_az_temperatures = [self.graphwindowpresenter.data['temperatures'][qdate][qtime]['az'] for qtime in temp_qtimes]
                temp_el_temperatures = [self.graphwindowpresenter.data['temperatures'][qdate][qtime]['el'] for qtime in temp_qtimes]
                temp_shelter_temperatures = [self.graphwindowpresenter.data['temperatures'][qdate][qtime]['shelter'] for qtime in temp_qtimes]
            
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

        #self.graphwindow.mplCanvasWidget.fig.clf()
        
        #self.axes = self.graphwindow.mplCanvasWidget.fig.add_subplot(111)

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
                temp_qtimes = self.graphwindowpresenter.data['autotest_levels'][qdate].keys()

                temp_az_autotests = [self.graphwindowpresenter.data['autotest_levels'][qdate][qtime]['az'] for qtime in temp_qtimes]
                temp_el_autotests = [self.graphwindowpresenter.data['autotest_levels'][qdate][qtime]['el'] for qtime in temp_qtimes]
            
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
            
        #self.graphwindow.mplCanvasWidget.fig.clf()
        #self.axes = self.graphwindow.mplCanvasWidget.fig.add_subplot(111)

        ax.plot(new_datetimes, new_el_autotests, 'r-.', label='El')
        ax.plot(new_datetimes, new_az_autotests, 'b--', label='Az')
        





    def plot_mti_period(self, start_qdate, stop_qdate, ax, ax2, rwy, radar_mode, weather_mode):

        #print(self.graphwindowpresenter.data['mti_deviations'])

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
                temp_qtimes = self.graphwindowpresenter.data['mti_deviations'][qdate].keys()

                temp_az_mti_deviations = [self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['mti_deviation']['az'] for qtime in temp_qtimes if 
                                            (self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['rwy'] == rwy and
                                            self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['radar_mode'] == radar_mode and
                                            self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['weather_mode'] == weather_mode)]
                
                temp_el_mti_deviations = [self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['mti_deviation']['el'] for qtime in temp_qtimes if 
                                            (self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['rwy'] == rwy and
                                            self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['radar_mode'] == radar_mode and
                                            self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['weather_mode'] == weather_mode)]

                temp_rng_mti_deviations = [self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['mti_deviation']['rng'] for qtime in temp_qtimes if 
                                            (self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['rwy'] == rwy and
                                            self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['radar_mode'] == radar_mode and
                                            self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['weather_mode'] == weather_mode)]
            
                temp_datetimes = [self.to_datetime(qdate, qtime) for qtime in temp_qtimes if 
                                            (self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['rwy'] == rwy and
                                            self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['radar_mode'] == radar_mode and
                                            self.graphwindowpresenter.data['mti_deviations'][qdate][qtime]['weather_mode'] == weather_mode)]

                datetimes.extend(temp_datetimes)

                az_mti_deviations.extend(temp_az_mti_deviations)
                el_mti_deviations.extend(temp_el_mti_deviations)
                rng_mti_deviations.extend(temp_rng_mti_deviations)

            except Exception as e:
                print(e)

        
        #ax2.scatter(datetimes, rng_mti_deviations, c='red', marker='s', label='Rng')

        ax.scatter(datetimes, az_mti_deviations, c='blue', marker='^', label='Az')#, 'b', label='Az')
        ax.scatter(datetimes, el_mti_deviations, c='blue', marker='o', label='El')#, 'r.', label='El')

        ax2.scatter(datetimes, rng_mti_deviations, c='red', marker='s', label='Rng')

        #ax2 = ax.twinx()
        #ax2.set_ylabel('feet')#, color='red')  # we already handled the x-label with ax1
        
        #ax2.scatter(datetimes, rng_mti_deviations, c='red', marker='s', label='Rng')

        #ax2.tick_params(axis='y', labelcolor='red')

        #ax.tick_params(axis='y', labelcolor='blue')

        #lines, labels = ax.get_legend_handles_labels()
        #lines2, labels2 = ax2.get_legend_handles_labels()
        #ax2.legend(lines + lines2, labels + labels2, loc='best')


        #ax.set_ylabel('radians')#, color='blue')

        #ax.set_title('MTI Deviation')

        #for label in ax.get_xticklabels():
        #    label.set_ha("right")
        #    label.set_rotation(30)
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
    











    def plot_fault_condition_period(self, start_qdate, stop_qdate, ax):

        qdates = []
        qdate = start_qdate

        while qdate <= stop_qdate:
            qdates.append(qdate)
            qdate = qdate.addDays(1)

        failed_indications = []
        warning_indications = []
        normal_indications = []

        datetimes = []

        #previous_fault_condition = None
        #previous_qdate = None

        for qdate in qdates:

            try:

                temp_datetimes = []

                qtimes = self.graphwindowpresenter.data['fault_condition'][qdate].keys()

                for qtime in qtimes:

                    new_fault_condition = self.graphwindowpresenter.data['fault_condition'][qdate][qtime]
                
                    if new_fault_condition == 'Failed':
                        failed_indications.append(1)
                        warning_indications.append(None)
                        normal_indications.append(None)
                    elif new_fault_condition == 'Warning':
                        failed_indications.append(None)
                        warning_indications.append(0)
                        normal_indications.append(None)
                    elif new_fault_condition == 'Normal':
                        failed_indications.append(None)
                        warning_indications.append(None)
                        normal_indications.append(-1)
                    else:
                        # This can actually happen! 'Unavail' is given instead of the three above, early on in the systems life.
                        failed_indications.append(None)
                        warning_indications.append(None)
                        normal_indications.append(None)

                    temp_datetimes.append(self.to_datetime(qdate, qtime))

            except KeyError as e:
                print(e)
                #old_condition = self.graphwindowpresenter.data['faults'][qdate][qtime]['old condition']
                #old_condition_datetime = self.to_datetime(qdate, qtime) - datetime.timedelta(microseconds=1)
                #new_condition = self.graphwindowpresenter.data['faults'][qdate][qtime]['new condition']
                #new_condition_datetime = self.to_datetime(qdate, qtime) + datetime.timedelta(microseconds=1)

                #if old_condition == 'Failed':
                #    failed_indications.append(1)
                #    warning_indications.append(None)
                #    normal_indications.append(None)
                #elif old_condition == 'Warning':
                #    failed_indications.append(None)
                #    warning_indications.append(0)
                #    normal_indications.append(None)
                #elif old_condition == 'Normal':
                #    failed_indications.append(None)
                #    warning_indications.append(None)
                #    normal_indications.append(-1)

                #if new_condition == 'Failed':
                #    failed_indications.append(1)
                #    warning_indications.append(None)
                #    normal_indications.append(None)
                #elif new_condition == 'Warning':
                #    failed_indications.append(None)
                #    warning_indications.append(0)
                #    normal_indications.append(None)
                #elif new_condition == 'Normal':
                #    failed_indications.append(None)
                #    warning_indications.append(None)
                #    normal_indications.append(-1)

                

                #failed_indications = [1.0 * each for each in failed_indications if each != None]
                #warning_indications = [0.0 * each for each in warning_indications if each != None]
                #normal_indications = [-1.0 * each for each in normal_indications if each != None]

                #temp_datetimes.append(old_condition_datetime)
                #temp_datetimes.append(new_condition_datetime)

            #temp_failed_datetimes = [self.to_datetime(qdate, qtime) for qtime in temp_failed_qtimes if qtime != None]
            #temp_warning_datetimes = [self.to_datetime(qdate, qtime) for qtime in temp_warning_qtimes if qtime != None]
            #temp_normal_datetimes = [self.to_datetime(qdate, qtime) for qtime in temp_normal_qtimes if qtime != None]

            datetimes.extend(temp_datetimes)
            #warning_datetimes.extend(temp_warning_datetimes)
            #normal_datetimes.extend(temp_normal_datetimes)


        #print(datetimes)
        #print(failed_indications)
        #print(warning_indications)
        #print(normal_indications)

        #self.graphwindow.mplCanvasWidget.fig.clf()
        
        #self.axes = self.graphwindow.mplCanvasWidget.fig.add_subplot(111)

        default_size = matplotlib.rcParams['lines.markersize'] ** 2
        new_size = default_size * 2

        #print('datetimes: ' + str(len(datetimes)))
        #print('failed_indications: ' + str(len(failed_indications)))

        ax.scatter(datetimes, failed_indications, s=new_size, c='r')#, label='Az')
        ax.scatter(datetimes, warning_indications, s=new_size, c='y')#, label='El')
        ax.scatter(datetimes, normal_indications, s=new_size, c='g')#, label='Shelter')