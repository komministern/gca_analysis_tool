# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filterwidget.ui'
#
# Created: Wed Apr 12 11:40:26 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(490, 294)
        self.gridLayout_3 = QtGui.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_FilterName = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_FilterName.setObjectName("lineEdit_FilterName")
        self.gridLayout.addWidget(self.lineEdit_FilterName, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 6)
        spacerItem = QtGui.QSpacerItem(20, 73, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 73, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 2, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_FilterState = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_FilterState.setObjectName("comboBox_FilterState")
        self.gridLayout_2.addWidget(self.comboBox_FilterState, 0, 0, 1, 1)
        self.plainTextEdit_FilterContent = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_FilterContent.setObjectName("plainTextEdit_FilterContent")
        self.gridLayout_2.addWidget(self.plainTextEdit_FilterContent, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 4, 3, 2)
        self.comboBox_PossibleIdentifiers = QtGui.QComboBox(Form)
        self.comboBox_PossibleIdentifiers.setMinimumSize(QtCore.QSize(180, 0))
        self.comboBox_PossibleIdentifiers.setObjectName("comboBox_PossibleIdentifiers")
        self.gridLayout_3.addWidget(self.comboBox_PossibleIdentifiers, 2, 0, 1, 2)
        self.pushButton_RemoveContent = QtGui.QPushButton(Form)
        self.pushButton_RemoveContent.setMaximumSize(QtCore.QSize(31, 16777215))
        self.pushButton_RemoveContent.setObjectName("pushButton_RemoveContent")
        self.gridLayout_3.addWidget(self.pushButton_RemoveContent, 2, 2, 1, 1)
        self.pushButton_AddContent = QtGui.QPushButton(Form)
        self.pushButton_AddContent.setMaximumSize(QtCore.QSize(31, 16777215))
        self.pushButton_AddContent.setObjectName("pushButton_AddContent")
        self.gridLayout_3.addWidget(self.pushButton_AddContent, 2, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 74, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 3, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 74, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 3, 2, 1, 1)
        self.pushButton_Cancel = QtGui.QPushButton(Form)
        self.pushButton_Cancel.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout_3.addWidget(self.pushButton_Cancel, 4, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(307, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 4, 1, 1, 4)
        self.pushButton_Save = QtGui.QPushButton(Form)
        self.pushButton_Save.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.gridLayout_3.addWidget(self.pushButton_Save, 4, 5, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Filter Name", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_RemoveContent.setText(QtGui.QApplication.translate("Form", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_AddContent.setText(QtGui.QApplication.translate("Form", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cancel.setText(QtGui.QApplication.translate("Form", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Save.setText(QtGui.QApplication.translate("Form", "Save", None, QtGui.QApplication.UnicodeUTF8))

