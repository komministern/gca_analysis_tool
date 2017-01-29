#!/usr/bin/env python
# -*- coding: utf-8 -*-


#    Copyright © 2016, 2017 Oscar Franzén <oscarfranzen@yahoo.se>
#
#    This file is part of GCA Analysis Tool.


class ColoringContainer(object):
        
    def __init__(self, upper_left_red_dates, upper_left_green_dates, upper_left_yellow_dates, upper_left_white_dates,
    lower_right_red_dates, lower_right_green_dates, lower_right_yellow_dates, lower_right_white_dates):

        self.upper_left_red_dates = upper_left_red_dates
        self.upper_left_green_dates = upper_left_green_dates
        self.upper_left_yellow_dates = upper_left_yellow_dates
        self.upper_left_white_dates = upper_left_white_dates

        self.lower_right_red_dates = lower_right_red_dates
        self.lower_right_green_dates = lower_right_green_dates
        self.lower_right_yellow_dates = lower_right_yellow_dates
        self.lower_right_white_dates = lower_right_white_dates
