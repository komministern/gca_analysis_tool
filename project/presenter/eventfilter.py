#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtGui, QtCore


class EventBlocker(QtCore.QObject):

    def __init__(self, events_to_block=()):
        super(EventBlocker, self).__init__()
        self.events_to_block = events_to_block
    
    def eventFilter(self, obj, event):
        if event.type() in self.events_to_block:
            #print 'blocked some click on ', obj
            return True
        return super(EventBlocker, self).eventFilter(obj, event)
    
    def block_all_mouse_click_events(self):
        self.events_to_block = (QtCore.QEvent.MouseButtonPress, QtCore.QEvent.MouseButtonRelease, QtCore.QEvent.MouseButtonDblClick, QtCore.QEvent.Wheel)
        
    def unblock_all_events(self):
        self.events_to_block = ()
        