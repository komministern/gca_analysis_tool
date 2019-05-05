
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

        #self.mousepressed = False
        #self.resizewhenmousereleased = False
        
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('gca.ico'))

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


