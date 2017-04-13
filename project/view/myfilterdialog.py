#!/usr/bin/env python
# -*- coding: utf-8 -*-


#    Copyright � 2016, 2017 Oscar Franz�n <oscarfranzen@yahoo.se>
#
#    This file is part of GCA Analysis Tool.


from PySide import QtGui, QtCore
from ui_filterdialog import Ui_Dialog
from presenter.filtercontainer import Filter

class MyFilterDialog(QtGui.QDialog, Ui_Dialog):

#    quit = QtCore.Signal()

    def __init__(self, initial_filter, name_editable = True):
        super(MyFilterDialog, self).__init__()
        self.setupUi(self)
        
        if not name_editable:
            self.lineEdit_FilterName.setEnabled(False)
        
        self.filter = initial_filter

        self.lineEdit_FilterName.setText(self.filter.name)

        self.plainTextEdit_FilterContent.setItems(self.filter.content)

        self.possible_identifiers = [u'(00)', u'(01)', u'(02)', u'(03)', u'(04)',
                                     u'(05)', u'(06)', u'(07)', u'(08)', u'(09)',
                                     u'(0a)', u'(0b)', u'(0c)', u'(0d)', u'(0e)',
                                     u'(0f)', u'(10)', u'(11)', u'(12)', u'(13)',
                                     u'(14)', u'(15)', u'(16)', u'(17)', u'(18)',
                                     u'(19)', u'(1a)', u'(1b)', u'(1c)', u'(1d)',
                                     u'(1e)', u'(1f)', u'(20)', u'(21)', u'(22)',
                                     u'(23)', u'(24)']
        self.plainTextEdit_PossibleContent.setItems(self.possible_identifiers)

        self.filter_states = [u'Suppress', u'Show Only']
        self.comboBox_FilterState.addItems(self.filter_states)
        self.comboBox_FilterState.setCurrentIndex(self.filter.state)

        self.comboBox_FilterState.currentIndexChanged.connect(self.set_state)

        self.pushButton_Save.pressed.connect(self.validate_filter)
        self.pushButton_Cancel.pressed.connect(self.cancel_filter)
        
        self.pushButton_AddContent.pressed.connect(self.add_content)
        self.pushButton_RemoveContent.pressed.connect(self.remove_content)


    
    def set_state(self, index):
        self.filter.state = index
        

    def add_content(self):
        chosen_identifier_index = self.plainTextEdit_PossibleContent.chosen_index
        if self.possible_identifiers[chosen_identifier_index] not in self.filter.content:
            self.filter.content.append(self.possible_identifiers[chosen_identifier_index])
            self.filter.content.sort()
            index_to_highlight = self.filter.content.index(self.possible_identifiers[chosen_identifier_index])
            self.plainTextEdit_FilterContent.setItems(self.filter.content, index_to_highlight)


    def remove_content(self):
        chosen_content_index = self.plainTextEdit_FilterContent.chosen_index
        if chosen_content_index != None:
            del self.filter.content[chosen_content_index]
            self.plainTextEdit_FilterContent.setItems(self.filter.content)


    def get_final_filter(self):
        return self.filter


    def validate_filter(self):
        self.filter.name = self.lineEdit_FilterName.text()
        if self.filter.name == u'':
            self.message(u'You must name the filter to save it.')
        elif self.filter.content == []:
            self.message(u'Filter content is empty.')
        else:
            self.accept()


    def cancel_filter(self):
        self.reject()


    def message(self, text):
        msgBox = QtGui.QMessageBox()
        msgBox.setText(text)
        msgBox.exec_()
        
    def message_with_cancel_choice(self, text, informative_text, default_button):
        msgBox = QtGui.QMessageBox()
        msgBox.setText(text)
        msgBox.setInformativeText(informative_text)
        msgBox.setStandardButtons(QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Ok)
        msgBox.setDefaultButton(default_button)
        return msgBox.exec_()