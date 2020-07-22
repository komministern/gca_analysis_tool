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

import presenter.graphwindow.graphessentials as gess


def construct_autotest_level_graphs(historylog_qdates, all_qdates, data):

    datetimes = []
    az_autotests = []
    el_autotests = []

    for qdate in historylog_qdates:

        try:
            temp_qtimes = data['autotest_levels'][qdate].keys()

            temp_az_autotests = [data['autotest_levels'][qdate][qtime]['az'] for qtime in temp_qtimes]
            temp_el_autotests = [data['autotest_levels'][qdate][qtime]['el'] for qtime in temp_qtimes]
            
            temp_datetimes = [gess.to_datetime(qdate, qtime) for qtime in temp_qtimes]

            datetimes.extend(temp_datetimes)

            az_autotests.extend(temp_az_autotests)
            el_autotests.extend(temp_el_autotests)

        except KeyError:

            pass

    partitioned_datetimes = gess.partition(datetimes)

    new_datetimes = []
    new_az_autotests = []
    new_el_autotests = []

    i = 0
    for partition in partitioned_datetimes:

        new_datetimes.extend(partition)
        new_az_autotests.extend(az_autotests[i:i+len(partition)])
        new_el_autotests.extend(el_autotests[i:i+len(partition)])

        new_datetimes.append(partition[-1] + dt.timedelta(seconds=5000))
        new_az_autotests.append(None)
        new_el_autotests.append(None)
            
        i += len(partition)
            
    if len(new_datetimes) > 1:

        del new_datetimes[-1]
        del new_az_autotests[-1]
        del new_el_autotests[-1]
    
    autotest_graphs = {}

    autotest_graphs['az'] = (new_datetimes, new_az_autotests)
    autotest_graphs['el'] = (new_datetimes, new_el_autotests)

    return autotest_graphs







