# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_graphwindow.ui',
# licensing of 'ui_graphwindow.ui' applies.
#
# Created: Wed Jul 31 16:06:23 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 401)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mplCanvasWidget = MyMplCanvasWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCanvasWidget.sizePolicy().hasHeightForWidth())
        self.mplCanvasWidget.setSizePolicy(sizePolicy)
        self.mplCanvasWidget.setObjectName("mplCanvasWidget")
        self.gridLayout_2.addWidget(self.mplCanvasWidget, 0, 0, 1, 5)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setInvertedAppearance(False)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 0, 1, 5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_X_Day = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_X_Day.setObjectName("radioButton_X_Day")
        self.gridLayout.addWidget(self.radioButton_X_Day, 0, 0, 1, 1)
        self.radioButton_X_Week = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_X_Week.setObjectName("radioButton_X_Week")
        self.gridLayout.addWidget(self.radioButton_X_Week, 1, 0, 1, 1)
        self.radioButton_X_Month = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_X_Month.setObjectName("radioButton_X_Month")
        self.gridLayout.addWidget(self.radioButton_X_Month, 2, 0, 1, 1)
        self.radioButton_X_Year = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_X_Year.setObjectName("radioButton_X_Year")
        self.gridLayout.addWidget(self.radioButton_X_Year, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBox_Y_Subplot_1 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_Y_Subplot_1.setObjectName("comboBox_Y_Subplot_1")
        self.gridLayout_4.addWidget(self.comboBox_Y_Subplot_1, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.comboBox_Y_Subplot_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_Y_Subplot_2.setObjectName("comboBox_Y_Subplot_2")
        self.gridLayout_4.addWidget(self.comboBox_Y_Subplot_2, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 1)
        self.comboBox_Y_Subplot_3 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_Y_Subplot_3.setObjectName("comboBox_Y_Subplot_3")
        self.gridLayout_4.addWidget(self.comboBox_Y_Subplot_3, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 2, 1, 1, 1)
        self.groupBox_Deviation_Parameters = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Deviation_Parameters.setObjectName("groupBox_Deviation_Parameters")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_Deviation_Parameters)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_Deviation_Parameters)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_Rwy_1 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_Rwy_1.setObjectName("radioButton_Rwy_1")
        self.gridLayout_3.addWidget(self.radioButton_Rwy_1, 0, 0, 1, 1)
        self.radioButton_Rwy_4 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_Rwy_4.setObjectName("radioButton_Rwy_4")
        self.gridLayout_3.addWidget(self.radioButton_Rwy_4, 0, 1, 1, 1)
        self.radioButton_Rwy_2 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_Rwy_2.setObjectName("radioButton_Rwy_2")
        self.gridLayout_3.addWidget(self.radioButton_Rwy_2, 1, 0, 1, 1)
        self.radioButton_Rwy_5 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_Rwy_5.setObjectName("radioButton_Rwy_5")
        self.gridLayout_3.addWidget(self.radioButton_Rwy_5, 1, 1, 1, 1)
        self.radioButton_Rwy_3 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_Rwy_3.setObjectName("radioButton_Rwy_3")
        self.gridLayout_3.addWidget(self.radioButton_Rwy_3, 2, 0, 1, 1)
        self.radioButton_Rwy_6 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_Rwy_6.setObjectName("radioButton_Rwy_6")
        self.gridLayout_3.addWidget(self.radioButton_Rwy_6, 2, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_Deviation_Parameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioButton_Par = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_Par.setObjectName("radioButton_Par")
        self.gridLayout_5.addWidget(self.radioButton_Par, 0, 0, 1, 1)
        self.radioButton_Combined = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_Combined.setObjectName("radioButton_Combined")
        self.gridLayout_5.addWidget(self.radioButton_Combined, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_7, 0, 1, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_Deviation_Parameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.radioButton_Clear = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton_Clear.setObjectName("radioButton_Clear")
        self.gridLayout_6.addWidget(self.radioButton_Clear, 0, 0, 1, 1)
        self.radioButton_Rain = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton_Rain.setObjectName("radioButton_Rain")
        self.gridLayout_6.addWidget(self.radioButton_Rain, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_8, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_Deviation_Parameters, 2, 2, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.radioButton_DPI100 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_DPI100.setObjectName("radioButton_DPI100")
        self.gridLayout_8.addWidget(self.radioButton_DPI100, 0, 0, 1, 1)
        self.radioButton_DPI150 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_DPI150.setObjectName("radioButton_DPI150")
        self.gridLayout_8.addWidget(self.radioButton_DPI150, 1, 0, 1, 1)
        self.radioButton_DPI200 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_DPI200.setObjectName("radioButton_DPI200")
        self.gridLayout_8.addWidget(self.radioButton_DPI200, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(575, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "X-axis", None, -1))
        self.radioButton_X_Day.setText(QtWidgets.QApplication.translate("MainWindow", "Day", None, -1))
        self.radioButton_X_Week.setText(QtWidgets.QApplication.translate("MainWindow", "Week", None, -1))
        self.radioButton_X_Month.setText(QtWidgets.QApplication.translate("MainWindow", "Month", None, -1))
        self.radioButton_X_Year.setText(QtWidgets.QApplication.translate("MainWindow", "Year", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Y-axis", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Graph 1", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Graph 2", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Graph 3", None, -1))
        self.groupBox_Deviation_Parameters.setTitle(QtWidgets.QApplication.translate("MainWindow", "MTI Deviation Parameters", None, -1))
        self.groupBox_6.setTitle(QtWidgets.QApplication.translate("MainWindow", "Runway", None, -1))
        self.radioButton_Rwy_1.setText(QtWidgets.QApplication.translate("MainWindow", "Runway 1", None, -1))
        self.radioButton_Rwy_4.setText(QtWidgets.QApplication.translate("MainWindow", "Runway 4", None, -1))
        self.radioButton_Rwy_2.setText(QtWidgets.QApplication.translate("MainWindow", "Runway 2", None, -1))
        self.radioButton_Rwy_5.setText(QtWidgets.QApplication.translate("MainWindow", "Runway 5", None, -1))
        self.radioButton_Rwy_3.setText(QtWidgets.QApplication.translate("MainWindow", "Runway 3", None, -1))
        self.radioButton_Rwy_6.setText(QtWidgets.QApplication.translate("MainWindow", "Runway 6", None, -1))
        self.groupBox_7.setTitle(QtWidgets.QApplication.translate("MainWindow", "Mode", None, -1))
        self.radioButton_Par.setText(QtWidgets.QApplication.translate("MainWindow", "PAR", None, -1))
        self.radioButton_Combined.setText(QtWidgets.QApplication.translate("MainWindow", "Combined", None, -1))
        self.groupBox_8.setTitle(QtWidgets.QApplication.translate("MainWindow", "Weather", None, -1))
        self.radioButton_Clear.setText(QtWidgets.QApplication.translate("MainWindow", "Clear", None, -1))
        self.radioButton_Rain.setText(QtWidgets.QApplication.translate("MainWindow", "Rain", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "DPI", None, -1))
        self.radioButton_DPI100.setText(QtWidgets.QApplication.translate("MainWindow", "100", None, -1))
        self.radioButton_DPI150.setText(QtWidgets.QApplication.translate("MainWindow", "150", None, -1))
        self.radioButton_DPI200.setText(QtWidgets.QApplication.translate("MainWindow", "200", None, -1))

from view.graphwindow.mplcanvaswidget import MyMplCanvasWidget
