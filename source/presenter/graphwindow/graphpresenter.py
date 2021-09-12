"""
    This file is part of GCA Analysis Tool.

    Copyright (C) 2020 Oscar Franzén <oscarfranzen@protonmail.com>

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

import time
import datetime

from PySide2 import QtCore, QtGui, QtWidgets

from . import graphessentials as gess
from . import radarstatusgraph as radarstatusgraph
from . import temperaturegraph as temperaturegraph
from . import mtigraph as mtigraph
from . import autotestgraph as autotestgraph
from . import heatergraph as heatergraph
from . import faultgraph as faultgraph
from . import tiltgraph as tiltgraph



class GraphPresenter(QtCore.QObject):

    def __init__(self, graphwindowpresenter, data):
        super(GraphPresenter, self).__init__()
        self.graphwindowpresenter = graphwindowpresenter
        self.data = data


        # Let's gather some basic stuff
        self.historylog_qdates = data['dates']

        print(self.historylog_qdates)

        self.all_qdates = self.get_all_qdates()

        # print(self.all_qdates)

        self.radar_on_datetimes = self.get_radar_on_datetimes()
        self.radar_off_datetimes = self.get_radar_off_datetimes()


        # Construct graphs.
        self.radar_on_off_graph = radarstatusgraph.construct_radar_on_off_graph(self.historylog_qdates, self.all_qdates, self.data)
        self.temperature_graphs = temperaturegraph.construct_temperature_graphs(self.historylog_qdates, self.all_qdates, self.data)
        self.mti_deviation_graphs = mtigraph.construct_mti_deviation_graphs(self.historylog_qdates, self.all_qdates, self.data)
        self.autotest_level_graphs = autotestgraph.construct_autotest_level_graphs(self.historylog_qdates, self.all_qdates, self.data)
        #self.heater_control_graphs = heatergraph.construct_heater_control_graphs(self.historylog_qdates, self.all_qdates, self.data, self.radar_on_datetimes, self.radar_off_datetimes)
        self.fault_condition_graphs = faultgraph.construct_fault_condition_graphs(self.historylog_qdates, self.all_qdates, self.data)
        self.tilt_graph = tiltgraph.construct_tilt_graph(self.historylog_qdates, self.all_qdates, self.data)












    # The dates given in the data object are in the form of QDate objects.
    # The times given in the data object are in the form of QTime objects.

    # We will loop through the dates using the Qt objects, but producing the final 
    # graphs (events plus some value) with the datetime object. 


    def get_radar_on_off_graph(self, first_qdate, last_qdate):
        first_datetime = gess.to_datetime(first_qdate, QtCore.QTime(0, 0, s=1))
        last_datetime = gess.to_datetime(last_qdate, QtCore.QTime(23, 59, s=59))
        radar_on_off_graph = list(zip(*[(t, v) for (t, v) in zip(*self.radar_on_off_graph) if (t >= first_datetime and t <= last_datetime)]))
        if radar_on_off_graph:
            return radar_on_off_graph
        else:
            return [[], []]


    def get_fault_condition_graph(self, first_qdate, last_qdate, which):
        first_datetime = gess.to_datetime(first_qdate, QtCore.QTime(0, 0, s=1))
        last_datetime = gess.to_datetime(last_qdate, QtCore.QTime(23, 59, s=59))
        fault_condition_graph = list(zip(*[(t, v) for (t, v) in zip(*self.fault_condition_graphs[which]) if (t >= first_datetime and t <= last_datetime)]))
        if fault_condition_graph:
            return fault_condition_graph
        else:
            return [[], []]

    
    def get_temperature_graph(self, first_qdate, last_qdate, which):
        first_datetime = gess.to_datetime(first_qdate, QtCore.QTime(0, 0, s=1))
        last_datetime = gess.to_datetime(last_qdate, QtCore.QTime(23, 59, s=59))
        temperature_graph = list(zip(*[(t, v) for (t, v) in zip(*self.temperature_graphs[which]) if (t >= first_datetime and t <= last_datetime)]))
        if temperature_graph:
            return temperature_graph
        else:
            return [[], []]


    def get_mti_deviation_graph(self, first_qdate, last_qdate, runway, radar_mode, weather_mode, which):
        first_datetime = gess.to_datetime(first_qdate, QtCore.QTime(0, 0, s=1))
        last_datetime = gess.to_datetime(last_qdate, QtCore.QTime(23, 59, s=59))
        mti_deviation_graph = list(zip(*[(t, v) for (t, v) in zip(*self.mti_deviation_graphs[(runway, radar_mode, weather_mode, which)]) if (t >= first_datetime and t <= last_datetime)]))
        if mti_deviation_graph:
            return mti_deviation_graph
        else:
            return [[], []]


    def get_autotest_level_graph(self, first_qdate, last_qdate, which):
        first_datetime = gess.to_datetime(first_qdate, QtCore.QTime(0, 0, s=1))
        last_datetime = gess.to_datetime(last_qdate, QtCore.QTime(23, 59, s=59))
        autotest_level_graph = list(zip(*[(t, v) for (t, v) in zip(*self.autotest_level_graphs[which]) if (t >= first_datetime and t <= last_datetime)]))
        if autotest_level_graph:
            return autotest_level_graph
        else:
            return [[], []]


    def get_heater_control_graph(self, first_qdate, last_qdate, which):
        first_datetime = gess.to_datetime(first_qdate, QtCore.QTime(0, 0, s=1))
        last_datetime = gess.to_datetime(last_qdate, QtCore.QTime(23, 59, s=59))
        heater_control_graph = list(zip(*[(t, v) for (t, v) in zip(*self.heater_control_graphs[which]) if (t >= first_datetime and t <= last_datetime)]))
        if heater_control_graph:
            return heater_control_graph
        else:
            return [[], []]

    
    def get_tilt_value_graph(self, first_qdate, last_qdate):
        first_datetime = gess.to_datetime(first_qdate, QtCore.QTime(0, 0, s=1))
        last_datetime = gess.to_datetime(last_qdate, QtCore.QTime(23, 59, s=59))
        tilt_value_graph = list(zip(*[(t, v) for (t, v) in zip(*self.tilt_graph) if (t >= first_datetime and t <= last_datetime)]))
        if tilt_value_graph:
            return tilt_value_graph
        else:
            return [[], []]




















    def get_all_qdates(self):
        all_qdates = []
        first_qdate = self.historylog_qdates[0]
        last_qdate = self.historylog_qdates[-1]
        qdate = first_qdate
        while qdate <= last_qdate:
            all_qdates.append(qdate)
            qdate = qdate.addDays(1)
        return all_qdates


    def get_radar_off_datetimes(self):
        radar_off_datetimes = []
        for qdate in self.historylog_qdates:
            qtimes = sorted(list(self.graphwindowpresenter.data['radar_turned_on_off_status'][qdate].keys()))
            temp_radar_off_datetimes = [gess.to_datetime(qdate, qtime) for qtime in qtimes if self.data['radar_turned_on_off_status'][qdate][qtime]['off']]
            radar_off_datetimes.extend(temp_radar_off_datetimes)    
        return radar_off_datetimes
    

    def get_radar_on_datetimes(self):
        radar_on_datetimes = []
        for qdate in self.historylog_qdates:
            qtimes = sorted(list(self.graphwindowpresenter.data['radar_turned_on_off_status'][qdate].keys()))
            temp_radar_on_datetimes = [gess.to_datetime(qdate, qtime) for qtime in qtimes if self.data['radar_turned_on_off_status'][qdate][qtime]['on']]
            radar_on_datetimes.extend(temp_radar_on_datetimes)    
        return radar_on_datetimes
