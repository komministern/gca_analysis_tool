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

from PySide2 import QtCore
import datetime as dt

import numpy as np
import presenter.graphwindow.graphessentials as gess




def construct_heater_control_graphs(historylog_qdates, all_qdates, data, radar_on_datetimes, radar_off_datetimes):

    az_on_value = 1.8
    az_off_value = 0.8
    
    el_on_value = 0.5
    el_off_value = -0.5

    blower_on_value = -0.8
    blower_off_value = -1.8



    heater_control_graphs = {}



    az_heater_status_values = []    

    el_heater_status_values = []    

    blower_status_values = []    

    datetimes = []



    # First, just plot the discrete climate control logs.

    for qdate in historylog_qdates:

        temp_az_heater_status_values = []

        temp_el_heater_status_values = []
    
        temp_blower_status_values = []

        temp_datetimes = []

        qtimes = sorted(list(data['heater_control_status'][qdate].keys()))

        for qtime in qtimes:

            present_datetime = gess.to_datetime(qdate, qtime)

            temp_datetimes.append(present_datetime)


            if data['heater_control_status'][qdate][qtime]['az'] == 'On':
                temp_az_heater_status_values.append(az_on_value)
            else:
                temp_az_heater_status_values.append(az_off_value)


            if data['heater_control_status'][qdate][qtime]['el'] == 'On':
                temp_el_heater_status_values.append(el_on_value)
            else:
                temp_el_heater_status_values.append(el_off_value)


            if data['heater_control_status'][qdate][qtime]['blower'] == 'On':
                temp_blower_status_values.append(blower_on_value)
            else:
                temp_blower_status_values.append(blower_off_value)


        az_heater_status_values.extend(temp_az_heater_status_values)

        el_heater_status_values.extend(temp_el_heater_status_values)

        blower_status_values.extend(temp_blower_status_values)

        datetimes.extend(temp_datetimes)




    # Now, add all radar on/off events

    el_heater_status_values_with_on_off_events = []
    datetimes_with_on_off_events = []

    datetime_index = 0
    on_index = 0

    for radar_off_datetime in radar_off_datetimes:

        while datetimes[datetime_index] < radar_off_datetime:
        
            el_heater_status_values_with_on_off_events.append(el_heater_status_values[datetime_index])
            datetimes_with_on_off_events.append(datetimes[datetime_index])
            datetime_index += 1

        el_heater_status_values_with_on_off_events.append(None)
        datetimes_with_on_off_events.append(radar_off_datetime)

        while radar_on_datetimes[on_index] < radar_off_datetime:
            on_index += 1

        el_heater_status_values_with_on_off_events.append(el_off_value)     # ????????????????
        datetimes_with_on_off_events.append(radar_on_datetimes[on_index])

    
    heater_control_graphs['az'] = (datetimes_with_on_off_events, el_heater_status_values_with_on_off_events)
    heater_control_graphs['el'] = (datetimes_with_on_off_events, el_heater_status_values_with_on_off_events)
    heater_control_graphs['blower'] = (datetimes_with_on_off_events, el_heater_status_values_with_on_off_events)


    return heater_control_graphs



    

def slask():

    complete_az_heater_status_values = []    

    complete_el_heater_status_values = []    

    complete_blower_status_values = []    

    complete_datetimes = []

    index = 0

    # Next, plot the radar off events, with the value None.

    for radar_off_datetime in radar_off_datetimes:

        while datetimes[index] < radar_off_datetime:
            complete_az_heater_status_values.append(az_heater_status_values[index])
            complete_el_heater_status_values.append(el_heater_status_values[index])
            complete_blower_status_values.append(blower_status_values[index])
            complete_datetimes.append(datetimes[index])
            index += 1
        
        complete_datetimes.append(radar_off_datetime)

        complete_az_heater_status_values.append(None)
        complete_el_heater_status_values.append(None)
        complete_blower_status_values.append(None)
    



    super_az_heater_status_values = []    

    super_el_heater_status_values = []    

    super_blower_status_values = []    

    super_datetimes = []

    index = 0

    for radar_on_datetime in radar_on_datetimes:

        while complete_datetimes[index] < radar_on_datetime and index < (len(complete_datetimes) - 1):
            super_az_heater_status_values.append(complete_az_heater_status_values[index])
            super_el_heater_status_values.append(complete_el_heater_status_values[index])
            super_blower_status_values.append(complete_blower_status_values[index])
            super_datetimes.append(complete_datetimes[index])
            index += 1
        
        super_datetimes.append(radar_on_datetime)

        super_az_heater_status_values.append(az_off_value)  #
        super_el_heater_status_values.append(el_off_value)  # ???????????????????
        super_blower_status_values.append(blower_off_value) #




    enhanced_az_heater_status_values = []    
    enhanced_az_datetimes = []

    enhanced_el_heater_status_values = []    
    enhanced_el_datetimes = []

    enhanced_blower_status_values = []    
    enhanced_blower_datetimes = []




    enhanced_az_heater_status_values.append(super_az_heater_status_values[0])
    enhanced_az_datetimes.append(super_datetimes[0])

    for t, value in zip(super_datetimes[1:], super_az_heater_status_values[1:]):

        previous_t = enhanced_az_datetimes[-1]
        previous_value = enhanced_az_heater_status_values[-1]

        for i in range(t.day - previous_t.day):

            enhanced_az_datetimes.append(dt.datetime(previous_t.year, previous_t.month, previous_t.day, 23, 59, 59) + dt.timedelta(days=i))
            enhanced_az_heater_status_values.append(previous_value)

            enhanced_az_datetimes.append(dt.datetime(previous_t.year, previous_t.month, previous_t.day, 0, 0, 1) + dt.timedelta(days=i+1))
            enhanced_az_heater_status_values.append(previous_value)

        if previous_value != value:
            enhanced_az_datetimes.append(t - dt.timedelta(seconds=1))
            enhanced_az_heater_status_values.append(previous_value)
        
        enhanced_az_datetimes.append(t)
        enhanced_az_heater_status_values.append(value)


    
    enhanced_el_heater_status_values.append(super_el_heater_status_values[0])
    enhanced_el_datetimes.append(super_datetimes[0])

    for t, value in zip(super_datetimes[1:], super_el_heater_status_values[1:]):

        previous_t = enhanced_el_datetimes[-1]
        previous_value = enhanced_el_heater_status_values[-1]

        for i in range(t.day - previous_t.day):

            enhanced_el_datetimes.append(dt.datetime(previous_t.year, previous_t.month, previous_t.day, 23, 59, 59) + dt.timedelta(days=i))
            enhanced_el_heater_status_values.append(previous_value)

            enhanced_el_datetimes.append(dt.datetime(previous_t.year, previous_t.month, previous_t.day, 0, 0, 1) + dt.timedelta(days=i+1))
            enhanced_el_heater_status_values.append(previous_value)

        if previous_value != value:
            enhanced_el_datetimes.append(t - dt.timedelta(seconds=1))
            enhanced_el_heater_status_values.append(previous_value)
        
        enhanced_el_datetimes.append(t)
        enhanced_el_heater_status_values.append(value)




    enhanced_blower_status_values.append(super_blower_status_values[0])
    enhanced_blower_datetimes.append(super_datetimes[0])

    for t, value in zip(super_datetimes[1:], super_blower_status_values[1:]):

        previous_t = enhanced_blower_datetimes[-1]
        previous_value = enhanced_blower_status_values[-1]

        for i in range(t.day - previous_t.day):

            enhanced_blower_datetimes.append(dt.datetime(previous_t.year, previous_t.month, previous_t.day, 23, 59, 59) + dt.timedelta(days=i))
            enhanced_blower_status_values.append(previous_value)

            enhanced_blower_datetimes.append(dt.datetime(previous_t.year, previous_t.month, previous_t.day, 0, 0, 1) + dt.timedelta(days=i+1))
            enhanced_blower_status_values.append(previous_value)


        if previous_value != value:
            enhanced_blower_datetimes.append(t - dt.timedelta(seconds=1))
            enhanced_blower_status_values.append(previous_value)
        
        enhanced_blower_datetimes.append(t)
        enhanced_blower_status_values.append(value)

        


    




    heater_control_graphs['az'] = (np.array(enhanced_az_datetimes), np.array(enhanced_az_heater_status_values))
    heater_control_graphs['el'] = (np.array(enhanced_el_datetimes), np.array(enhanced_el_heater_status_values))
    heater_control_graphs['blower'] = (np.array(enhanced_blower_datetimes), np.array(enhanced_blower_status_values))


    return heater_control_graphs


