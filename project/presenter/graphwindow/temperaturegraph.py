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

from PySide2 import QtCore
import datetime as dt

import presenter.graphwindow.graphessentials as gess


def construct_temperature_graphs(historylog_qdates, all_qdates, data):

    datetimes = []
    az_temperatures = []
    el_temperatures = []
    shelter_temperatures = []

    for qdate in all_qdates:

        try:
            temp_qtimes = data['temperatures'][qdate].keys()

            temp_az_temperatures = [data['temperatures'][qdate][qtime]['az'] for qtime in temp_qtimes]
            temp_el_temperatures = [data['temperatures'][qdate][qtime]['el'] for qtime in temp_qtimes]
            temp_shelter_temperatures = [data['temperatures'][qdate][qtime]['shelter'] for qtime in temp_qtimes]
            
            temp_datetimes = [gess.to_datetime(qdate, qtime) for qtime in temp_qtimes]

            datetimes.extend(temp_datetimes)

            az_temperatures.extend(temp_az_temperatures)
            el_temperatures.extend(temp_el_temperatures)
            shelter_temperatures.extend(temp_shelter_temperatures)

        except KeyError:

            pass

    partitioned_datetimes = gess.partition(datetimes)
            
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

        new_datetimes.append(partition[-1] + dt.timedelta(seconds=5000))
        new_az_temperatures.append(None)
        new_el_temperatures.append(None)
        new_shelter_temperatures.append(None)

        i += len(partition)

    if len(new_datetimes) > 1:

        del new_datetimes[-1]
        del new_az_temperatures[-1]
        del new_el_temperatures[-1]
        del new_shelter_temperatures[-1]

    temperature_graphs = {}

    temperature_graphs['az'] = (new_datetimes, new_az_temperatures)
    temperature_graphs['el'] = (new_datetimes, new_el_temperatures)
    temperature_graphs['shelter'] = (new_datetimes, new_shelter_temperatures)

    return temperature_graphs








