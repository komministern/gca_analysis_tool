# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_filterdialog.ui'
#
# Created: Sun Nov 26 13:55:29 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(698, 349)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout_4 = QtGui.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_FilterName = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_FilterName.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_FilterName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_FilterName.setObjectName("lineEdit_FilterName")
        self.gridLayout_3.addWidget(self.lineEdit_FilterName, 0, 0, 1, 1)
        self.pushButton_Cancel = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_Cancel.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_Cancel.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Cancel.setAutoDefault(False)
        self.pushButton_Cancel.setDefault(False)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout_3.addWidget(self.pushButton_Cancel, 0, 1, 1, 1)
        self.pushButton_Save = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_Save.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_Save.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_Save.setAutoDefault(False)
        self.pushButton_Save.setDefault(True)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.gridLayout_3.addWidget(self.pushButton_Save, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 3)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit_PossibleContent = MyPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_PossibleContent.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit_PossibleContent.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
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
        self.comboBox_FilterState.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_FilterState.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox_FilterState.setObjectName("comboBox_FilterState")
        self.gridLayout.addWidget(self.comboBox_FilterState, 0, 0, 1, 1)
        self.plainTextEdit_FilterContent = MyPlainTextEdit(self.groupBox)
        self.plainTextEdit_FilterContent.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit_FilterContent.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.plainTextEdit_FilterContent.setObjectName("plainTextEdit_FilterContent")
        self.gridLayout.addWidget(self.plainTextEdit_FilterContent, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 2, 4, 1)
        self.pushButton_AddContent = QtGui.QPushButton(Dialog)
        self.pushButton_AddContent.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_AddContent.setMaximumSize(QtCore.QSize(31, 30))
        self.pushButton_AddContent.setObjectName("pushButton_AddContent")
        self.gridLayout_4.addWidget(self.pushButton_AddContent, 2, 1, 1, 1)
        self.pushButton_RemoveContent = QtGui.QPushButton(Dialog)
        self.pushButton_RemoveContent.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_RemoveContent.setMaximumSize(QtCore.QSize(31, 30))
        self.pushButton_RemoveContent.setObjectName("pushButton_RemoveContent")
        self.gridLayout_4.addWidget(self.pushButton_RemoveContent, 3, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 97, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Edit history log filter", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_FilterName.setStatusTip(QtGui.QApplication.translate("Dialog", "Name of the current filter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cancel.setStatusTip(QtGui.QApplication.translate("Dialog", "Cancel editing discarding possible changes", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Save.setStatusTip(QtGui.QApplication.translate("Dialog", "Save current filter settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Save.setText(QtGui.QApplication.translate("Dialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Possible Identifiers", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit_PossibleContent.setStatusTip(QtGui.QApplication.translate("Dialog", "Possible codes used to filter history log content", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Filter Content", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_FilterState.setStatusTip(QtGui.QApplication.translate("Dialog", "Choose suppressing or highlighting function", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit_FilterContent.setStatusTip(QtGui.QApplication.translate("Dialog", "Currently picked codes for filter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_AddContent.setStatusTip(QtGui.QApplication.translate("Dialog", "Add code to filter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_AddContent.setText(QtGui.QApplication.translate("Dialog", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_RemoveContent.setStatusTip(QtGui.QApplication.translate("Dialog", "Remove code from filter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_RemoveContent.setText(QtGui.QApplication.translate("Dialog", "<<", None, QtGui.QApplication.UnicodeUTF8))

from myplaintextedit import MyPlainTextEdit
