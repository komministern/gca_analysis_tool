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

#import os
#import string
from PySide2 import QtCore, QtGui
#from coloringcontainer import ColoringContainer
#import textstuff as txt


class Filter(QtCore.QObject):

    SUPPRESS = 0
    SHOWONLY = 1

    def __init__(self):
        super(Filter, self).__init__()

        self.content = []
        self.state = self.SUPPRESS

        self.name = u''


