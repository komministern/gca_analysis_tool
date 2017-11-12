# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created: Sun Nov 12 20:22:01 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1227, 905)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(330, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(330, 435))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.calendarWidget = MyCalendarWidget(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
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
        self.calendarWidget.setSelectionMode(QtGui.QCalendarWidget.SingleSelection)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_6.addWidget(self.calendarWidget, 1, 0, 1, 3)
        self.pushButton_FirstEntry = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_FirstEntry.setToolTip("")
        self.pushButton_FirstEntry.setObjectName("pushButton_FirstEntry")
        self.gridLayout_6.addWidget(self.pushButton_FirstEntry, 2, 0, 1, 1)
        self.pushButton_LastEntry = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_LastEntry.setToolTip("")
        self.pushButton_LastEntry.setObjectName("pushButton_LastEntry")
        self.gridLayout_6.addWidget(self.pushButton_LastEntry, 2, 1, 1, 1)
        self.pushButton_Today = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_Today.setToolTip("")
        self.pushButton_Today.setObjectName("pushButton_Today")
        self.gridLayout_6.addWidget(self.pushButton_Today, 2, 2, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 79))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 79))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox_Coloring = QtGui.QComboBox(self.groupBox_5)
        self.comboBox_Coloring.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_Coloring.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox_Coloring.setToolTip("")
        self.comboBox_Coloring.setObjectName("comboBox_Coloring")
        self.gridLayout_4.addWidget(self.comboBox_Coloring, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_5, 0, 0, 1, 3)
        self.gridLayout_7.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.tabWidget_TextFields = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_TextFields.setObjectName("tabWidget_TextFields")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_HistoryLog = QtGui.QTextBrowser(self.tab)
        self.textBrowser_HistoryLog.setObjectName("textBrowser_HistoryLog")
        self.gridLayout.addWidget(self.textBrowser_HistoryLog, 0, 0, 1, 1)
        self.tabWidget_TextFields.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.plainTextEdit_Comment = QtGui.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_Comment.setObjectName("plainTextEdit_Comment")
        self.gridLayout_10.addWidget(self.plainTextEdit_Comment, 0, 0, 1, 1)
        self.groupBox_7 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pushButton_DeleteComment = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_DeleteComment.setObjectName("pushButton_DeleteComment")
        self.gridLayout_9.addWidget(self.pushButton_DeleteComment, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton_PreviousComment = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_PreviousComment.setObjectName("pushButton_PreviousComment")
        self.gridLayout_9.addWidget(self.pushButton_PreviousComment, 0, 2, 1, 1)
        self.pushButton_NextComment = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_NextComment.setObjectName("pushButton_NextComment")
        self.gridLayout_9.addWidget(self.pushButton_NextComment, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem1, 0, 4, 1, 1)
        self.pushButton_SaveComment = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_SaveComment.setObjectName("pushButton_SaveComment")
        self.gridLayout_9.addWidget(self.pushButton_SaveComment, 0, 5, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.tabWidget_TextFields.addTab(self.tab_2, "")
        self.gridLayout_7.addWidget(self.tabWidget_TextFields, 1, 1, 3, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(330, 130))
        self.tabWidget.setMaximumSize(QtCore.QSize(330, 130))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.plainTextEdit_StringSearch = MyStringSearchPlainTextEdit(self.tab_3)
        self.plainTextEdit_StringSearch.setMinimumSize(QtCore.QSize(0, 30))
        self.plainTextEdit_StringSearch.setMaximumSize(QtCore.QSize(16777215, 30))
        self.plainTextEdit_StringSearch.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_StringSearch.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_StringSearch.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.plainTextEdit_StringSearch.setPlainText("")
        self.plainTextEdit_StringSearch.setObjectName("plainTextEdit_StringSearch")
        self.gridLayout_5.addWidget(self.plainTextEdit_StringSearch, 0, 0, 1, 2)
        self.pushButton_CommitStringSearch = QtGui.QPushButton(self.tab_3)
        self.pushButton_CommitStringSearch.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_CommitStringSearch.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_CommitStringSearch.setToolTip("")
        self.pushButton_CommitStringSearch.setObjectName("pushButton_CommitStringSearch")
        self.gridLayout_5.addWidget(self.pushButton_CommitStringSearch, 0, 2, 1, 1)
        self.pushButton_PreviousSearch = QtGui.QPushButton(self.tab_3)
        self.pushButton_PreviousSearch.setEnabled(True)
        self.pushButton_PreviousSearch.setMinimumSize(QtCore.QSize(0, 29))
        self.pushButton_PreviousSearch.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_PreviousSearch.setToolTip("")
        self.pushButton_PreviousSearch.setObjectName("pushButton_PreviousSearch")
        self.gridLayout_5.addWidget(self.pushButton_PreviousSearch, 1, 0, 1, 1)
        self.pushButton_NextSearch = QtGui.QPushButton(self.tab_3)
        self.pushButton_NextSearch.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_NextSearch.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_NextSearch.setToolTip("")
        self.pushButton_NextSearch.setObjectName("pushButton_NextSearch")
        self.gridLayout_5.addWidget(self.pushButton_NextSearch, 1, 1, 1, 1)
        self.pushButton_ResetStringSearch = QtGui.QPushButton(self.tab_3)
        self.pushButton_ResetStringSearch.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_ResetStringSearch.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_ResetStringSearch.setToolTip("")
        self.pushButton_ResetStringSearch.setObjectName("pushButton_ResetStringSearch")
        self.gridLayout_5.addWidget(self.pushButton_ResetStringSearch, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_ChooseFilter = QtGui.QComboBox(self.tab_4)
        self.comboBox_ChooseFilter.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_ChooseFilter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox_ChooseFilter.setObjectName("comboBox_ChooseFilter")
        self.gridLayout_3.addWidget(self.comboBox_ChooseFilter, 0, 0, 1, 3)
        self.pushButton_NewFilter = QtGui.QPushButton(self.tab_4)
        self.pushButton_NewFilter.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_NewFilter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_NewFilter.setObjectName("pushButton_NewFilter")
        self.gridLayout_3.addWidget(self.pushButton_NewFilter, 1, 0, 1, 1)
        self.pushButton_EditFilter = QtGui.QPushButton(self.tab_4)
        self.pushButton_EditFilter.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_EditFilter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_EditFilter.setObjectName("pushButton_EditFilter")
        self.gridLayout_3.addWidget(self.pushButton_EditFilter, 1, 1, 1, 1)
        self.pushButton_DeleteFilter = QtGui.QPushButton(self.tab_4)
        self.pushButton_DeleteFilter.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_DeleteFilter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_DeleteFilter.setObjectName("pushButton_DeleteFilter")
        self.gridLayout_3.addWidget(self.pushButton_DeleteFilter, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_7.addWidget(self.tabWidget, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(17, 139, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem2, 3, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_ActiveSite = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_ActiveSite.setMinimumSize(QtCore.QSize(180, 30))
        self.comboBox_ActiveSite.setMaximumSize(QtCore.QSize(180, 30))
        self.comboBox_ActiveSite.setToolTip("")
        self.comboBox_ActiveSite.setObjectName("comboBox_ActiveSite")
        self.gridLayout_2.addWidget(self.comboBox_ActiveSite, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_4, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1227, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_TextFields.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "GCA Analysis Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Calendar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_FirstEntry.setStatusTip(QtGui.QApplication.translate("MainWindow", "Focus calendar on the  first recorded date in the history log (excluding ignored dates)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_FirstEntry.setText(QtGui.QApplication.translate("MainWindow", "First Date", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_LastEntry.setStatusTip(QtGui.QApplication.translate("MainWindow", "Focus calendar on the last recorded date in the history log (excluding ignored dates)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_LastEntry.setText(QtGui.QApplication.translate("MainWindow", "Last Date", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Today.setStatusTip(QtGui.QApplication.translate("MainWindow", "Focus calendar on the active date", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Today.setText(QtGui.QApplication.translate("MainWindow", "Active Date", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Coloring Scheme", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_Coloring.setStatusTip(QtGui.QApplication.translate("MainWindow", "Choose different coloring rules for the calendar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_TextFields.setTabText(self.tabWidget_TextFields.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "History Log", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("MainWindow", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_DeleteComment.setStatusTip(QtGui.QApplication.translate("MainWindow", "Delete this comment from database", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_DeleteComment.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_PreviousComment.setStatusTip(QtGui.QApplication.translate("MainWindow", "Jump to previous comment", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_PreviousComment.setText(QtGui.QApplication.translate("MainWindow", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_NextComment.setStatusTip(QtGui.QApplication.translate("MainWindow", "Jump to next comment", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_NextComment.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_SaveComment.setStatusTip(QtGui.QApplication.translate("MainWindow", "Save this comment to database", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_SaveComment.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_TextFields.setTabText(self.tabWidget_TextFields.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CommitStringSearch.setStatusTip(QtGui.QApplication.translate("MainWindow", "Commit search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CommitStringSearch.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_PreviousSearch.setStatusTip(QtGui.QApplication.translate("MainWindow", "Focus calendar on the previous date in which history log contains search string", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_PreviousSearch.setText(QtGui.QApplication.translate("MainWindow", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_NextSearch.setStatusTip(QtGui.QApplication.translate("MainWindow", "Focus calendar on the next date in which history log contains search string", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_NextSearch.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ResetStringSearch.setStatusTip(QtGui.QApplication.translate("MainWindow", "Clear search string", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ResetStringSearch.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "String Search", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ChooseFilter.setStatusTip(QtGui.QApplication.translate("MainWindow", "Choose history log filter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_NewFilter.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create a new filter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_NewFilter.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_EditFilter.setStatusTip(QtGui.QApplication.translate("MainWindow", "Edit currently chosen filter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_EditFilter.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_DeleteFilter.setStatusTip(QtGui.QApplication.translate("MainWindow", "Delete currently chosen filter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_DeleteFilter.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Active Site", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ActiveSite.setStatusTip(QtGui.QApplication.translate("MainWindow", "Choose active site", None, QtGui.QApplication.UnicodeUTF8))

from mycalendarwidget import MyCalendarWidget
from mystringsearchplaintextedit import MyStringSearchPlainTextEdit
