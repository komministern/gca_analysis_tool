# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


#import os
#import string
#import time
from PySide2 import QtCore, QtGui, QtWidgets
#from presenter.coloringcontainer import ColoringContainer
#import presenter.textstuff as txt
from presenter.mainwindow.localresources.filtercontainer import Filter
from view.mainwindow.myfilterdialog import MyFilterDialog
#from presenter.eventfilter import EventBlocker



class FilterPresenter(QtCore.QObject):

    def __init__(self, model, mainwindow, mainwindowpresenter):
        super(FilterPresenter, self).__init__()
        self.model = model
        #self.view = view
        self.mainwindow = mainwindow
        self.mainwindowpresenter = mainwindowpresenter

        #self.current_filter = self.model.filter_list[0]
        self.current_filter = self.model.get_filter_by_index(0)

        #self.view.comboBox_ChooseFilter.addItems([each.name for each in self.model.filter_list])
        self.mainwindow.comboBox_ChooseFilter.addItems([each.name for each in self.model.get_filter_list()])
        
        self.mainwindow.pushButton_EditFilter.setEnabled(False)
        self.mainwindow.pushButton_DeleteFilter.setEnabled(False)

    # ----------- Filter stuff


    def format_text(self, text):
        if text != u'No history log exists for this date.' and text != 'This date is in the list of ignored dates. You must deignore it before you can view the contents of the historylog.':
            if self.current_filter.state == 1 and self.current_filter.content:  # Show Only
                return '\n'.join([s for s in text.splitlines() if s[0:4] in self.current_filter.content])
            elif self.current_filter.state == 0:        # Suppress
                return '\n'.join([s for s in text.splitlines() if not s[0:4] in self.current_filter.content])
        return text


    def show_filter_dialog(self, initial_filter, name_editable = True):
        self.dialog = MyFilterDialog(initial_filter, name_editable, self.mainwindow)
        self.dialog.setModal(True)
        
        self.dialog.show()
        height = self.dialog.pushButton_AddContent.height()
        self.dialog.pushButton_AddContent.setFixedWidth(height * 1.5)
        self.dialog.pushButton_RemoveContent.setFixedWidth(height * 1.5)

        if self.dialog.exec_():
            filter = self.dialog.get_final_filter()
            self.save_filter(filter)


    def save_filter(self, filter):
        if filter.name in set([each.name for each in self.model.get_filter_list()]):
            for index in range(len(self.model.get_filter_list())):
                if self.model.get_filter_by_index(index).name == filter.name:
                    break
            self.model.remove_filter_by_index(index)
            #del self.model.get_filter_by_index(index)

        #self.model.filter_list.append(filter)
        self.model.add_filter(filter)
        
        #self.model.filter_list.sort(key = lambda x: x.name)
        #self.model.update_filters()
        
        self.mainwindow.comboBox_ChooseFilter.clear()
        self.mainwindow.comboBox_ChooseFilter.addItems([each.name for each in self.model.get_filter_list()])

        for index in range(len(self.model.get_filter_list())):
            if self.model.get_filter_by_index(index).name == filter.name:
                break
 
        self.mainwindow.comboBox_ChooseFilter.setCurrentIndex(index)


    def new_filter(self):
        self.show_filter_dialog(Filter())


    def edit_filter(self):
        self.show_filter_dialog(self.current_filter, name_editable = True)
        

    def delete_filter(self):
        clicked = self.mainwindowpresenter.message_with_cancel_choice(u'Delete ' + self.current_filter.name + '?', u'This will completely remove the filter.', QtWidgets.QMessageBox.Cancel)
        if clicked == QtWidgets.QMessageBox.Ok:

            self.model.remove_filter_by_index(self.model.get_filter_list().index(self.current_filter))  # In mainwindowpresenter!?!

            #self.model.filter_list.remove(self.current_filter)
            #self.model.update_filters()

            self.mainwindow.comboBox_ChooseFilter.clear()
            self.mainwindow.comboBox_ChooseFilter.addItems([each.name for each in self.model.get_filter_list()])
        
            self.choose_filter(0)
        

    def choose_filter(self, index):
        
        if index == 0:
            text = self.mainwindow.tabWidget_Search.tabText(1)
            if text[-1] == u'*':
                self.mainwindow.tabWidget_Search.setTabText(1, text[0:-1])
                
            self.mainwindow.pushButton_EditFilter.setEnabled(False)
            self.mainwindow.pushButton_DeleteFilter.setEnabled(False)
        else:

            text = self.mainwindow.tabWidget_Search.tabText(1)
            if text[-1] != u'*':
                self.mainwindow.tabWidget_Search.setTabText(1, text + u'*')
                
            self.mainwindow.pushButton_EditFilter.setEnabled(True)
            self.mainwindow.pushButton_DeleteFilter.setEnabled(True)

        #self.current_filter = self.model.filter_list[index]
        self.current_filter = self.model.get_filter_by_index(index)     # Hmmmm.... Should this be called from mainwindowpresenter instead!?!
        self.mainwindowpresenter.update_text()