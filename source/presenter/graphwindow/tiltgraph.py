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

#import numpy as np
from . import graphessentials as gess


def construct_tilt_graph(historylog_qdates, all_qdates, data):

    tilt_values = []
    tilt_datetimes = []
    
    for qdate in historylog_qdates:

        qtimes = data['tilt_values'][qdate].keys()

        for qtime in qtimes:
            new_tilt_value_string = data['tilt_values'][qdate][qtime]

            tilt_values.append(int(float(new_tilt_value_string)))
            tilt_datetimes.append(gess.to_datetime(qdate, qtime))
            

    tilt_values_graph = (tilt_datetimes, tilt_values)

    return tilt_values_graph
    
