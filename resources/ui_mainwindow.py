# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created: Wed Aug 15 21:46:08 2018
#      by: pyside2-uic  running on PySide2 5.9.0a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1168, 728)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_ActiveSite = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_ActiveSite.setMinimumSize(QtCore.QSize(180, 30))
        self.comboBox_ActiveSite.setMaximumSize(QtCore.QSize(180, 30))
        self.comboBox_ActiveSite.setToolTip("")
        self.comboBox_ActiveSite.setObjectName("comboBox_ActiveSite")
        self.gridLayout_2.addWidget(self.comboBox_ActiveSite, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_4, 0, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(330, 403))
        self.groupBox_3.setMaximumSize(QtCore.QSize(330, 435))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.calendarWidget = MyCalendarWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMinimumSize(QtCore.QSize(304, 240))
        self.calendarWidget.setMaximumSize(QtCore.QSize(304, 240))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_6.addWidget(self.calendarWidget, 1, 0, 1, 3)
        self.pushButton_FirstEntry = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_FirstEntry.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_FirstEntry.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_FirstEntry.setToolTip("")
        self.pushButton_FirstEntry.setObjectName("pushButton_FirstEntry")
        self.gridLayout_6.addWidget(self.pushButton_FirstEntry, 2, 0, 1, 1)
        self.pushButton_LastEntry = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_LastEntry.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_LastEntry.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_LastEntry.setToolTip("")
        self.pushButton_LastEntry.setObjectName("pushButton_LastEntry")
        self.gridLayout_6.addWidget(self.pushButton_LastEntry, 2, 1, 1, 1)
        self.pushButton_Today = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_Today.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_Today.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_Today.setToolTip("")
        self.pushButton_Today.setObjectName("pushButton_Today")
        self.gridLayout_6.addWidget(self.pushButton_Today, 2, 2, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 79))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 79))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox_Coloring = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_Coloring.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_Coloring.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox_Coloring.setToolTip("")
        self.comboBox_Coloring.setObjectName("comboBox_Coloring")
        self.gridLayout_4.addWidget(self.comboBox_Coloring, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_5, 0, 0, 1, 3)
        self.gridLayout_7.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.tabWidget_TextFields = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_TextFields.setObjectName("tabWidget_TextFields")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_HistoryLog = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_HistoryLog.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_HistoryLog.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_HistoryLog.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser_HistoryLog.setObjectName("textBrowser_HistoryLog")
        self.gridLayout.addWidget(self.textBrowser_HistoryLog, 0, 0, 1, 1)
        self.tabWidget_TextFields.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.plainTextEdit_Comment = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_Comment.setObjectName("plainTextEdit_Comment")
        self.gridLayout_10.addWidget(self.plainTextEdit_Comment, 0, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pushButton_DeleteComment = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_DeleteComment.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_DeleteComment.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_DeleteComment.setObjectName("pushButton_DeleteComment")
        self.gridLayout_9.addWidget(self.pushButton_DeleteComment, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton_PreviousComment = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_PreviousComment.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_PreviousComment.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_PreviousComment.setObjectName("pushButton_PreviousComment")
        self.gridLayout_9.addWidget(self.pushButton_PreviousComment, 0, 2, 1, 1)
        self.pushButton_NextComment = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_NextComment.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_NextComment.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_NextComment.setObjectName("pushButton_NextComment")
        self.gridLayout_9.addWidget(self.pushButton_NextComment, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem1, 0, 4, 1, 1)
        self.pushButton_SaveComment = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_SaveComment.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_SaveComment.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_SaveComment.setObjectName("pushButton_SaveComment")
        self.gridLayout_9.addWidget(self.pushButton_SaveComment, 0, 5, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.tabWidget_TextFields.addTab(self.tab_2, "")
        self.gridLayout_7.addWidget(self.tabWidget_TextFields, 1, 1, 4, 1)
        self.tabWidget_Search = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_Search.setMinimumSize(QtCore.QSize(330, 130))
        self.tabWidget_Search.setMaximumSize(QtCore.QSize(330, 130))
        self.tabWidget_Search.setObjectName("tabWidget_Search")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.plainTextEdit_StringSearch = MyStringSearchPlainTextEdit(self.tab_3)
        self.plainTextEdit_StringSearch.setMinimumSize(QtCore.QSize(0, 30))
        self.plainTextEdit_StringSearch.setMaximumSize(QtCore.QSize(16777215, 30))
        self.plainTextEdit_StringSearch.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_StringSearch.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_StringSearch.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_StringSearch.setPlainText("")
        self.plainTextEdit_StringSearch.setObjectName("plainTextEdit_StringSearch")
        self.gridLayout_5.addWidget(self.plainTextEdit_StringSearch, 0, 0, 1, 2)
        self.pushButton_CommitStringSearch = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_CommitStringSearch.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_CommitStringSearch.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_CommitStringSearch.setToolTip("")
        self.pushButton_CommitStringSearch.setObjectName("pushButton_CommitStringSearch")
        self.gridLayout_5.addWidget(self.pushButton_CommitStringSearch, 0, 2, 1, 1)
        self.pushButton_PreviousSearch = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_PreviousSearch.setEnabled(True)
        self.pushButton_PreviousSearch.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_PreviousSearch.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_PreviousSearch.setToolTip("")
        self.pushButton_PreviousSearch.setObjectName("pushButton_PreviousSearch")
        self.gridLayout_5.addWidget(self.pushButton_PreviousSearch, 1, 0, 1, 1)
        self.pushButton_NextSearch = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_NextSearch.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_NextSearch.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_NextSearch.setToolTip("")
        self.pushButton_NextSearch.setObjectName("pushButton_NextSearch")
        self.gridLayout_5.addWidget(self.pushButton_NextSearch, 1, 1, 1, 1)
        self.pushButton_ResetStringSearch = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_ResetStringSearch.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_ResetStringSearch.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_ResetStringSearch.setToolTip("")
        self.pushButton_ResetStringSearch.setObjectName("pushButton_ResetStringSearch")
        self.gridLayout_5.addWidget(self.pushButton_ResetStringSearch, 1, 2, 1, 1)
        self.tabWidget_Search.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_ChooseFilter = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_ChooseFilter.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_ChooseFilter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox_ChooseFilter.setObjectName("comboBox_ChooseFilter")
        self.gridLayout_3.addWidget(self.comboBox_ChooseFilter, 0, 0, 1, 3)
        self.pushButton_NewFilter = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_NewFilter.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_NewFilter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_NewFilter.setObjectName("pushButton_NewFilter")
        self.gridLayout_3.addWidget(self.pushButton_NewFilter, 1, 0, 1, 1)
        self.pushButton_EditFilter = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_EditFilter.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_EditFilter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_EditFilter.setObjectName("pushButton_EditFilter")
        self.gridLayout_3.addWidget(self.pushButton_EditFilter, 1, 1, 1, 1)
        self.pushButton_DeleteFilter = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_DeleteFilter.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_DeleteFilter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_DeleteFilter.setObjectName("pushButton_DeleteFilter")
        self.gridLayout_3.addWidget(self.pushButton_DeleteFilter, 1, 2, 1, 1)
        self.tabWidget_Search.addTab(self.tab_4, "")
        self.gridLayout_7.addWidget(self.tabWidget_Search, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMaximumSize(QtCore.QSize(331, 16777215))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_7.addWidget(self.progressBar, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(17, 139, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem2, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1168, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_TextFields.setCurrentIndex(0)
        self.tabWidget_Search.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "GCA Analysis Tool", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Active Site", None, -1))
        self.comboBox_ActiveSite.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Choose active site", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Calendar", None, -1))
        self.pushButton_FirstEntry.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Focus calendar on the  first recorded date in the history log (excluding ignored dates)", None, -1))
        self.pushButton_FirstEntry.setText(QtWidgets.QApplication.translate("MainWindow", "First Date", None, -1))
        self.pushButton_LastEntry.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Focus calendar on the last recorded date in the history log (excluding ignored dates)", None, -1))
        self.pushButton_LastEntry.setText(QtWidgets.QApplication.translate("MainWindow", "Last Date", None, -1))
        self.pushButton_Today.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Focus calendar on the active date", None, -1))
        self.pushButton_Today.setText(QtWidgets.QApplication.translate("MainWindow", "Active Date", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "Coloring Scheme", None, -1))
        self.comboBox_Coloring.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Choose different coloring rules for the calendar", None, -1))
        self.tabWidget_TextFields.setTabText(self.tabWidget_TextFields.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "History Log", None, -1))
        self.groupBox_7.setTitle(QtWidgets.QApplication.translate("MainWindow", "Notes", None, -1))
        self.pushButton_DeleteComment.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Delete this comment from database", None, -1))
        self.pushButton_DeleteComment.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.pushButton_PreviousComment.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Jump to previous comment", None, -1))
        self.pushButton_PreviousComment.setText(QtWidgets.QApplication.translate("MainWindow", "Previous", None, -1))
        self.pushButton_NextComment.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Jump to next comment", None, -1))
        self.pushButton_NextComment.setText(QtWidgets.QApplication.translate("MainWindow", "Next", None, -1))
        self.pushButton_SaveComment.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Save this comment to database", None, -1))
        self.pushButton_SaveComment.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.tabWidget_TextFields.setTabText(self.tabWidget_TextFields.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Notes", None, -1))
        self.pushButton_CommitStringSearch.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Commit search", None, -1))
        self.pushButton_CommitStringSearch.setText(QtWidgets.QApplication.translate("MainWindow", "Search", None, -1))
        self.pushButton_PreviousSearch.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Focus calendar on the previous date in which history log contains search string", None, -1))
        self.pushButton_PreviousSearch.setText(QtWidgets.QApplication.translate("MainWindow", "Previous", None, -1))
        self.pushButton_NextSearch.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Focus calendar on the next date in which history log contains search string", None, -1))
        self.pushButton_NextSearch.setText(QtWidgets.QApplication.translate("MainWindow", "Next", None, -1))
        self.pushButton_ResetStringSearch.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Clear search string", None, -1))
        self.pushButton_ResetStringSearch.setText(QtWidgets.QApplication.translate("MainWindow", "Clear", None, -1))
        self.tabWidget_Search.setTabText(self.tabWidget_Search.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", "String Search", None, -1))
        self.comboBox_ChooseFilter.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Choose history log filter", None, -1))
        self.pushButton_NewFilter.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Create a new filter", None, -1))
        self.pushButton_NewFilter.setText(QtWidgets.QApplication.translate("MainWindow", "New", None, -1))
        self.pushButton_EditFilter.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Edit currently chosen filter", None, -1))
        self.pushButton_EditFilter.setText(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.pushButton_DeleteFilter.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Delete currently chosen filter", None, -1))
        self.pushButton_DeleteFilter.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.tabWidget_Search.setTabText(self.tabWidget_Search.indexOf(self.tab_4), QtWidgets.QApplication.translate("MainWindow", "Filter", None, -1))
        self.progressBar.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Indicates progress of file I/O operations, which can be lengthy at times", None, -1))


from .mycalendarwidget import MyCalendarWidget
from .mystringsearchplaintextedit import MyStringSearchPlainTextEdit