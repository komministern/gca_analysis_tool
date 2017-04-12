#!/usr/bin/env python
# -*- coding: utf-8 -*-


#    Copyright © 2016, 2017 Oscar Franzén <oscarfranzen@yahoo.se>
#
#    This file is part of GCA Analysis Tool.


from PySide import QtGui, QtCore
from ui_filterdialog import Ui_Dialog
from presenter.filtercontainer import Filter

class MyFilterDialog(QtGui.QDialog, Ui_Dialog):

#    quit = QtCore.Signal()

    def __init__(self, initial_filter):
        super(MyFilterDialog, self).__init__()
        self.setupUi(self)
        
        self.filter = initial_filter

        self.lineEdit_FilterName.setText(self.filter.name)

        self.plainTextEdit_FilterContent.setPlainText('\n'.join(self.filter.content))
        if len(self.filter.content) > 0:
            print 'highlight and mark top row'
        
        self.possible_identifiers = [u'(19)', u'(1a)', u'(1b)', u'(1c)']
        self.comboBox_PossibleIdentifiers.addItems(self.possible_identifiers)
        
        self.filter_states = [u'Suppress', u'Show Only']
        self.comboBox_FilterState.addItems(self.filter_states)
        self.comboBox_FilterState.setCurrentIndex(self.filter.state)
        
        self.pushButton_Save.pressed.connect(self.validate_filter)
        self.pushButton_Cancel.pressed.connect(self.cancel_filter)
        
        self.pushButton_AddContent.pressed.connect(self.add_content)
        self.pushButton_RemoveContent.pressed.connect(self.remove_content)
        

    def add_content(self):
        pass
    
    def remove_content(self):
        pass


    def get_final_filter(self):
        return self.filter
        
    def validate_filter(self):
        self.filter.name = self.lineEdit_FilterName.text()
        self.accept()
        
    def cancel_filter(self):
        self.reject()

    def keyPressEvent(self, e):
        print e.key()