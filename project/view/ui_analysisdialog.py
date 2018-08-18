# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_analysisdialog.ui'
#
# Created: Sat Aug 18 12:40:04 2018
#      by: pyside2-uic  running on PySide2 5.9.0a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(330, 275)
        Dialog.setMaximumSize(QtCore.QSize(330, 275))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.calendarWidget = MyOtherCalendarWidget(Dialog)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.lineEdit_From = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_From.setReadOnly(True)
        self.lineEdit_From.setObjectName("lineEdit_From")
        self.gridLayout.addWidget(self.lineEdit_From, 2, 0, 1, 1)
        self.lineEdit_Until = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Until.setReadOnly(True)
        self.lineEdit_Until.setObjectName("lineEdit_Until")
        self.gridLayout.addWidget(self.lineEdit_Until, 2, 1, 1, 1)
        self.pushButton_Go = QtWidgets.QPushButton(Dialog)
        self.pushButton_Go.setObjectName("pushButton_Go")
        self.gridLayout.addWidget(self.pushButton_Go, 3, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Analysis", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "From:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "To:", None, -1))
        self.pushButton_Go.setText(QtWidgets.QApplication.translate("Dialog", "Analyze", None, -1))

from .myothercalendarwidget import MyOtherCalendarWidget
