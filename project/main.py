#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


import sys
#import time
import multiprocessing
import logging
from PySide import QtGui
from view.view import MyView
from presenter.presenter import MyPresenter
from model.database import Database


if __name__ == '__main__':

    multiprocessing.freeze_support()

    #logger = logging.getLogger(__name__)

    # load the logging configuration
    #logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
    # Make sure that the already created module loggers does not get stopped!!!
    # Should i get the working directory for this????
    # Do I have to copy the logging.ini file to the dist directory after freezing the app with PyInstaller????

    app = QtGui.QApplication(sys.argv)

    #print 'CREATING MODEL, VIEW AND PRESENTER'

    #from model.database import Database
    model = Database()
    
    #from view.view import MyView
    view = MyView() 
    #view.show()

    #from presenter.presenter import MyPresenter
    presenter = MyPresenter(model, view, app)
    
    view.show()
    
    #print 'NOW STARTING APP'
    
    #time.sleep(5)
    
    #presenter.start_app(test=False)

    #print 'APP STARTED'

    #if presenter.trial_has_ended:
    #    presenter.message(u'Trial has ended.\n\nCopyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>')
    #elif presenter.progress.wasCanceled():
    #    pass
    #else:
        
    sys.exit(app.exec_())

