#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


import sys
from PySide import QtGui
#from view.view import MyView
#from presenter.presenter import MyPresenter
#from model.database import Database


if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)

    #print 'CREATING MODEL, VIEW AND PRESENTER'

    from model.database import Database
    model = Database()
    
    from view.view import MyView
    view = MyView() 
    #view.show()

    from presenter.presenter import MyPresenter
    presenter = MyPresenter(model, view)
    
    view.show()
    
    #print 'NOW STARTING APP'
    
    presenter.start_app()

    #print 'APP STARTED'

    if presenter.trial_has_ended:
        presenter.message(u'Trial has ended.\n\nCopyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>')
    elif presenter.progress.wasCanceled():
        pass
    else:
        sys.exit(app.exec_())

