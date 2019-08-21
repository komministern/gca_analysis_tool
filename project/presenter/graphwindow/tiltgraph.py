
from PySide2 import QtCore
import datetime as dt

#import numpy as np
import presenter.graphwindow.graphessentials as gess


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
    
