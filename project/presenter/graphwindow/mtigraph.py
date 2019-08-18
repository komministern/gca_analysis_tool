

from PySide2 import QtCore
import datetime as dt

import presenter.graphwindow.graphessentials as gess


def construct_mti_deviation_graphs(historylog_qdates, all_qdates, data):

    mti_deviation_graph_dict = {}

    runways = ('Rwy1', 'Rwy2', 'Rwy3', 'Rwy4', 'Rwy5', 'Rwy6')
    radar_modes = ('PAR', 'Combined')
    weather_modes = ('Clear', 'Rain')

    for rwy in runways:
        for radar_mode in radar_modes:
            for weather_mode in weather_modes:

                datetimes = []
                az_mti_deviations = []
                el_mti_deviations = []
                rng_mti_deviations = []

                for qdate in historylog_qdates:

                    try:

                        temp_qtimes = data['mti_deviations'][qdate].keys()

                        temp_az_mti_deviations = [data['mti_deviations'][qdate][qtime]['mti_deviation']['az'] for qtime in temp_qtimes if 
                                            (data['mti_deviations'][qdate][qtime]['rwy'] == rwy and
                                            data['mti_deviations'][qdate][qtime]['radar_mode'] == radar_mode and
                                            data['mti_deviations'][qdate][qtime]['weather_mode'] == weather_mode)]
                
                        temp_el_mti_deviations = [data['mti_deviations'][qdate][qtime]['mti_deviation']['el'] for qtime in temp_qtimes if 
                                            (data['mti_deviations'][qdate][qtime]['rwy'] == rwy and
                                            data['mti_deviations'][qdate][qtime]['radar_mode'] == radar_mode and
                                            data['mti_deviations'][qdate][qtime]['weather_mode'] == weather_mode)]

                        temp_rng_mti_deviations = [data['mti_deviations'][qdate][qtime]['mti_deviation']['rng'] for qtime in temp_qtimes if 
                                            (data['mti_deviations'][qdate][qtime]['rwy'] == rwy and
                                            data['mti_deviations'][qdate][qtime]['radar_mode'] == radar_mode and
                                            data['mti_deviations'][qdate][qtime]['weather_mode'] == weather_mode)]
            
                        temp_datetimes = [gess.to_datetime(qdate, qtime) for qtime in temp_qtimes if 
                                            (data['mti_deviations'][qdate][qtime]['rwy'] == rwy and
                                            data['mti_deviations'][qdate][qtime]['radar_mode'] == radar_mode and
                                            data['mti_deviations'][qdate][qtime]['weather_mode'] == weather_mode)]

                        datetimes.extend(temp_datetimes)

                        az_mti_deviations.extend(temp_az_mti_deviations)
                        el_mti_deviations.extend(temp_el_mti_deviations)
                        rng_mti_deviations.extend(temp_rng_mti_deviations)

                    except Exception as e:
                
                        print(e)

                mti_deviation_graph_dict[(rwy, radar_mode, weather_mode, 'az')] = (datetimes, az_mti_deviations)
                mti_deviation_graph_dict[(rwy, radar_mode, weather_mode, 'el')] = (datetimes, el_mti_deviations)
                mti_deviation_graph_dict[(rwy, radar_mode, weather_mode, 'rng')] = (datetimes, rng_mti_deviations)

    return mti_deviation_graph_dict

        #ax2.scatter(datetimes, rng_mti_deviations, c='red', marker='s', label='Rng')

        #ax.scatter(datetimes, az_mti_deviations, c='blue', marker='^', label='Az')#, 'b', label='Az')
        #ax.scatter(datetimes, el_mti_deviations, c='blue', marker='o', label='El')#, 'r.', label='El')

        #ax2.scatter(datetimes, rng_mti_deviations, c='red', marker='s', label='Rng')
