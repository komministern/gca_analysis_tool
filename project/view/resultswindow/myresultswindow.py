
# -*- coding: utf-8 -*-

#    Copyright � 2016, 2017, 2018, 2019 Oscar Franz�n <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtGui, QtCore, QtWidgets
from view.ui.ui_resultswindow import Ui_MainWindow


class MyResultsWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    quit = QtCore.Signal()
    draw_graph = QtCore.Signal()

    def __init__(self, parent=None):
        super(MyResultsWindow, self).__init__(parent)

        # This really is not nice. Font size is set with pixel in view.
        #font = parent.font()
        #self.setFont(font)
        
        self.setupUi(self)

        #self.resized_since_last_mouse_release = False

        self.resized = False


    def resizeEvent(self, event):
        super(MyResultsWindow, self).resizeEvent(event)
        self.resized = True

    def mouseMoveEvent(self, event):    # Somewhat ugly, but how else??? 
        super(MyResultsWindow, self).mouseMoveEvent(event)
        if self.resized:
            self.draw_graph.emit()
            self.resized = False

    def closeEvent(self, event):
        event.ignore()
        self.quit.emit()


