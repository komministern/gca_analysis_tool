# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ...view.mainwindow.mystringsearchplaintextedit import MyStringSearchPlainTextEdit
from ...view.mainwindow.mycalendarwidget import MyCalendarWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1069, 655)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox_ActiveSite = QComboBox(self.groupBox_4)
        self.comboBox_ActiveSite.setObjectName(u"comboBox_ActiveSite")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_ActiveSite.sizePolicy().hasHeightForWidth())
        self.comboBox_ActiveSite.setSizePolicy(sizePolicy2)
        self.comboBox_ActiveSite.setMinimumSize(QSize(250, 0))
        self.comboBox_ActiveSite.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.comboBox_ActiveSite, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_4, 0, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.groupBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_FirstDate = QPushButton(self.groupBox_3)
        self.pushButton_FirstDate.setObjectName(u"pushButton_FirstDate")
        sizePolicy1.setHeightForWidth(self.pushButton_FirstDate.sizePolicy().hasHeightForWidth())
        self.pushButton_FirstDate.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.pushButton_FirstDate, 2, 0, 1, 1)

        self.pushButton_LastDate = QPushButton(self.groupBox_3)
        self.pushButton_LastDate.setObjectName(u"pushButton_LastDate")
        sizePolicy1.setHeightForWidth(self.pushButton_LastDate.sizePolicy().hasHeightForWidth())
        self.pushButton_LastDate.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.pushButton_LastDate, 2, 2, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.groupBox_5.setMinimumSize(QSize(0, 0))
        self.groupBox_5.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.comboBox_Coloring = QComboBox(self.groupBox_5)
        self.comboBox_Coloring.setObjectName(u"comboBox_Coloring")
        sizePolicy1.setHeightForWidth(self.comboBox_Coloring.sizePolicy().hasHeightForWidth())
        self.comboBox_Coloring.setSizePolicy(sizePolicy1)
        self.comboBox_Coloring.setMinimumSize(QSize(0, 0))
        self.comboBox_Coloring.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.comboBox_Coloring, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_5, 0, 0, 1, 3)

        self.calendarWidget = MyCalendarWidget(self.groupBox_3)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setFirstDayOfWeek(Qt.Monday)
        self.calendarWidget.setSelectionMode(QCalendarWidget.SingleSelection)

        self.gridLayout_6.addWidget(self.calendarWidget, 1, 0, 1, 3)

        self.pushButton_ActiveDate = QPushButton(self.groupBox_3)
        self.pushButton_ActiveDate.setObjectName(u"pushButton_ActiveDate")
        sizePolicy1.setHeightForWidth(self.pushButton_ActiveDate.sizePolicy().hasHeightForWidth())
        self.pushButton_ActiveDate.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.pushButton_ActiveDate, 2, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.tabWidget_TextFields = QTabWidget(self.centralwidget)
        self.tabWidget_TextFields.setObjectName(u"tabWidget_TextFields")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textBrowser_HistoryLog = QTextBrowser(self.tab)
        self.textBrowser_HistoryLog.setObjectName(u"textBrowser_HistoryLog")
        self.textBrowser_HistoryLog.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textBrowser_HistoryLog.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textBrowser_HistoryLog.setLineWrapMode(QTextEdit.NoWrap)

        self.gridLayout.addWidget(self.textBrowser_HistoryLog, 0, 0, 1, 1)

        self.tabWidget_TextFields.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_10 = QGridLayout(self.tab_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.plainTextEdit_Comment = QPlainTextEdit(self.tab_2)
        self.plainTextEdit_Comment.setObjectName(u"plainTextEdit_Comment")

        self.gridLayout_10.addWidget(self.plainTextEdit_Comment, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy1.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy1)
        self.gridLayout_9 = QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_DeleteComment = QPushButton(self.groupBox_7)
        self.pushButton_DeleteComment.setObjectName(u"pushButton_DeleteComment")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_DeleteComment.sizePolicy().hasHeightForWidth())
        self.pushButton_DeleteComment.setSizePolicy(sizePolicy4)
        self.pushButton_DeleteComment.setMinimumSize(QSize(0, 0))
        self.pushButton_DeleteComment.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.pushButton_DeleteComment, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.pushButton_PreviousComment = QPushButton(self.groupBox_7)
        self.pushButton_PreviousComment.setObjectName(u"pushButton_PreviousComment")
        sizePolicy4.setHeightForWidth(self.pushButton_PreviousComment.sizePolicy().hasHeightForWidth())
        self.pushButton_PreviousComment.setSizePolicy(sizePolicy4)
        self.pushButton_PreviousComment.setMinimumSize(QSize(0, 0))
        self.pushButton_PreviousComment.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.pushButton_PreviousComment, 0, 2, 1, 1)

        self.pushButton_NextComment = QPushButton(self.groupBox_7)
        self.pushButton_NextComment.setObjectName(u"pushButton_NextComment")
        sizePolicy4.setHeightForWidth(self.pushButton_NextComment.sizePolicy().hasHeightForWidth())
        self.pushButton_NextComment.setSizePolicy(sizePolicy4)
        self.pushButton_NextComment.setMinimumSize(QSize(0, 0))
        self.pushButton_NextComment.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.pushButton_NextComment, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.pushButton_SaveComment = QPushButton(self.groupBox_7)
        self.pushButton_SaveComment.setObjectName(u"pushButton_SaveComment")
        sizePolicy4.setHeightForWidth(self.pushButton_SaveComment.sizePolicy().hasHeightForWidth())
        self.pushButton_SaveComment.setSizePolicy(sizePolicy4)
        self.pushButton_SaveComment.setMinimumSize(QSize(0, 0))
        self.pushButton_SaveComment.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.pushButton_SaveComment, 0, 5, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_7, 1, 0, 1, 1)

        self.tabWidget_TextFields.addTab(self.tab_2, "")

        self.gridLayout_7.addWidget(self.tabWidget_TextFields, 1, 1, 4, 1)

        self.tabWidget_Search = QTabWidget(self.centralwidget)
        self.tabWidget_Search.setObjectName(u"tabWidget_Search")
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tabWidget_Search.sizePolicy().hasHeightForWidth())
        self.tabWidget_Search.setSizePolicy(sizePolicy5)
        self.tabWidget_Search.setMinimumSize(QSize(0, 0))
        self.tabWidget_Search.setMaximumSize(QSize(16777215, 16777215))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.plainTextEdit_StringSearch = MyStringSearchPlainTextEdit(self.tab_3)
        self.plainTextEdit_StringSearch.setObjectName(u"plainTextEdit_StringSearch")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.plainTextEdit_StringSearch.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_StringSearch.setSizePolicy(sizePolicy6)
        self.plainTextEdit_StringSearch.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_StringSearch.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_StringSearch.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_StringSearch.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_StringSearch.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.gridLayout_5.addWidget(self.plainTextEdit_StringSearch, 0, 0, 1, 2)

        self.pushButton_CommitStringSearch = QPushButton(self.tab_3)
        self.pushButton_CommitStringSearch.setObjectName(u"pushButton_CommitStringSearch")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton_CommitStringSearch.sizePolicy().hasHeightForWidth())
        self.pushButton_CommitStringSearch.setSizePolicy(sizePolicy7)
        self.pushButton_CommitStringSearch.setMinimumSize(QSize(0, 0))
        self.pushButton_CommitStringSearch.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.pushButton_CommitStringSearch, 0, 2, 1, 1)

        self.pushButton_PreviousSearch = QPushButton(self.tab_3)
        self.pushButton_PreviousSearch.setObjectName(u"pushButton_PreviousSearch")
        self.pushButton_PreviousSearch.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.pushButton_PreviousSearch.sizePolicy().hasHeightForWidth())
        self.pushButton_PreviousSearch.setSizePolicy(sizePolicy7)
        self.pushButton_PreviousSearch.setMinimumSize(QSize(0, 0))
        self.pushButton_PreviousSearch.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.pushButton_PreviousSearch, 1, 0, 1, 1)

        self.pushButton_NextSearch = QPushButton(self.tab_3)
        self.pushButton_NextSearch.setObjectName(u"pushButton_NextSearch")
        sizePolicy7.setHeightForWidth(self.pushButton_NextSearch.sizePolicy().hasHeightForWidth())
        self.pushButton_NextSearch.setSizePolicy(sizePolicy7)
        self.pushButton_NextSearch.setMinimumSize(QSize(0, 0))
        self.pushButton_NextSearch.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.pushButton_NextSearch, 1, 1, 1, 1)

        self.pushButton_ResetStringSearch = QPushButton(self.tab_3)
        self.pushButton_ResetStringSearch.setObjectName(u"pushButton_ResetStringSearch")
        sizePolicy7.setHeightForWidth(self.pushButton_ResetStringSearch.sizePolicy().hasHeightForWidth())
        self.pushButton_ResetStringSearch.setSizePolicy(sizePolicy7)
        self.pushButton_ResetStringSearch.setMinimumSize(QSize(0, 0))
        self.pushButton_ResetStringSearch.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.pushButton_ResetStringSearch, 1, 2, 1, 1)

        self.tabWidget_Search.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comboBox_ChooseFilter = QComboBox(self.tab_4)
        self.comboBox_ChooseFilter.setObjectName(u"comboBox_ChooseFilter")
        sizePolicy7.setHeightForWidth(self.comboBox_ChooseFilter.sizePolicy().hasHeightForWidth())
        self.comboBox_ChooseFilter.setSizePolicy(sizePolicy7)
        self.comboBox_ChooseFilter.setMinimumSize(QSize(0, 0))
        self.comboBox_ChooseFilter.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.comboBox_ChooseFilter, 0, 0, 1, 3)

        self.pushButton_NewFilter = QPushButton(self.tab_4)
        self.pushButton_NewFilter.setObjectName(u"pushButton_NewFilter")
        sizePolicy7.setHeightForWidth(self.pushButton_NewFilter.sizePolicy().hasHeightForWidth())
        self.pushButton_NewFilter.setSizePolicy(sizePolicy7)
        self.pushButton_NewFilter.setMinimumSize(QSize(0, 0))
        self.pushButton_NewFilter.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_NewFilter, 1, 0, 1, 1)

        self.pushButton_EditFilter = QPushButton(self.tab_4)
        self.pushButton_EditFilter.setObjectName(u"pushButton_EditFilter")
        sizePolicy7.setHeightForWidth(self.pushButton_EditFilter.sizePolicy().hasHeightForWidth())
        self.pushButton_EditFilter.setSizePolicy(sizePolicy7)
        self.pushButton_EditFilter.setMinimumSize(QSize(0, 0))
        self.pushButton_EditFilter.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_EditFilter, 1, 1, 1, 1)

        self.pushButton_DeleteFilter = QPushButton(self.tab_4)
        self.pushButton_DeleteFilter.setObjectName(u"pushButton_DeleteFilter")
        sizePolicy7.setHeightForWidth(self.pushButton_DeleteFilter.sizePolicy().hasHeightForWidth())
        self.pushButton_DeleteFilter.setSizePolicy(sizePolicy7)
        self.pushButton_DeleteFilter.setMinimumSize(QSize(0, 0))
        self.pushButton_DeleteFilter.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_DeleteFilter, 1, 2, 1, 1)

        self.tabWidget_Search.addTab(self.tab_4, "")

        self.gridLayout_7.addWidget(self.tabWidget_Search, 2, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.gridLayout_7.addWidget(self.progressBar, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(0, 1390, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1069, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_TextFields.setCurrentIndex(0)
        self.tabWidget_Search.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GCA Analysis Tool", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Active Site", None))
#if QT_CONFIG(tooltip)
        self.comboBox_ActiveSite.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBox_ActiveSite.setStatusTip(QCoreApplication.translate("MainWindow", u"Select active site", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Calendar", None))
#if QT_CONFIG(statustip)
        self.pushButton_FirstDate.setStatusTip(QCoreApplication.translate("MainWindow", u"Select the date of the first recorded history log for this system", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_FirstDate.setText(QCoreApplication.translate("MainWindow", u"First", None))
#if QT_CONFIG(statustip)
        self.pushButton_LastDate.setStatusTip(QCoreApplication.translate("MainWindow", u"Select the date of the last recorded history log for this system", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_LastDate.setText(QCoreApplication.translate("MainWindow", u"Latest", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Coloring Scheme", None))
#if QT_CONFIG(tooltip)
        self.comboBox_Coloring.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBox_Coloring.setStatusTip(QCoreApplication.translate("MainWindow", u"Select coloring rules for the calendar", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.calendarWidget.setStatusTip(QCoreApplication.translate("MainWindow", u"Select date of interest", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.pushButton_ActiveDate.setStatusTip(QCoreApplication.translate("MainWindow", u"Show selected date", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_ActiveDate.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.tabWidget_TextFields.setTabText(self.tabWidget_TextFields.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"History Log", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Notes", None))
#if QT_CONFIG(statustip)
        self.pushButton_DeleteComment.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete this comment from database", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_DeleteComment.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(statustip)
        self.pushButton_PreviousComment.setStatusTip(QCoreApplication.translate("MainWindow", u"Jump to previous comment", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_PreviousComment.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
#if QT_CONFIG(statustip)
        self.pushButton_NextComment.setStatusTip(QCoreApplication.translate("MainWindow", u"Jump to next comment", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_NextComment.setText(QCoreApplication.translate("MainWindow", u"Next", None))
#if QT_CONFIG(statustip)
        self.pushButton_SaveComment.setStatusTip(QCoreApplication.translate("MainWindow", u"Save this comment to database", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_SaveComment.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabWidget_TextFields.setTabText(self.tabWidget_TextFields.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Notes", None))
        self.plainTextEdit_StringSearch.setPlainText("")
#if QT_CONFIG(tooltip)
        self.pushButton_CommitStringSearch.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_CommitStringSearch.setStatusTip(QCoreApplication.translate("MainWindow", u"Commit search", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_CommitStringSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
#if QT_CONFIG(tooltip)
        self.pushButton_PreviousSearch.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_PreviousSearch.setStatusTip(QCoreApplication.translate("MainWindow", u"Focus calendar on the previous date in which history log contains search string", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_PreviousSearch.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
#if QT_CONFIG(tooltip)
        self.pushButton_NextSearch.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_NextSearch.setStatusTip(QCoreApplication.translate("MainWindow", u"Focus calendar on the next date in which history log contains search string", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_NextSearch.setText(QCoreApplication.translate("MainWindow", u"Next", None))
#if QT_CONFIG(tooltip)
        self.pushButton_ResetStringSearch.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_ResetStringSearch.setStatusTip(QCoreApplication.translate("MainWindow", u"Clear search string", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_ResetStringSearch.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget_Search.setTabText(self.tabWidget_Search.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"String Search", None))
#if QT_CONFIG(statustip)
        self.comboBox_ChooseFilter.setStatusTip(QCoreApplication.translate("MainWindow", u"Select filter", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.pushButton_NewFilter.setStatusTip(QCoreApplication.translate("MainWindow", u"Create a new filter", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_NewFilter.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(statustip)
        self.pushButton_EditFilter.setStatusTip(QCoreApplication.translate("MainWindow", u"Edit the currently selected filter", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_EditFilter.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
#if QT_CONFIG(statustip)
        self.pushButton_DeleteFilter.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete the currently selected filter", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_DeleteFilter.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.tabWidget_Search.setTabText(self.tabWidget_Search.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Filter", None))
#if QT_CONFIG(statustip)
        self.progressBar.setStatusTip(QCoreApplication.translate("MainWindow", u"Indicates progress of file I/O operations, which can be lengthy at times", None))
#endif // QT_CONFIG(statustip)
    # retranslateUi

