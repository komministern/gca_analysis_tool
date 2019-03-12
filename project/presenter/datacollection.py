

from PySide2 import QtCore

import copy

import presenter.datacollection_helper_functions as dchf

class DataCollection(QtCore.QObject):



    def __init__(self, historylog_dict, start_date, end_date):

        super(DataCollection, self).__init__()

        self.dates = sorted([date for date in historylog_dict.keys() if (date >= start_date) and (date <= end_date)])

        self.historylog_dict = copy.deepcopy({date:historylog_dict[date] for date in self.dates})

        self.temperatures = {date:self.get_temperatures(date) for date in self.dates}
        self.autotest_levels = {date:self.get_autotest_levels(date) for date in self.dates}
        self.mti_deviations = {date:self.get_mti_deviations(date) for date in self.dates}
        self.minutes_report = {date:self.get_minutes_report(date) for date in self.dates}



        # Check for instantaneous/short lived faults

        # Collect all faults by name/code and count them

        # Count/draw power failures


    def historylog(self, date):
        try:
            return self.historylog_dict[date]

        except KeyError:
            # If the date does not exist in the database, return a empty historylog.
            return ''



    def get_minutes_report(self, date):
        relevant_status_entries = [line for line in self.historylog(date).splitlines() if line[1:3] in ('0a', '03', '07', '12', '09', '05', '04', '08')]

        minutes_report_day = {}

        #print(date)

        for entry in relevant_status_entries:

            if dchf.runway_number_minutes_report(entry):
                runway_minutes_report = {}
                for i in range(1, 7):
                    runway_minutes_report[i] = dchf.runway_x_minutes(entry, i)

            elif dchf.radar_mode_minutes_report_entry(entry):
                par_mode_minutes_report = dchf.par_mode_minutes(entry)
                asr_mode_minutes_report = dchf.asr_mode_minutes(entry)
                combined_mode_minutes_report = dchf.combined_mode_minutes(entry)

            elif dchf.function_status_minutes_report_entry(entry):
                normal_status_minutes_report = dchf.normal_status_minutes(entry)
                degraded_status_minutes_report = dchf.degraded_status_minutes(entry)
                faulted_status_minutes_report = dchf.faulted_status_minutes(entry)

            elif dchf.system_off_minutes_report_entry(entry):
                system_off_minutes_report = dchf.system_off_minutes(entry)

            elif dchf.maintenance_mode_minutes_report_entry(entry):
                maintenance_mode_minutes_report = dchf.maintenance_mode_minutes(entry)

            elif dchf.transmitter_minutes_report_entry(entry):
                transmitter_minutes_report = dchf.transmitter_minutes(entry)

            elif dchf.antenna_drive_minutes_report_entry(entry):
                antenna_drive_minutes_report = dchf.antenna_drive_minutes(entry)

            elif dchf.ssr_on_minutes_report_entry(entry):
                ssr_minutes_report = dchf.ssr_minutes(entry)

        try:
            minutes_report_day['runway'] = runway_minutes_report
            minutes_report_day['par'] = par_mode_minutes_report
            minutes_report_day['asr'] = asr_mode_minutes_report
            minutes_report_day['combined'] = combined_mode_minutes_report
            minutes_report_day['normal'] = normal_status_minutes_report
            minutes_report_day['degraded'] = degraded_status_minutes_report
            minutes_report_day['faulted'] = faulted_status_minutes_report
            minutes_report_day['system off'] = system_off_minutes_report
            minutes_report_day['maintenance mode'] = maintenance_mode_minutes_report
            minutes_report_day['transmitter'] = transmitter_minutes_report
            minutes_report_day['antenna drive'] = antenna_drive_minutes_report
            minutes_report_day['ssr'] = ssr_minutes_report
            return minutes_report_day
        
        except UnboundLocalError:
            # This happens when one of the variables above is referenced before assignment. That
            # is, on days when the relevant information does not exist in the historylog. (Typically
            # on the same day as the CaptureSite is done.)
            return {}




        
            

    def get_temperatures(self, date):
        temperature_entries = [line for line in self.historylog(date).splitlines() if dchf.temperature_autotest_status_entry(line)]
        temperature_dictionary_day = {}

        for temperature_entry in temperature_entries:
            temperature_dictionary_day[dchf.time(temperature_entry)] = dchf.temperatures(temperature_entry)

        return temperature_dictionary_day


    def get_autotest_levels(self, date):
        autotest_entries = [line for line in self.historylog(date).splitlines() if dchf.temperature_autotest_status_entry(line)]
        autotest_dictionary_day = {}

        for autotest_entry in autotest_entries:
            autotest_dictionary_day[dchf.time(autotest_entry)] = dchf.autotest_levels(autotest_entry)

        return autotest_dictionary_day


    def get_mti_deviations(self, date):
        
        relevant_status_entries = [line for line in self.historylog(date).splitlines() if line[1:3] in ('1a', '1b', '11', '0e', '1e')]

        mti_deviation_dictionary_day = {}

        for entry in relevant_status_entries:

            if dchf.tilt_status_entry(entry):
                tilt = dchf.tilt(entry)

            elif dchf.weather_status_entry(entry):
                weather = dchf.weather(entry)

            elif dchf.runway_status_entry(entry):
                runway = dchf.runway(entry)
                direction = dchf.direction(entry)

            elif dchf.radar_mode_status_entry(entry):
                radar_mode = dchf.radar_mode(entry)

            elif dchf.mti_deviation_status_entry(entry):
                state = (runway, direction, radar_mode, weather, tilt)

                mti_deviation_dictionary_day[dchf.time(entry)] = ( state, dchf.mti_deviations(entry) )

        return mti_deviation_dictionary_day


    
        