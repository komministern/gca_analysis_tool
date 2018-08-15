# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_analysisdialog.ui'
#
# Created: Wed Aug 15 21:46:08 2018
#      by: pyside2-uic  running on PySide2 5.9.0a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(651, 266)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.calendarWidget_From = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget_From.setObjectName("calendarWidget_From")
        self.gridLayout.addWidget(self.calendarWidget_From, 0, 0, 1, 1)
        self.calendarWidget_To = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget_To.setObjectName("calendarWidget_To")
        self.gridLayout.addWidget(self.calendarWidget_To, 0, 1, 1, 1)
        self.pushButton_Go = QtWidgets.QPushButton(Dialog)
        self.pushButton_Go.setObjectName("pushButton_Go")
        self.gridLayout.addWidget(self.pushButton_Go, 1, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Analyze between dates", None, -1))
        self.pushButton_Go.setText(QtWidgets.QApplication.translate("Dialog", "GO", None, -1))

