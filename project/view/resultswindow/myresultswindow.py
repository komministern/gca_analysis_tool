
# -*- coding: utf-8 -*-

#    Copyright � 2016, 2017, 2018, 2019 Oscar Franz�n <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


from PySide2 import QtGui, QtCore, QtWidgets
from view.ui.ui_resultswindow import Ui_MainWindow


class MyResultsWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    quit = QtCore.Signal()

    def __init__(self, parent=None):
        super(MyResultsWindow, self).__init__(parent)

        # This really is not nice. Font size is set with pixel in view.
        #font = parent.font()
        #self.setFont(font)

        self.setupUi(self)


    def closeEvent(self, event):
        event.ignore()
        self.quit.emit()