# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_graphwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ...view.graphwindow.mplcanvaswidget import MyMplCanvasWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(788, 528)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.mplCanvasWidget = MyMplCanvasWidget(self.centralwidget)
        self.mplCanvasWidget.setObjectName(u"mplCanvasWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCanvasWidget.sizePolicy().hasHeightForWidth())
        self.mplCanvasWidget.setSizePolicy(sizePolicy)

        self.gridLayout_9.addWidget(self.mplCanvasWidget, 0, 0, 1, 1)

        self.horizontalScrollBar = QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)
        self.horizontalScrollBar.setInvertedAppearance(False)

        self.gridLayout_9.addWidget(self.horizontalScrollBar, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 788, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy1)
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable)
        self.dockWidget.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.gridLayout_2 = QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(1, 138, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.dockWidgetContents_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton_X_Week = QRadioButton(self.groupBox_2)
        self.radioButton_X_Week.setObjectName(u"radioButton_X_Week")

        self.gridLayout.addWidget(self.radioButton_X_Week, 1, 0, 1, 1)

        self.radioButton_X_Day = QRadioButton(self.groupBox_2)
        self.radioButton_X_Day.setObjectName(u"radioButton_X_Day")

        self.gridLayout.addWidget(self.radioButton_X_Day, 0, 0, 1, 1)

        self.radioButton_X_Year = QRadioButton(self.groupBox_2)
        self.radioButton_X_Year.setObjectName(u"radioButton_X_Year")

        self.gridLayout.addWidget(self.radioButton_X_Year, 3, 0, 1, 1)

        self.radioButton_X_Month = QRadioButton(self.groupBox_2)
        self.radioButton_X_Month.setObjectName(u"radioButton_X_Month")

        self.gridLayout.addWidget(self.radioButton_X_Month, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.dockWidgetContents_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox_Y_Subplot_1 = QComboBox(self.groupBox_4)
        self.comboBox_Y_Subplot_1.setObjectName(u"comboBox_Y_Subplot_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_Y_Subplot_1.sizePolicy().hasHeightForWidth())
        self.comboBox_Y_Subplot_1.setSizePolicy(sizePolicy3)
        self.comboBox_Y_Subplot_1.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_4.addWidget(self.comboBox_Y_Subplot_1, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.comboBox_Y_Subplot_2 = QComboBox(self.groupBox_4)
        self.comboBox_Y_Subplot_2.setObjectName(u"comboBox_Y_Subplot_2")
        sizePolicy3.setHeightForWidth(self.comboBox_Y_Subplot_2.sizePolicy().hasHeightForWidth())
        self.comboBox_Y_Subplot_2.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.comboBox_Y_Subplot_2, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 1)

        self.comboBox_Y_Subplot_3 = QComboBox(self.groupBox_4)
        self.comboBox_Y_Subplot_3.setObjectName(u"comboBox_Y_Subplot_3")
        sizePolicy3.setHeightForWidth(self.comboBox_Y_Subplot_3.sizePolicy().hasHeightForWidth())
        self.comboBox_Y_Subplot_3.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.comboBox_Y_Subplot_3, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 0, 2, 1, 1)

        self.groupBox_Deviation_Parameters = QGroupBox(self.dockWidgetContents_2)
        self.groupBox_Deviation_Parameters.setObjectName(u"groupBox_Deviation_Parameters")
        sizePolicy3.setHeightForWidth(self.groupBox_Deviation_Parameters.sizePolicy().hasHeightForWidth())
        self.groupBox_Deviation_Parameters.setSizePolicy(sizePolicy3)
        self.gridLayout_7 = QGridLayout(self.groupBox_Deviation_Parameters)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_6 = QGroupBox(self.groupBox_Deviation_Parameters)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_3 = QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radioButton_Rwy_1 = QRadioButton(self.groupBox_6)
        self.radioButton_Rwy_1.setObjectName(u"radioButton_Rwy_1")

        self.gridLayout_3.addWidget(self.radioButton_Rwy_1, 0, 0, 1, 1)

        self.radioButton_Rwy_4 = QRadioButton(self.groupBox_6)
        self.radioButton_Rwy_4.setObjectName(u"radioButton_Rwy_4")

        self.gridLayout_3.addWidget(self.radioButton_Rwy_4, 0, 1, 1, 1)

        self.radioButton_Rwy_2 = QRadioButton(self.groupBox_6)
        self.radioButton_Rwy_2.setObjectName(u"radioButton_Rwy_2")

        self.gridLayout_3.addWidget(self.radioButton_Rwy_2, 1, 0, 1, 1)

        self.radioButton_Rwy_5 = QRadioButton(self.groupBox_6)
        self.radioButton_Rwy_5.setObjectName(u"radioButton_Rwy_5")

        self.gridLayout_3.addWidget(self.radioButton_Rwy_5, 1, 1, 1, 1)

        self.radioButton_Rwy_3 = QRadioButton(self.groupBox_6)
        self.radioButton_Rwy_3.setObjectName(u"radioButton_Rwy_3")

        self.gridLayout_3.addWidget(self.radioButton_Rwy_3, 2, 0, 1, 1)

        self.radioButton_Rwy_6 = QRadioButton(self.groupBox_6)
        self.radioButton_Rwy_6.setObjectName(u"radioButton_Rwy_6")

        self.gridLayout_3.addWidget(self.radioButton_Rwy_6, 2, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBox_Deviation_Parameters)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy1.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy1)
        self.gridLayout_5 = QGridLayout(self.groupBox_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.radioButton_Par = QRadioButton(self.groupBox_7)
        self.radioButton_Par.setObjectName(u"radioButton_Par")

        self.gridLayout_5.addWidget(self.radioButton_Par, 0, 0, 1, 1)

        self.radioButton_Combined = QRadioButton(self.groupBox_7)
        self.radioButton_Combined.setObjectName(u"radioButton_Combined")

        self.gridLayout_5.addWidget(self.radioButton_Combined, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_7, 0, 1, 1, 1)

        self.groupBox_8 = QGroupBox(self.groupBox_Deviation_Parameters)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy1.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy1)
        self.gridLayout_6 = QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.radioButton_Clear = QRadioButton(self.groupBox_8)
        self.radioButton_Clear.setObjectName(u"radioButton_Clear")

        self.gridLayout_6.addWidget(self.radioButton_Clear, 0, 0, 1, 1)

        self.radioButton_Rain = QRadioButton(self.groupBox_8)
        self.radioButton_Rain.setObjectName(u"radioButton_Rain")

        self.gridLayout_6.addWidget(self.radioButton_Rain, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_8, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_Deviation_Parameters, 0, 3, 1, 1)

        self.groupBox_3 = QGroupBox(self.dockWidgetContents_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.radioButton_DPI50 = QRadioButton(self.groupBox_3)
        self.radioButton_DPI50.setObjectName(u"radioButton_DPI50")

        self.gridLayout_8.addWidget(self.radioButton_DPI50, 0, 0, 1, 1)

        self.radioButton_DPI75 = QRadioButton(self.groupBox_3)
        self.radioButton_DPI75.setObjectName(u"radioButton_DPI75")

        self.gridLayout_8.addWidget(self.radioButton_DPI75, 1, 0, 1, 1)

        self.radioButton_DPI100 = QRadioButton(self.groupBox_3)
        self.radioButton_DPI100.setObjectName(u"radioButton_DPI100")

        self.gridLayout_8.addWidget(self.radioButton_DPI100, 2, 0, 1, 1)

        self.radioButton_DPI150 = QRadioButton(self.groupBox_3)
        self.radioButton_DPI150.setObjectName(u"radioButton_DPI150")

        self.gridLayout_8.addWidget(self.radioButton_DPI150, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(1, 138, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 5, 1, 1)

        self.dockWidget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dockWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"X-axis", None))
        self.radioButton_X_Week.setText(QCoreApplication.translate("MainWindow", u"Week", None))
        self.radioButton_X_Day.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.radioButton_X_Year.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.radioButton_X_Month.setText(QCoreApplication.translate("MainWindow", u"Month", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Y-axis", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Graph 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Graph 2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Graph 3", None))
        self.groupBox_Deviation_Parameters.setTitle(QCoreApplication.translate("MainWindow", u"MTI Deviation Parameters", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Runway", None))
        self.radioButton_Rwy_1.setText(QCoreApplication.translate("MainWindow", u"Runway 1", None))
        self.radioButton_Rwy_4.setText(QCoreApplication.translate("MainWindow", u"Runway 4", None))
        self.radioButton_Rwy_2.setText(QCoreApplication.translate("MainWindow", u"Runway 2", None))
        self.radioButton_Rwy_5.setText(QCoreApplication.translate("MainWindow", u"Runway 5", None))
        self.radioButton_Rwy_3.setText(QCoreApplication.translate("MainWindow", u"Runway 3", None))
        self.radioButton_Rwy_6.setText(QCoreApplication.translate("MainWindow", u"Runway 6", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.radioButton_Par.setText(QCoreApplication.translate("MainWindow", u"PAR", None))
        self.radioButton_Combined.setText(QCoreApplication.translate("MainWindow", u"Combined", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Weather", None))
        self.radioButton_Clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.radioButton_Rain.setText(QCoreApplication.translate("MainWindow", u"Rain", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"DPI", None))
        self.radioButton_DPI50.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.radioButton_DPI75.setText(QCoreApplication.translate("MainWindow", u"75", None))
        self.radioButton_DPI100.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.radioButton_DPI150.setText(QCoreApplication.translate("MainWindow", u"150", None))
    # retranslateUi

