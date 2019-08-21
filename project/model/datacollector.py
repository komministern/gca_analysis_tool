#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.

from PySide2 import QtCore

import copy

import model.datacollector_helper_functions as dchf

class Datacollector(QtCore.QObject):


    def __init__(self, model):

        super(Datacollector, self).__init__()

        self.model = model

        self.last_working_date = QtCore.QDate(2019, 12, 31)


    def set_progress(self, progress):
        self.model.io_progress.emit(progress)


    def get_analysis(self, site_name, start_date, end_date, use_ignored=False):

        analysis = {}

        self.set_progress(10)

        if use_ignored:
            self.dates = sorted([date for date in self.model.get_historylog_dictionary(site_name).keys() if (date >= start_date) and (date <= end_date) and (date <= self.last_working_date)])
        else:
            ignored_dates = self.model.get_ignored_dates(site_name)
            self.dates = sorted([date for date in self.model.get_historylog_dictionary(site_name).keys() if (date >= start_date) and (date <= end_date) and (date <= self.last_working_date) and date not in ignored_dates])
        
        self.historylog_dict = {date:self.model.get_historylog_dictionary(site_name)[date] for date in self.dates}





        self.set_progress(0)

        n = 10
        d = int(95/n)
        prog = 5

        analysis['system_name'] = site_name
        self.set_progress(prog)
        prog += d

        analysis['dates'] = self.dates
        self.set_progress(prog)
        prog += d

        analysis['temperatures'] = {date:self.get_temperatures(date) for date in self.dates}
        self.set_progress(prog)
        prog += d

        analysis['autotest_levels'] = {date:self.get_autotest_levels(date) for date in self.dates}
        self.set_progress(prog)
        prog += d

        analysis['mti_deviations'] = {date:self.get_mti_deviations(date) for date in self.dates}
        self.set_progress(prog)
        prog += d

        analysis['minutes_report'] = {date:self.get_minutes_report(date) for date in self.dates}
        self.set_progress(prog)
        prog += d

        #analysis['faults'] = {date:self.get_faults(date) for date in self.dates}
        #self.set_progress(90)

        analysis['fault_conditions'] = {date:self.get_fault_condition(date) for date in self.dates}
        self.set_progress(prog)
        prog += d

        analysis['heater_control_status'] = {date:self.get_heater_control_status(date) for date in self.dates}
        self.set_progress(prog)
        prog += d

        analysis['radar_turned_on_off_status'] = {date: self.get_radar_turned_on_off_actions(date) for date in self.dates}
        self.set_progress(prog)
        prog += d

        analysis['tilt_values'] = {date: self.get_tilt_values(date) for date in self.dates}
        self.set_progress(100)




        #return copy.deepcopy(analysis)     # Necessary?
        return analysis




    def update_fault_index_file(self):

        import os
        cwd = os.getcwd()
        resource_dir = os.path.join(cwd, 'resources')
        index_file_path = os.path.join(resource_dir, 'fault_index.txt')

        try:
            with open(index_file_path) as f:
                indexed_faults = f.readlines()
            known_fault_dict = {}
            print('----------------------------------------------------------')
            print('previously saved faults:')
            for line in indexed_faults:
                strings = line.split(';')
                number = int( strings[0] )
                fault_texts = [s.strip() for s in strings[1:]]
                known_fault_dict[number] = fault_texts
                
                string_to_print = str(number)
                for each in fault_texts:
                    string_to_print = string_to_print + ', ' + each
                print(string_to_print)

            print('')
        except Exception:
            print('----------------------------------------------------------')
            print('no previously saved faults')
            known_fault_dict = {}
            print('')

        for date in self.faults:
            for time, fault in self.faults[date].items():

                if not fault['number'] in known_fault_dict.keys():
                    print('----------------------------------------------------------')
                    print('added fault: ' + str(fault['number']) + '   ' + fault['text'])
                    known_fault_dict[fault['number']] = [fault['text']]
                else:
                    if not fault['text'] in known_fault_dict[ fault['number'] ]:
                        print('---------------------------------------------------------')
                        print('conflict in fault name')
                        print(date)
                        print(time)
                        print('fault number: ' + str(fault['number']))
                        print('new fault text: ' + fault['text'])
                        for each in known_fault_dict[fault['number']]:
                            print('old fault text: ' + each)
                        print('adding new fault text anyway')
                        print('')
                        known_fault_dict[ fault['number'] ].append( fault['text'] )


        with open(index_file_path, 'w') as f:
            numbers = sorted(known_fault_dict.keys())
            for number in numbers:
                f.write(str(number))
                for each in known_fault_dict[number]:
                    f.write(';' + each.strip())
                f.write('\n')

        numbers = sorted(known_fault_dict.keys())
        for number in numbers:
            for each in known_fault_dict[number]:
                print(str(number) + '   ' + each)

        # read all faults into a database



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
        
        except UnboundLocalError as e:
            # This happens when one of the variables above is referenced before assignment. That
            # is, on days when the relevant information does not exist in the historylog. (Typically
            # on the same day as the CaptureSite is done.)

            print('------------------------------------------------------')
            print(date)
            print(e)

            return {}


    def get_radar_turned_on_off_actions(self, date):
        radar_turned_on_off_entries = [line for line in self.historylog(date).splitlines() if (dchf.radar_still_on_entry(line) or dchf.radar_turned_on_entry(line) or dchf.radar_turned_off_entry(line))]
        radar_turned_on_off_entries_day = {}

        for radar_turned_on_off_entry in radar_turned_on_off_entries:
            radar_turned_on_off_entries_day[dchf.time(radar_turned_on_off_entry)] = dchf.radar_turned_on_off_actions(radar_turned_on_off_entry)

        return radar_turned_on_off_entries_day


    def get_fault_condition(self, date):
        fault_condition_entries = [line for line in self.historylog(date).splitlines() if dchf.fault_condition_entry(line)]
        fault_condition_entries_day = {}

        for fault_condition_entry in fault_condition_entries:
            fault_condition_entries_day[dchf.time(fault_condition_entry)] = dchf.fault_condition(fault_condition_entry)

        return fault_condition_entries_day


    def get_tilt_values(self, date):
        tilt_status_entries = [line for line in self.historylog(date).splitlines() if dchf.tilt_status_entry(line)]
        tilt_status_entries_day = {}

        for tilt_status_entry in tilt_status_entries:
            tilt_status_entries_day[dchf.time(tilt_status_entry)] = dchf.tilt_value(tilt_status_entry)

        return tilt_status_entries_day



    def get_faults(self, date):
        fault_entries = [line for line in self.historylog(date).splitlines() if dchf.fault_details_entry(line)]
        fault_entries_day = {}

        for fault_entry in fault_entries:
            fault_entries_day[dchf.time(fault_entry)] = dchf.fault_details(fault_entry)

        return fault_entries_day


    def get_heater_control_status(self, date):
        heater_control_entries = [line for line in self.historylog(date).splitlines() if dchf.heater_control_entry(line)]
        heater_control_dictionary_day = {}

        for heater_control_entry in heater_control_entries:
            heater_control_dictionary_day[dchf.time(heater_control_entry)] = dchf.heater_control_status(heater_control_entry)
        
        return heater_control_dictionary_day


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
                tilt = dchf.tilt_value(entry)

            elif dchf.weather_status_entry(entry):
                weather = dchf.weather(entry)

            elif dchf.runway_status_entry(entry):
                runway = dchf.runway(entry)
                direction = dchf.direction(entry)

            elif dchf.radar_mode_status_entry(entry):
                radar_mode = dchf.radar_mode(entry)

            elif dchf.mti_deviation_status_entry(entry):
                try:
                    #state = (runway, direction, radar_mode, weather, tilt)
                    mti_deviation_dictionary_day[dchf.time(entry)] = {'tilt': tilt, 'weather_mode': weather, 'rwy': runway, 'direction': direction, 'radar_mode': radar_mode, 'mti_deviation': dchf.mti_deviations(entry)}
                except UnboundLocalError as e:
                    # This happens sometimes for some reason. (Luleå 130520 for example.) The daily historylog entry
                    # should always start with a state update. But sometimes, very seldom, this does not happen. 
                    print('--------------------------------------------------------------')
                    print(date)
                    print(e)

        return mti_deviation_dictionary_day


    
        