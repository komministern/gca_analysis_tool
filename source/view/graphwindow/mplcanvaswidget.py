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

from __future__ import unicode_literals
import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
#matplotlib.use('Qt5Agg')
#from PyQt5 import QtCore, QtWidgets
from PySide2 import QtCore, QtWidgets

#from numpy import arange, sin, pi
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

#from matplotlib.backends.qt_compat import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


#from matplotlib.backends.backend_qt5agg import FigureCanvas
#from matplotlib.figure import Figure


class MyMplCanvasWidget(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, self.fig)
        
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.fig.canvas.draw()

    def set_new_dpi(self, dpi):
        self.fig.set_dpi(dpi)
        
        #FigureCanvas.updateGeometry(self)

        #self.fig.canvas.draw()
