# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_filterdialog.ui'
#
# Created: Mon Apr 17 22:23:33 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(485, 274)
        Dialog.setMaximumSize(QtCore.QSize(485, 16777215))
        self.gridLayout_4 = QtGui.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_FilterName = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_FilterName.setObjectName("lineEdit_FilterName")
        self.gridLayout_3.addWidget(self.lineEdit_FilterName, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 3)
        self.pushButton_Cancel = QtGui.QPushButton(Dialog)
        self.pushButton_Cancel.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout_4.addWidget(self.pushButton_Cancel, 0, 3, 1, 1)
        self.pushButton_Save = QtGui.QPushButton(Dialog)
        self.pushButton_Save.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.gridLayout_4.addWidget(self.pushButton_Save, 0, 4, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit_PossibleContent = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_PossibleContent.setMinimumSize(QtCore.QSize(192, 0))
        self.plainTextEdit_PossibleContent.setObjectName("plainTextEdit_PossibleContent")
        self.gridLayout_2.addWidget(self.plainTextEdit_PossibleContent, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 4, 1)
        spacerItem = QtGui.QSpacerItem(20, 97, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 1, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_FilterState = QtGui.QComboBox(self.groupBox)
        self.comboBox_FilterState.setObjectName("comboBox_FilterState")
        self.gridLayout.addWidget(self.comboBox_FilterState, 0, 0, 1, 1)
        self.plainTextEdit_FilterContent = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_FilterContent.setMinimumSize(QtCore.QSize(192, 0))
        self.plainTextEdit_FilterContent.setObjectName("plainTextEdit_FilterContent")
        self.gridLayout.addWidget(self.plainTextEdit_FilterContent, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 2, 4, 3)
        self.pushButton_AddContent = QtGui.QPushButton(Dialog)
        self.pushButton_AddContent.setMaximumSize(QtCore.QSize(31, 16777215))
        self.pushButton_AddContent.setObjectName("pushButton_AddContent")
        self.gridLayout_4.addWidget(self.pushButton_AddContent, 2, 1, 1, 1)
        self.pushButton_RemoveContent = QtGui.QPushButton(Dialog)
        self.pushButton_RemoveContent.setMaximumSize(QtCore.QSize(31, 16777215))
        self.pushButton_RemoveContent.setObjectName("pushButton_RemoveContent")
        self.gridLayout_4.addWidget(self.pushButton_RemoveContent, 3, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 97, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "History Log Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "Filter Name", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Save.setText(QtGui.QApplication.translate("Dialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Possible Identifiers", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_AddContent.setText(QtGui.QApplication.translate("Dialog", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_RemoveContent.setText(QtGui.QApplication.translate("Dialog", "<<", None, QtGui.QApplication.UnicodeUTF8))

