"""
    This file is part of GCA Analysis Tool.

    Copyright (C) 2020 Oscar Franzén <oscarfranzen@protonmail.com>

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
        