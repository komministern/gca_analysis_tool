# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_filterdialog.ui'
#
# Created: Sun Jun  3 18:52:14 2018
#      by: pyside2-uic  running on PySide2 5.9.0a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(698, 349)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_FilterName = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_FilterName.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_FilterName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_FilterName.setObjectName("lineEdit_FilterName")
        self.gridLayout_3.addWidget(self.lineEdit_FilterName, 0, 0, 1, 1)
        self.pushButton_Cancel = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_Cancel.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_Cancel.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Cancel.setAutoDefault(False)
        self.pushButton_Cancel.setDefault(False)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout_3.addWidget(self.pushButton_Cancel, 0, 1, 1, 1)
        self.pushButton_Save = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_Save.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_Save.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Save.setAutoDefault(False)
        self.pushButton_Save.setDefault(True)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.gridLayout_3.addWidget(self.pushButton_Save, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 3)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit_PossibleContent = MyPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_PossibleContent.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit_PossibleContent.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_PossibleContent.setObjectName("plainTextEdit_PossibleContent")
        self.gridLayout_2.addWidget(self.plainTextEdit_PossibleContent, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 4, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 97, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_FilterState = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_FilterState.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_FilterState.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox_FilterState.setObjectName("comboBox_FilterState")
        self.gridLayout.addWidget(self.comboBox_FilterState, 0, 0, 1, 1)
        self.plainTextEdit_FilterContent = MyPlainTextEdit(self.groupBox)
        self.plainTextEdit_FilterContent.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit_FilterContent.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_FilterContent.setObjectName("plainTextEdit_FilterContent")
        self.gridLayout.addWidget(self.plainTextEdit_FilterContent, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 2, 4, 1)
        self.pushButton_AddContent = QtWidgets.QPushButton(Dialog)
        self.pushButton_AddContent.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_AddContent.setMaximumSize(QtCore.QSize(31, 30))
        self.pushButton_AddContent.setObjectName("pushButton_AddContent")
        self.gridLayout_4.addWidget(self.pushButton_AddContent, 2, 1, 1, 1)
        self.pushButton_RemoveContent = QtWidgets.QPushButton(Dialog)
        self.pushButton_RemoveContent.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_RemoveContent.setMaximumSize(QtCore.QSize(31, 30))
        self.pushButton_RemoveContent.setObjectName("pushButton_RemoveContent")
        self.gridLayout_4.addWidget(self.pushButton_RemoveContent, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 97, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Edit history log filter", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("Dialog", "Filter Name", None, -1))
        self.lineEdit_FilterName.setStatusTip(QtWidgets.QApplication.translate("Dialog", "Name of the current filter", None, -1))
        self.pushButton_Cancel.setStatusTip(QtWidgets.QApplication.translate("Dialog", "Cancel editing discarding possible changes", None, -1))
        self.pushButton_Cancel.setText(QtWidgets.QApplication.translate("Dialog", "Cancel", None, -1))
        self.pushButton_Save.setStatusTip(QtWidgets.QApplication.translate("Dialog", "Save current filter settings", None, -1))
        self.pushButton_Save.setText(QtWidgets.QApplication.translate("Dialog", "Save", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Dialog", "Identifiers", None, -1))
        self.plainTextEdit_PossibleContent.setStatusTip(QtWidgets.QApplication.translate("Dialog", "Possible codes used to filter history log content", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Dialog", "Filter Content", None, -1))
        self.comboBox_FilterState.setStatusTip(QtWidgets.QApplication.translate("Dialog", "Choose suppressing or highlighting function", None, -1))
        self.plainTextEdit_FilterContent.setStatusTip(QtWidgets.QApplication.translate("Dialog", "Currently picked codes for filter", None, -1))
        self.pushButton_AddContent.setStatusTip(QtWidgets.QApplication.translate("Dialog", "Add code to filter", None, -1))
        self.pushButton_AddContent.setText(QtWidgets.QApplication.translate("Dialog", ">>", None, -1))
        self.pushButton_RemoveContent.setStatusTip(QtWidgets.QApplication.translate("Dialog", "Remove code from filter", None, -1))
        self.pushButton_RemoveContent.setText(QtWidgets.QApplication.translate("Dialog", "<<", None, -1))

from myplaintextedit import MyPlainTextEdit
