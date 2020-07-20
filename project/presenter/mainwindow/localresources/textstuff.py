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


def normal(text):
    if '(03)' in text:
        index = text.find('(03)')
        if int(text[index+24:index+28]) > 0:
            return True
        else:
            return False
    else:
        return False


def degraded(text):
    if '(03)' in text:
        index = text.find('(03)')

        try:
            if int(text[index+29:index+33]) > 0:
                return True
            else:
                return False
        except ValueError:
            if int(text[1 + index+29:1 + index+33]) > 0:
                return True
            else:
                return False
    else:
        return False

def faulted(text):
    if '(03)' in text:
        index = text.find('(03)')
                    
        # BIZARRE!!!! Get to the bottom of this with some kind of step function!!!!!
            
        try:
            if int(text[index+34:index+38]) > 0:
                return True
            else:
                return False
        except ValueError:
            if int(text[1 + index+34:1 + index+38]) > 0:
                return True
            else:
                return False 
    else:
        return False



def new_fault_in(text):
    if '(16)' in text:
        index = text.find('(16)')
        if int(text[index+24:index+30]) > 0:
            return True
        else:
            return False
    else:
        return False


def no_new_fault_in(text):
    if '(16)' in text:
        index = text.find('(16)')
        if int(text[index+24:index+30]) == 0:
            return True
        else:
            return False
    else:
        return False


def active_fault_in(text):
    if '(17)' in text:
        index = text.find('(17)')
        if int(text[index+24:index+30]) > 0:
            return True
        else:
            return False
    else:
        return False


def no_active_fault_in(text):
    if '(17)' in text:
        index = text.find('(17)')
        if int(text[index+24:index+30]) == 0:
            return True
        else:
            return False
    else:
        return False


def transmitter_on(text):
    
    if '(05)' in text:
        index = text.find('(05)')
        if int(text[index+24:index+30]) > 0:
            return True
        else:
            return False
    else:
        return False



