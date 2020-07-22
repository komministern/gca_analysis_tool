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


def construct_fault_condition_graphs(historylog_qdates, all_qdates, data):

    failed_indications = []
    warning_indications = []
    normal_indications = []

    failed_datetimes = []
    warning_datetimes = []
    normal_datetimes = []


    for qdate in historylog_qdates:

        qtimes = data['fault_conditions'][qdate].keys()

        for qtime in qtimes:

            new_fault_condition = data['fault_conditions'][qdate][qtime]
                
            if new_fault_condition == 'Failed':
                failed_indications.append(1)
                failed_datetimes.append(gess.to_datetime(qdate, qtime))

            elif new_fault_condition == 'Warning':
                warning_indications.append(0)
                warning_datetimes.append(gess.to_datetime(qdate, qtime))
            
            elif new_fault_condition == 'Normal':
                normal_indications.append(-1)
                normal_datetimes.append(gess.to_datetime(qdate, qtime))
            
            else:
                print('Unavail')
                # This can actually happen! 'Unavail' is given instead of the three above, early on in the systems life.
                

    fault_condition_graphs = {}

    fault_condition_graphs['failed'] = (failed_datetimes, failed_indications)
    fault_condition_graphs['warning'] = (warning_datetimes, warning_indications)
    fault_condition_graphs['normal'] = (normal_datetimes, normal_indications)

    return fault_condition_graphs
    
