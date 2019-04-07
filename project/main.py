#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


import sys
#import time
import multiprocessing
import logging
import PySide2
from PySide2 import QtCore, QtGui, QtWidgets
from view.view import MyView
from presenter.presenter import MyPresenter
from model.model import MyModel
#from model.database import Database

logger = logging.getLogger(__name__)    # Ok here?
#logging.config.fileConfig('logging.ini', disable_existing_loggers=False)

if __name__ == '__main__':

    multiprocessing.freeze_support()

    #logger = logging.getLogger(__name__)

    # load the logging configuration
    #logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
    # Make sure that the already created module loggers does not get stopped!!!
    # Should i get the working directory for this????
    # Do I have to copy the logging.ini file to the dist directory after freezing the app with PyInstaller????

    # Make this choosable in menu perhaps?
    english = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom)
    QtCore.QLocale.setDefault(english)

    app = QtWidgets.QApplication(sys.argv)
    model = MyModel()
    view = MyView() 
    presenter = MyPresenter(model, view, app)


    view.mainwindow.show()

    comboBox_Coloring_width = view.mainwindow.comboBox_Coloring.size().width()
    comboBox_Coloring_height = view.mainwindow.comboBox_Coloring.size().height()

    view.mainwindow.comboBox_ActiveSite.setFixedWidth(comboBox_Coloring_width * 2.0 / 3.0)

    
    #print(PySide2.__version__)
    #print(PySide2.QtCore.__version__)

        
    sys.exit(app.exec_())
