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

#from matplotlib.backends.qt_compat import QtCore, QtGui, QtWidgets

#import matplotlib

#matplotlib.use('Qt5Agg')

#from matplotlib.backends.qt_compat import QtCore, QtGui, QtWidgets

import os

from PySide2 import QtGui, QtCore, QtWidgets
from view.ui.ui_graphwindow import Ui_MainWindow

import common.frozenstuff as frozenstuff


class GraphWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    quit = QtCore.Signal()
    draw_graph = QtCore.Signal()

    def __init__(self, parent=None):
        super(GraphWindow, self).__init__()#parent)

        #self.mousepressed = False
        #self.resizewhenmousereleased = False
        
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon(os.path.join(frozenstuff.cwd('resources'), 'gca.ico')))

        #print(self.windowFlags())

        #self.activateWindow()

        #self.setWindowFlag(QtCore.Qt.)

        #self.resized = False


    def resizeEvent(self, event):

        #print('resized')

        super(GraphWindow, self).resizeEvent(event)

        #if self.mousepressed:
        #    self.resizewhenmousereleased = True
        #    print('pending redraw')
        
        self.timer = QtCore.QTimer.singleShot(500, self.draw)

        #self.resized = True

    def mousePressEvent(self, event):
        #self.mousepressed = True
        #print('mousepressed')
        super(GraphWindow, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        #if self.resizewhenmousereleased:
        #    self.draw_graph.emit()
        #    print('redraw')
        
        #self.resizewhenmousereleased = False
        #self.mousepressed = False

        super(GraphWindow, self).mouseReleaseEvent(event)


    def draw(self):
        self.draw_graph.emit()

    def mouseMoveEvent(self, event):    # Somewhat ugly, but how else??? 
        super(GraphWindow, self).mouseMoveEvent(event)
        #if self.resized:
        #    self.draw_graph.emit()
        #    self.resized = False


    def closeEvent(self, event):
        self.quit.emit()
        super(GraphWindow, self).closeEvent(event)


