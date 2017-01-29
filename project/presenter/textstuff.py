#!/usr/bin/env python
# -*- coding: utf-8 -*-


#    Copyright © 2016, 2017 Oscar Franzén <oscarfranzen@yahoo.se>
#
#    This file is part of GCA Analysis Tool.


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



