#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.

import PySide2
import platform
from PySide2 import QtCore, QtGui, QtWidgets

from presenter.eventfilter import EventBlocker

from presenter.filterpresenter import FilterPresenter
from presenter.commentspresenter import CommentsPresenter
from presenter.sitepresenter import SitePresenter
from presenter.textpresenter import TextPresenter
from presenter.calendarpresenter import CalendarPresenter
from presenter.searchpresenter import SearchPresenter
from presenter.menupresenter import MenuPresenter
from presenter.ignorepresenter import IgnorePresenter
from presenter.analysispresenter import AnalysisPresenter


class MyPresenter(QtCore.QObject):

    def __init__(self, model, view, app, **kwds):
        super(MyPresenter, self).__init__(**kwds)

        # Store view and model.
        self.model = model
        self.view = view
        self.app = app

        # Sub-presenters
        self.filter_presenter = FilterPresenter(model, view, self)
        self.text_presenter = TextPresenter(model, view, self)
        self.calendar_presenter = CalendarPresenter(model, view, self)
        self.search_presenter = SearchPresenter(model, view, self)
        self.comments_presenter = CommentsPresenter(model, view, self)
        self.site_presenter = SitePresenter(model, view, self)
        self.menu_presenter = MenuPresenter(model, view, self)
        self.ignore_presenter = IgnorePresenter(model, view, self)
        self.analysis_presenter = AnalysisPresenter(model, view, self)

        # Colors
        self.green = QtGui.QColor.fromRgbF(0.248478, 1.000000, 0.431632, 1.000000)
        self.red = QtGui.QColor.fromRgbF(1.000000, 0.343099, 0.419516, 1.000000)
        self.yellow = QtGui.QColor.fromRgbF(1.000000, 0.997757, 0.346044, 1.000000)
        self.blue = QtGui.QColor.fromRgbF(0.509743, 0.734401, 1.000000, 1.000000)

        self.view.progressBar.setMaximum(100)
        
        self.eventblocker = EventBlocker()
        self.app.installEventFilter(self.eventblocker)
        
        self.timer = QtCore.QTimer(self)

        self.connect_signals()


        #Block stuff

        #self.view.comboBox_Coloring.model().item(1).setEnabled(False)
        #self.view.comboBox_Coloring.model().item(2).setEnabled(False)
        #self.view.comboBox_Coloring.model().item(3).setEnabled(False)
        #self.view.comboBox_Coloring.model().item(4).setEnabled(False)

        self.view.calendarWidget.setMaximumDate(QtCore.QDate(2019, 12, 31))



    def connect_signals(self):
        self.view.quit.connect(self.model.quit)

        self.view.calendarWidget.selectionChanged.connect(self.calendar_presenter.new_date_chosen)

        self.view.pushButton_NewFilter.clicked.connect(self.filter_presenter.new_filter)
        self.view.pushButton_EditFilter.clicked.connect(self.filter_presenter.edit_filter)
        self.view.pushButton_DeleteFilter.clicked.connect(self.filter_presenter.delete_filter)
        self.view.comboBox_ChooseFilter.currentIndexChanged.connect(self.filter_presenter.choose_filter)

        self.view.pushButton_CommitStringSearch.clicked.connect(self.search_presenter.commit_string_search)
        self.view.pushButton_ResetStringSearch.clicked.connect(self.search_presenter.reset_string_search)

        self.view.comboBox_ActiveSite.currentIndexChanged.connect(self.site_presenter.set_active_site)
        
        self.view.comboBox_Coloring.currentIndexChanged.connect(self.calendar_presenter.set_coloring_scheme)

        self.view.importAction.triggered.connect(self.site_presenter.import_capturesite)

        self.view.analysisAction.triggered.connect(self.analysis_presenter.show_analysis_dialog)
        
        self.view.ignoreAction.triggered.connect(self.ignore_presenter.ignore_date)
        self.view.deIgnoreAction.triggered.connect(self.ignore_presenter.deignore_all_dates)
        
        self.view.aboutAction.triggered.connect(self.about)

        self.view.pushButton_FirstDate.clicked.connect(self.calendar_presenter.set_first_date)
        self.view.pushButton_LastDate.clicked.connect(self.calendar_presenter.set_last_date)
        self.view.pushButton_ActiveDate.clicked.connect(self.calendar_presenter.set_active_date)

        self.view.pushButton_NextSearch.clicked.connect(self.search_presenter.set_next_search_date)
        self.view.pushButton_PreviousSearch.clicked.connect(self.search_presenter.set_previous_search_date)

        self.view.plainTextEdit_StringSearch.textChanged.connect(self.search_presenter.text_changed)
        self.view.plainTextEdit_StringSearch.returnPressed.connect(self.search_presenter.return_pressed)

        self.view.pushButton_SaveComment.clicked.connect(self.comments_presenter.save_comment)
        self.view.pushButton_DeleteComment.clicked.connect(self.comments_presenter.delete_comment)

        self.view.pushButton_NextComment.clicked.connect(self.comments_presenter.set_next_comment_date)
        self.view.pushButton_PreviousComment.clicked.connect(self.comments_presenter.set_previous_comment_date)

        self.model.io_progress.connect(self.update_progressbar)



    # Helper methods
    def update_text(self):
        self.text_presenter.update_text()

    def update_menu(self):
        self.menu_presenter.update_menu()

    def update_calendar(self):
        self.calendar_presenter.update_calendar()

    def update_comment(self):
        self.comments_presenter.update_comment()

    def colored_dates(self, site_name):
        return self.calendar_presenter.colored_dates(site_name)

    def commit_string_search(self):
        self.search_presenter.commit_string_search()

    def format_text(self, atext):
        return self.filter_presenter.format_text(atext)

    @property
    def highlight(self):
        return self.search_presenter.highlight

    @property
    def presentation_dict(self):
        return self.site_presenter.presentation_dict

    def set_active_site(self, index):
        self.site_presenter.set_active_site(index)

    @property
    def active_site_name(self):
        return self.site_presenter.active_site_name

    @active_site_name.setter
    def active_site_name(self, site_name):
        self.site_presenter.active_site_name = site_name


    # Misc methods who do not fit into any of the sub-presenters
    def update_progressbar(self, progress):
        self.view.progressBar.setValue(progress)
        QtGui.qApp.processEvents()
        if progress >= 100:
            if not self.timer.isActive():
                # Some delay, just for the feeling
                self.timer.singleShot(100, self.zero_progressbar)
            
    def zero_progressbar(self):
        if self.view.progressBar.value() == 100:
            self.view.progressBar.setValue(0)
        
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
        msgBox = QtWidgets.QMessageBox(parent=self.view)
        msgBox.setText(text)
        if title_text:
            msgBox.setWindowTitle(title_text)
        msgBox.exec_()
        
    def message_with_cancel_choice(self, text, informative_text, default_button):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setInformativeText(informative_text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok)
        msgBox.setDefaultButton(default_button)
        return msgBox.exec_()

    def about(self):
        self.message(u'''
GCA Analysis Tool, v2.50 (free version)

Copyright © 2016, 2017, 2018 Oscar Franzén <oscarfranzen@protonmail.com>

This is a free version of the GCA Analysis Tool. It is fully functional until 2019-12-31, but lacks all features but the most basic ones. It may be copied and used freely.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Software used:
Python ''' + platform.python_version() + ''', PSF License
PySide2 ''' + PySide2.__version__ + ''', LGPL version 2.1
Qt ''' + PySide2.QtCore.__version__ + ''', LGPL version 3
''', u'About GCA Analysis Tool')

