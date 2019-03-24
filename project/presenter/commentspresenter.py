#!/usr/bin/env python
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
#from presenter.filtercontainer import Filter
#from view.myfilterdialog import MyFilterDialog
#from presenter.eventfilter import EventBlocker




class CommentsPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter):
        super(CommentsPresenter, self).__init__()
        self.model = model
        self.view = view
        self.presenter = presenter

        self.comment_text_changed = False


    # Comments stuff


    def active_date(self):                                          # Move this method
        return self.view.calendarWidget.selectedDate()


    def save_comment(self):
        if not self.presenter.active_site_name == u'':
            commented_dates = [date for date in self.model.get_comment_dictionary(self.presenter.active_site_name).keys()]
            if self.active_date() in commented_dates:

            # Does comment exist for this date?
            #if self.model.get_comment(self.active_site, self.active_date()):

                # Has the text been changed?
                #if self.comment_text_changed:

                clicked = self.presenter.message_with_cancel_choice(u'Comment already exists for this date.', u'Overwrite?', QtGui.QMessageBox.Ok)

                if clicked == QtGui.QMessageBox.Ok:
                    # Save it
                    text_to_save = self.view.plainTextEdit_Comment.toPlainText()
                    self.model.save_comment(self.presenter.active_site_name, self.view.calendarWidget.selectedDate(), text_to_save)
            else:
                # Just save it
                text_to_save = self.view.plainTextEdit_Comment.toPlainText()
                self.model.save_comment(self.presenter.active_site_name, self.view.calendarWidget.selectedDate(), text_to_save)
            #text_to_save = self.view.plainTextEdit_Comment.toPlainText()
            #self.model.save_comment(self.active_site, self.view.calendarWidget.selectedDate(), text_to_save)
            self.update_comment()
            self.presenter.update_calendar()


    def delete_comment(self):
        if not self.presenter.active_site_name == u'':
            commented_dates = [date for date in self.model.get_comment_dictionary(self.presenter.active_site_name).keys()]
            if self.active_date() in commented_dates:
        
                clicked = self.presenter.message_with_cancel_choice(u'Comment will be removed from the database.', u'Continue?', QtWidgets.QMessageBox.Cancel)
                if clicked == QtWidgets.QMessageBox.Ok:
                    self.model.delete_comment(self.presenter.active_site_name, self.active_date())
                    self.update_comment()
                    self.presenter.update_calendar()

            else:

                self.update_comment()


    def update_comment(self):
        
        date = self.view.calendarWidget.selectedDate()
            
        if self.presenter.active_site_name == u'':
            text = u''
        else:
            text = self.model.get_comment(self.presenter.active_site_name, self.view.calendarWidget.selectedDate())
            
        if text:
            self.view.plainTextEdit_Comment.setPlainText(text)
        else:
            self.view.plainTextEdit_Comment.clear()

        if self.presenter.active_site_name == u'':
            comment_dates = []
        else:
            comment_dates = [date for date in self.model.get_comment_dictionary(self.presenter.active_site_name).keys()]
            
        self.view.calendarWidget.setTriangleDates(comment_dates)


    def set_next_comment_date(self):
        if not self.presenter.active_site_name == u'':
            dates = sorted([date for date, _ in self.model.get_comment_dictionary(self.presenter.active_site_name).items()])
            if not len(dates) == 0:
                greater_dates = [date for date in dates if date > self.active_date()]
                if len(greater_dates) == 0:
                    new_index = 0
                else:
                    new_index = dates.index(greater_dates[0])
                self.view.calendarWidget.setSelectedDate(dates[new_index])
                self.view.calendarWidget.updateCells()



    def set_previous_comment_date(self):
        if not self.presenter.active_site_name == u'':
            dates = sorted([date for date, _ in self.model.get_comment_dictionary(self.presenter.active_site_name).items()])
            if not len(dates) == 0:
                lesser_dates = [date for date in dates if date < self.active_date()]
                if len(lesser_dates) == 0:
                    new_index = -1
                else:
                    new_index = dates.index(lesser_dates[-1])
                self.view.calendarWidget.setSelectedDate(dates[new_index])
                self.view.calendarWidget.updateCells()


