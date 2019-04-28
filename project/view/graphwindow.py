
# -*- coding: utf-8 -*-

#    Copyright � 2016, 2017, 2018, 2019 Oscar Franz�n <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.

#from matplotlib.backends.qt_compat import QtCore, QtGui, QtWidgets

#import matplotlib

#matplotlib.use('Qt5Agg')

#from matplotlib.backends.qt_compat import QtCore, QtGui, QtWidgets

from PySide2 import QtGui, QtCore, QtWidgets
from view.ui.ui_graphwindow import Ui_MainWindow


class GraphWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    quit = QtCore.Signal()
    draw_graph = QtCore.Signal()

    def __init__(self, parent=None):
        super(GraphWindow, self).__init__()#parent)
        
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('gca.ico'))

        #print(self.windowFlags())

        #self.activateWindow()

        #self.setWindowFlag(QtCore.Qt.)

        #self.resized = False


    def resizeEvent(self, event):
        super(GraphWindow, self).resizeEvent(event)

        self.timer = QtCore.QTimer.singleShot(200, self.draw)

        #self.resized = True

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


