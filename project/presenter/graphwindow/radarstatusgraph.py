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
import datetime

import presenter.graphwindow.graphessentials as gess

def construct_radar_on_off_graph(historylog_qdates, all_qdates, data):

    # This method produces a graph with at least two points each day. So, plots of all lengths will show
    # either on or off at all times. 
    # Some diagonal lines will appear in the plot if the history log has been reset in the system. 
    # (See especially the first date in all_dates)

    #t0 = time.time()

    radar_on_off_status = []
    radar_on_off_datetimes = []

    for qdate in all_qdates:

        try:    # ???????????????????????????
                
            temp_radar_on_off_status = []
            temp_radar_on_off_datetimes = []

            if qdate in data['radar_turned_on_off_status']:
                qtimes = sorted(list(data['radar_turned_on_off_status'][qdate].keys()))
            else:
                temp_radar_on_off_status.append(0)
                temp_radar_on_off_datetimes.append(gess.to_datetime(qdate, QtCore.QTime(0, 0, s=1)))
                temp_radar_on_off_status.append(0)
                temp_radar_on_off_datetimes.append(gess.to_datetime(qdate, QtCore.QTime(23, 59, s=59)))
                qtimes = []

            for qtime in qtimes:

                if qtime == qtimes[0] and not data['radar_turned_on_off_status'][qdate][qtime]['still on']:
                        
                    temp_radar_on_off_status.append(0)
                    temp_radar_on_off_datetimes.append(gess.to_datetime(qdate, QtCore.QTime(0, 0, 1)))

                if data['radar_turned_on_off_status'][qdate][qtime]['still on']:
                        
                    temp_radar_on_off_status.append(1)
                    temp_radar_on_off_datetimes.append(gess.to_datetime(qdate, qtime))

                elif data['radar_turned_on_off_status'][qdate][qtime]['on']:

                    temp_radar_on_off_status.append(0)
                    temp_radar_on_off_datetimes.append(gess.to_datetime(qdate, qtime) - datetime.timedelta(seconds=1))
                        
                    temp_radar_on_off_status.append(1)
                    temp_radar_on_off_datetimes.append(gess.to_datetime(qdate, qtime))
                    
                elif data['radar_turned_on_off_status'][qdate][qtime]['off']:

                    temp_radar_on_off_status.append(1)
                    temp_radar_on_off_datetimes.append(gess.to_datetime(qdate, qtime) - datetime.timedelta(seconds=1))

                    temp_radar_on_off_status.append(0)
                    temp_radar_on_off_datetimes.append(gess.to_datetime(qdate, qtime))

                    
                if qtime == qtimes[-1]:
                    if temp_radar_on_off_status[-1] == 0:

                        temp_radar_on_off_status.append(0)
                        temp_radar_on_off_datetimes.append(gess.to_datetime(qdate, QtCore.QTime(23, 59, 59)))

                    elif temp_radar_on_off_status[-1] == 1:

                        temp_radar_on_off_status.append(1)
                        temp_radar_on_off_datetimes.append(gess.to_datetime(qdate, QtCore.QTime(23, 59, 59)))

        except Exception as e:
            print('Exception in get_radar_on_graph')
            print(e)
            
        radar_on_off_status.extend(temp_radar_on_off_status)
        radar_on_off_datetimes.extend(temp_radar_on_off_datetimes)
        
    #print('get_radar_on_graph - ' + str(time.time() - t0))
        
    return (radar_on_off_datetimes, radar_on_off_status)