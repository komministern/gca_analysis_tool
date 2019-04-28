
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

    def __init__(self, parent=None, width=5, height=4, dpi=150):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        
        #self.axes = self.fig.add_subplot(111)

        #self.compute_initial_figure()

        FigureCanvas.__init__(self, self.fig)
        
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass