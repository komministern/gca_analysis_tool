#!/usr/bin/env python
# -*- coding: utf-8 -*-


#    Copyright © 2016, 2017 Oscar Franzén <oscarfranzen@yahoo.se>
#
#    This file is part of GCA Analysis Tool.


from PySide import QtGui, QtCore
from ui_filterwidget import Ui_Form
#from licensewindow import MyLicenseWindow


class MyFilterWidget(QtGui.QWidget, Ui_Form):

    quit = QtCore.Signal()

    def __init__(self, **kwds):
        super(MyFilterWidget, self).__init__(**kwds)
        self.setupUi(self)
        

#    def about(self):
#        self.win = MyLicenseWindow()
