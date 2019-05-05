#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018, 2019 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.

import PySide2
import platform
from PySide2 import QtCore, QtGui, QtWidgets

from presenter.mainwindow.localresources.eventfilter import EventBlocker

from presenter.mainwindow.filterpresenter import FilterPresenter
from presenter.mainwindow.commentspresenter import CommentsPresenter
from presenter.mainwindow.sitepresenter import SitePresenter
from presenter.mainwindow.textpresenter import TextPresenter
from presenter.mainwindow.calendarpresenter import CalendarPresenter
from presenter.mainwindow.searchpresenter import SearchPresenter
from presenter.mainwindow.menupresenter import MenuPresenter
from presenter.mainwindow.ignorepresenter import IgnorePresenter
from presenter.mainwindow.analysispresenter import AnalysisPresenter
#from presenter.mainwindow.resultspresenter import ResultsPresenter


class MyMainWindowPresenter(QtCore.QObject):

    def __init__(self, model, view, presenter, app):
        super(MyMainWindowPresenter, self).__init__()

        # Store view and model.
        self.model = model
        self.view = view
        self.presenter = presenter
        self.app = app

        self.view.create_mainwindow()

        # Sub-presenters
        self.filter = FilterPresenter(model, view, presenter)
        self.text = TextPresenter(model, view, presenter)
        self.calendar = CalendarPresenter(model, view, presenter)
        self.search = SearchPresenter(model, view, presenter)
        self.comments = CommentsPresenter(model, view, presenter)
        self.site = SitePresenter(model, view, presenter)
        self.menu = MenuPresenter(model, view, presenter)
        self.ignore = IgnorePresenter(model, view, presenter)
        self.analysis = AnalysisPresenter(model, view, presenter)
        #self.resultspresenter = ResultsPresenter(model, view, presenter)

        # Colors
        self.green = QtGui.QColor.fromRgbF(0.248478, 1.000000, 0.431632, 1.000000)
        self.red = QtGui.QColor.fromRgbF(1.000000, 0.343099, 0.419516, 1.000000)
        self.yellow = QtGui.QColor.fromRgbF(1.000000, 0.997757, 0.346044, 1.000000)
        self.blue = QtGui.QColor.fromRgbF(0.509743, 0.734401, 1.000000, 1.000000)

        self.view.mainwindow.progressBar.setMaximum(100)
        
        self.eventblocker = EventBlocker()
        self.app.installEventFilter(self.eventblocker)
        
        self.timer = QtCore.QTimer(self)

        self.connect_signals()

        


        #Block stuff

        #self.view.comboBox_Coloring.model().item(1).setEnabled(False)
        #self.view.comboBox_Coloring.model().item(2).setEnabled(False)
        #self.view.comboBox_Coloring.model().item(3).setEnabled(False)
        #self.view.comboBox_Coloring.model().item(4).setEnabled(False)

        self.view.mainwindow.calendarWidget.setMaximumDate(QtCore.QDate(2019, 12, 31))

        #self.menu.update_menu()

        



    def connect_signals(self):
        self.view.mainwindow.quit.connect(self.model.quit)

        self.view.mainwindow.calendarWidget.selectionChanged.connect(self.calendar.new_date_chosen)

        self.view.mainwindow.pushButton_NewFilter.clicked.connect(self.filter.new_filter)
        self.view.mainwindow.pushButton_EditFilter.clicked.connect(self.filter.edit_filter)
        self.view.mainwindow.pushButton_DeleteFilter.clicked.connect(self.filter.delete_filter)
        self.view.mainwindow.comboBox_ChooseFilter.currentIndexChanged.connect(self.filter.choose_filter)

        self.view.mainwindow.pushButton_CommitStringSearch.clicked.connect(self.search.commit_string_search)
        self.view.mainwindow.pushButton_ResetStringSearch.clicked.connect(self.search.reset_string_search)

        self.view.mainwindow.comboBox_ActiveSite.currentIndexChanged.connect(self.site.set_active_site)
        
        self.view.mainwindow.comboBox_Coloring.currentIndexChanged.connect(self.calendar.set_coloring_scheme)

        self.view.mainwindow.importAction.triggered.connect(self.site.import_capturesite)

        self.view.mainwindow.analysisAction.triggered.connect(self.analysis.analyze)
        
        self.view.mainwindow.ignoreAction.triggered.connect(self.ignore.ignore_date)
        self.view.mainwindow.deIgnoreAction.triggered.connect(self.ignore.deignore_date)
        self.view.mainwindow.deIgnoreAllAction.triggered.connect(self.ignore.deignore_all_dates)
        self.view.mainwindow.nextIgnoredDateAction.triggered.connect(self.ignore.jump_to_next_ignored_date)
        
        self.view.mainwindow.aboutAction.triggered.connect(self.about)

        self.view.mainwindow.wrapAction.triggered.connect(self.text.set_wrap_mode)
        self.view.mainwindow.noWrapAction.triggered.connect(self.text.set_nowrap_mode)

        self.view.mainwindow.pushButton_FirstDate.clicked.connect(self.calendar.set_first_date)
        self.view.mainwindow.pushButton_LastDate.clicked.connect(self.calendar.set_last_date)
        self.view.mainwindow.pushButton_ActiveDate.clicked.connect(self.calendar.set_active_date)

        self.view.mainwindow.pushButton_NextSearch.clicked.connect(self.search.set_next_search_date)
        self.view.mainwindow.pushButton_PreviousSearch.clicked.connect(self.search.set_previous_search_date)

        self.view.mainwindow.plainTextEdit_StringSearch.textChanged.connect(self.search.text_changed)
        self.view.mainwindow.plainTextEdit_StringSearch.returnPressed.connect(self.search.return_pressed)

        self.view.mainwindow.pushButton_SaveComment.clicked.connect(self.comments.save_comment)
        self.view.mainwindow.pushButton_DeleteComment.clicked.connect(self.comments.delete_comment)

        self.view.mainwindow.pushButton_NextComment.clicked.connect(self.comments.set_next_comment_date)
        self.view.mainwindow.pushButton_PreviousComment.clicked.connect(self.comments.set_previous_comment_date)



        self.model.io_progress.connect(self.update_progressbar)



    # Helper methods
    def update_text(self):
        self.text.update_text()

    def update_menu(self):
        self.menu.update_menu()

    def update_calendar(self):
        self.calendar.update_calendar()

    def update_comment(self):
        self.comments.update_comment()

    def colored_dates(self, site_name):
        return self.calendar.colored_dates(site_name)

    def commit_string_search(self):
        self.search.commit_string_search()

    def format_text(self, atext):
        return self.filter.format_text(atext)

    @property
    def active_date(self):
        return self.view.mainwindow.calendarWidget.selectedDate()


    @property
    def highlight(self):
        return self.search.highlight

    @property
    def presentation_dict(self):
        return self.site.presentation_dict

    def set_active_site(self, index):
        self.site.set_active_site(index)

    @property
    def active_site_name(self):
        return self.site.active_site_name

    @active_site_name.setter
    def active_site_name(self, site_name):
        self.site.active_site_name = site_name


    # Misc methods who do not fit into any of the sub-presenters
    def update_progressbar(self, progress):
        self.view.mainwindow.progressBar.setValue(progress)
        QtGui.qApp.processEvents()
        if progress >= 100:
            if not self.timer.isActive():
                # Some delay, just for the feeling
                self.timer.singleShot(100, self.zero_progressbar)
            
    def zero_progressbar(self):
        if self.view.mainwindow.progressBar.value() == 100:
            self.view.mainwindow.progressBar.setValue(0)
        
    # This is not a satisfactory solution. But it works i guess.
    # Call these methods prior to and after I/O actions known to take a lot
    # of time. This prevents any input from the GUI during the file operations,
    # at the same time as the progress bar update takes care of processEvents to
    # keep GUI from locking up.
    
    def inhibit_mouseclicks(self):
        #self.app.removeEventFilter(self.mousedetector)
        #self.app.installEventFilter(self.mouseinhibitor)
        self.eventblocker.block_all_mouse_click_events()

        
    def allow_mouseclicks(self):
        #self.app.removeEventFilter(self.mouseinhibitor)
        #self.app.installEventFilter(self.mousedetector)
        self.eventblocker.unblock_all_events()

    def message(self, text, title_text=''):
        msgBox = QtWidgets.QMessageBox(parent=self.view.mainwindow)
        msgBox.setText(text)
        if title_text:
            msgBox.setWindowTitle(title_text)
        msgBox.exec_()
        
    def message_with_cancel_choice(self, text, informative_text, default_button):
        msgBox = QtWidgets.QMessageBox(parent=self.view.mainwindow)
        msgBox.setText(text)
        msgBox.setInformativeText(informative_text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok)
        msgBox.setDefaultButton(default_button)
        return msgBox.exec_()

    def about(self):
        #QtWidgets.QMessageBox.about('''
        #self.message(u'''
        QtWidgets.QMessageBox.about(self.view.mainwindow, 'About GCA Analysis Tool...', '''
GCA Analysis Tool, v2.50 (free version)

Copyright © 2016-2019 Oscar Franzén <oscarfranzen@protonmail.com>

This is a free version of the GCA Analysis Tool. It is fully functional until 2019-12-31, but lacks all features but the most basic ones. It may be copied and used freely.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Software used:
Python ''' + platform.python_version() + ''', PSF License
PySide2 ''' + PySide2.__version__ + ''', LGPL version 2.1
Qt ''' + PySide2.QtCore.__version__ + ''', LGPL version 3
''')

