#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtCore


def temperature_autotest_status_entry(line):
    return ('(23)' == line[:4])

def radar_mode_status_entry(line):
    return ('(0e)' == line[:4])

def mti_deviation_status_entry(line):
    return ('(1e)' == line[:4])

def tilt_status_entry(line):
    return ('(1b)' == line[:4])

def weather_status_entry(line):
    return ('(1a)' == line[:4])

def runway_status_entry(line):
    return ('(11)' == line[:4])

def runway_number_minutes_report(line):
    return ('(0a)' == line[:4])

def radar_mode_minutes_report_entry(line):
    return ('(07)' == line[:4])

def function_status_minutes_report_entry(line):
    return ('(03)' == line[:4])

def system_off_minutes_report_entry(line):
    return ('(12)' == line[:4])

def maintenance_mode_minutes_report_entry(line):
    return ('(09)' == line[:4])

def transmitter_minutes_report_entry(line):
    return ('(05)' == line[:4])

def antenna_drive_minutes_report_entry(line):
    return ('(04)' == line[:4])

def ssr_on_minutes_report_entry(line):
    return ('(08)' == line[:4])

def fault_condition_entry(line):
    return ('(13)' == line[:4])

def fault_details_entry(line):
    return ('(14)' == line[:4])

def further_fault_details_entry(line):
    return ('(15)' == line[:4])


def time(line):
    hour = int(line[14:16])
    minute = int(line[17:19])
    second = int(line[20:22])
    return QtCore.QTime(hour, minute, second)



def runway(line):
    if mti_deviation_status_entry(line):
        runway = 'Rwy' + line[50:51]
    elif runway_status_entry(line):
        runway = 'Rwy' + line[31:32]
    return runway

def direction(line):
    return line[34:].strip()

def weather(line):
    return line[32:].strip()

def radar_mode(line):
    return line[35:].strip()

def tilt(line):
    return line[37:].strip()



def runway_x_minutes(line, n):
    runway_minutes_strings = line[24:].split()[0].split('/')
    return int( runway_minutes_strings[n - 1] )


def x_status_minutes(line, n):
    temp_string = line[24:40].replace(' ', '')
    #print(temp_string)
    x_minutes_string = temp_string.split('/')[n]
    return int( x_minutes_string )

def normal_status_minutes(line):
    return x_status_minutes(line, 0)

def degraded_status_minutes(line):
    return x_status_minutes(line, 1)

def faulted_status_minutes(line):
    return x_status_minutes(line, 2)


def x_mode_minutes(line, n):
    temp_string = line[24:40].replace(' ', '')
    #print(temp_string)
    x_minutes_string = temp_string.split('/')[n]
    return int( x_minutes_string )

def par_mode_minutes(line):
    return x_mode_minutes(line, 0)

def asr_mode_minutes(line):
    return x_mode_minutes(line, 1)

def combined_mode_minutes(line):
    return x_mode_minutes(line, 2)


def system_off_minutes(line):
    temp_string = line[23:].split()
    return int( temp_string[0] )

def maintenance_mode_minutes(line):
    temp_string = line[23:].split()
    return int( temp_string[0] )

def transmitter_minutes(line):
    temp_string = line[23:].split()
    return int( temp_string[0] )

def antenna_drive_minutes(line):
    temp_string = line[23:].split()
    return int( temp_string[0] )

def ssr_minutes(line):
    temp_string = line[23:].split()
    return int( temp_string[0] )


def temperatures(line):
    temperature_dict = {}

    shelter_temp_first_index = line.find('=') + 1
    shelter_temp_last_index = line.find('C,', shelter_temp_first_index)

    az_temp_first_index = line.find('=', shelter_temp_last_index) + 1
    az_temp_last_index = line.find('C,', az_temp_first_index)

    el_temp_first_index = line.find('=', az_temp_last_index) + 1
    el_temp_last_index = line.find('C.', el_temp_first_index)

    temperature_dict['az'] = int(line[az_temp_first_index:az_temp_last_index])
    temperature_dict['el'] = int(line[el_temp_first_index:el_temp_last_index])
    temperature_dict['shelter'] = int(line[shelter_temp_first_index:shelter_temp_last_index])

    return temperature_dict


def autotest_levels(line):
    autotest_dict = {}

    az_autotest_first_index = line.find('Auto-Test: Az=') + 14
    az_autotest_last_index = line.find(' dB', az_autotest_first_index)

    el_autotest_first_index = line.find('=', az_autotest_last_index) + 1
    el_autotest_last_index = line.find(' dB', el_autotest_first_index)

    autotest_dict['az'] = int(line[az_autotest_first_index:az_autotest_last_index])
    autotest_dict['el'] = int(line[el_autotest_first_index:el_autotest_last_index])

    return autotest_dict


def mti_deviations(line):

    mti_deviations_dict = {}

    str_values = line[65:].split('/')

    mti_deviations_dict['az'] = float(str_values[0])
    mti_deviations_dict['el'] = float(str_values[1])
    mti_deviations_dict['rng'] = float(str_values[2])

    return mti_deviations_dict

def fault_condition(line):
    return line.split()[-1]


def fault_details(line):
    fault_details_dict = {}

    fault_number = int( line[23:28].strip() )
    fault_text = line[41:]

    condition_codes = line[29:32].split('-')
    #print(condition_codes)
    condition_texts = ('Normal', 'Warning', 'Failed')

    old_condition = condition_texts[ int( condition_codes[0] ) - 1 ]
    new_condition = condition_texts[ int( condition_codes[1] ) - 1 ]

    fault_details_dict['number'] = fault_number
    fault_details_dict['text'] = fault_text
    fault_details_dict['old condition'] = old_condition
    fault_details_dict['new condition'] = new_condition

    return fault_details_dict

#def radar_mode_minutes_report(line):
#    return line[]


