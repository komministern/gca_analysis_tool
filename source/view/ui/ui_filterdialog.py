# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_filterdialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ...view.mainwindow.myplaintextedit import MyPlainTextEdit


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(809, 525)
        Dialog.setMinimumSize(QSize(0, 0))
        Dialog.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_4 = QGridLayout(Dialog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_FilterName = QLineEdit(self.groupBox_3)
        self.lineEdit_FilterName.setObjectName(u"lineEdit_FilterName")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_FilterName.sizePolicy().hasHeightForWidth())
        self.lineEdit_FilterName.setSizePolicy(sizePolicy)
        self.lineEdit_FilterName.setMinimumSize(QSize(0, 0))
        self.lineEdit_FilterName.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.lineEdit_FilterName, 0, 0, 1, 1)

        self.pushButton_Cancel = QPushButton(self.groupBox_3)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_Cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_Cancel.setSizePolicy(sizePolicy1)
        self.pushButton_Cancel.setMinimumSize(QSize(0, 0))
        self.pushButton_Cancel.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Cancel.setAutoDefault(False)

        self.gridLayout_3.addWidget(self.pushButton_Cancel, 0, 1, 1, 1)

        self.pushButton_Save = QPushButton(self.groupBox_3)
        self.pushButton_Save.setObjectName(u"pushButton_Save")
        sizePolicy1.setHeightForWidth(self.pushButton_Save.sizePolicy().hasHeightForWidth())
        self.pushButton_Save.setSizePolicy(sizePolicy1)
        self.pushButton_Save.setMinimumSize(QSize(0, 0))
        self.pushButton_Save.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Save.setAutoDefault(False)

        self.gridLayout_3.addWidget(self.pushButton_Save, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 3)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plainTextEdit_PossibleContent = MyPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_PossibleContent.setObjectName(u"plainTextEdit_PossibleContent")
        self.plainTextEdit_PossibleContent.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_PossibleContent.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.gridLayout_2.addWidget(self.plainTextEdit_PossibleContent, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 4, 1)

        self.verticalSpacer = QSpacerItem(10, 97, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_FilterState = QComboBox(self.groupBox)
        self.comboBox_FilterState.setObjectName(u"comboBox_FilterState")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_FilterState.sizePolicy().hasHeightForWidth())
        self.comboBox_FilterState.setSizePolicy(sizePolicy2)
        self.comboBox_FilterState.setMinimumSize(QSize(0, 0))
        self.comboBox_FilterState.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.comboBox_FilterState, 0, 0, 1, 1)

        self.plainTextEdit_FilterContent = MyPlainTextEdit(self.groupBox)
        self.plainTextEdit_FilterContent.setObjectName(u"plainTextEdit_FilterContent")
        self.plainTextEdit_FilterContent.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_FilterContent.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.gridLayout.addWidget(self.plainTextEdit_FilterContent, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 1, 2, 4, 1)

        self.pushButton_AddContent = QPushButton(Dialog)
        self.pushButton_AddContent.setObjectName(u"pushButton_AddContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_AddContent.sizePolicy().hasHeightForWidth())
        self.pushButton_AddContent.setSizePolicy(sizePolicy3)
        self.pushButton_AddContent.setMinimumSize(QSize(0, 0))
        self.pushButton_AddContent.setMaximumSize(QSize(84, 16777215))

        self.gridLayout_4.addWidget(self.pushButton_AddContent, 2, 1, 1, 1, Qt.AlignHCenter)

        self.pushButton_RemoveContent = QPushButton(Dialog)
        self.pushButton_RemoveContent.setObjectName(u"pushButton_RemoveContent")
        sizePolicy3.setHeightForWidth(self.pushButton_RemoveContent.sizePolicy().hasHeightForWidth())
        self.pushButton_RemoveContent.setSizePolicy(sizePolicy3)
        self.pushButton_RemoveContent.setMinimumSize(QSize(0, 0))
        self.pushButton_RemoveContent.setMaximumSize(QSize(84, 16777215))

        self.gridLayout_4.addWidget(self.pushButton_RemoveContent, 3, 1, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(10, 97, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 4, 1, 1, 1)


        self.retranslateUi(Dialog)

        self.pushButton_Cancel.setDefault(False)
        self.pushButton_Save.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Edit history log filter", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Filter Name", None))
#if QT_CONFIG(statustip)
        self.lineEdit_FilterName.setStatusTip(QCoreApplication.translate("Dialog", u"Name of the current filter", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.pushButton_Cancel.setStatusTip(QCoreApplication.translate("Dialog", u"Cancel editing discarding possible changes", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_Cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
#if QT_CONFIG(statustip)
        self.pushButton_Save.setStatusTip(QCoreApplication.translate("Dialog", u"Save current filter settings", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_Save.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Identifiers", None))
#if QT_CONFIG(statustip)
        self.plainTextEdit_PossibleContent.setStatusTip(QCoreApplication.translate("Dialog", u"Possible codes used to filter history log content", None))
#endif // QT_CONFIG(statustip)
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Filter Content", None))
#if QT_CONFIG(statustip)
        self.comboBox_FilterState.setStatusTip(QCoreApplication.translate("Dialog", u"Choose suppressing or highlighting function", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.plainTextEdit_FilterContent.setStatusTip(QCoreApplication.translate("Dialog", u"Currently picked codes for filter", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.pushButton_AddContent.setStatusTip(QCoreApplication.translate("Dialog", u"Add code to filter", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_AddContent.setText(QCoreApplication.translate("Dialog", u">>", None))
#if QT_CONFIG(statustip)
        self.pushButton_RemoveContent.setStatusTip(QCoreApplication.translate("Dialog", u"Remove code from filter", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_RemoveContent.setText(QCoreApplication.translate("Dialog", u"<<", None))
    # retranslateUi

