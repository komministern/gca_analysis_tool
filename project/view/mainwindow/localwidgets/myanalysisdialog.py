# -*- coding: utf-8 -*-

#    Copyright � 2016, 2017, 2018, 2019 Oscar Franz�n <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.



from PySide2 import QtGui, QtCore, QtWidgets
from view.ui.ui_analysisdialog import Ui_Dialog
#from presenter.filtercontainer import Filter

class MyAnalysisDialog(QtWidgets.QDialog, Ui_Dialog):

#    quit = QtCore.Signal()

    def __init__(self, parent=None):
        super(MyAnalysisDialog, self).__init__(parent)

        # This really is not nice. Font size is set with pixel in view.
        font = parent.font()
        self.setFont(font)

        self.setupUi(self)

        self.from_date = self.calendarWidget.selectedDate()
        self.until_date = self.calendarWidget.selectedDate()

        self.pushButton_Go.pressed.connect(self.go)
        self.calendarWidget.selectionChanged.connect(self.new_date_selection)


    
    def go(self):
        #print('GO!!!!!!!!!!!!!!')
        self.accept()

    def new_date_selection(self):
        if self.calendarWidget.selectedDate() < self.from_date:
            self.from_date = self.calendarWidget.selectedDate()
        
        elif self.calendarWidget.selectedDate() > self.until_date:
            self.until_date = self.calendarWidget.selectedDate()

        elif self.distance(self.calendarWidget.selectedDate(), self.from_date) < self.distance(self.calendarWidget.selectedDate(), self.until_date):
            self.from_date = self.calendarWidget.selectedDate()
        
        else:
            self.until_date = self.calendarWidget.selectedDate()

        self.lineEdit_From.setText(self.from_date.toString(QtCore.Qt.DefaultLocaleShortDate))
        self.lineEdit_Until.setText(self.until_date.toString(QtCore.Qt.DefaultLocaleShortDate))
        self.calendarWidget.from_date = self.from_date
        self.calendarWidget.until_date = self.until_date

        self.calendarWidget.updateCells()

    def distance(self, a_date, another_date):
        return abs(a_date.toJulianDay() - another_date.toJulianDay())

    def message(self, text):
        msgBox = QtGui.QMessageBox(parent=self)
        msgBox.setText(text)
        msgBox.exec_()
        
    def message_with_cancel_choice(self, text, informative_text, default_button):
        msgBox = QtGui.QMessageBox(parent=self)
        msgBox.setText(text)
        msgBox.setInformativeText(informative_text)
        msgBox.setStandardButtons(QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Ok)
        msgBox.setDefaultButton(default_button)
        return msgBox.exec_()
