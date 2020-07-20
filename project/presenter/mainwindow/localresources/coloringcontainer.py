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



class ColoringContainer(object):
        
    def __init__(self, upper_left_red_dates=[], upper_left_green_dates=[], upper_left_yellow_dates=[], upper_left_white_dates=[],
    lower_right_red_dates=[], lower_right_green_dates=[], lower_right_yellow_dates=[], lower_right_white_dates=[]):

        self.upper_left_red_dates = upper_left_red_dates
        self.upper_left_green_dates = upper_left_green_dates
        self.upper_left_yellow_dates = upper_left_yellow_dates
        self.upper_left_white_dates = upper_left_white_dates

        self.lower_right_red_dates = lower_right_red_dates
        self.lower_right_green_dates = lower_right_green_dates
        self.lower_right_yellow_dates = lower_right_yellow_dates
        self.lower_right_white_dates = lower_right_white_dates

