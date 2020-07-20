"""
    This file is part of GCA Analysis Tool.

    Copyright (C) 2016-2020  Oscar Franzén  oscarfranzen@protonmail.com

    GCA Analysis Tool is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    GCA Analysis Tool is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with GCA Analysis Tool. If not, see <https://www.gnu.org/licenses/>.

"""

import matplotlib
import numpy

import PySide2
import platform
from PySide2 import QtCore, QtGui, QtWidgets

from view.mainwindow.mymainwindow import MyMainWindow

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



class MyMainWindowPresenter(QtCore.QObject):

    def __init__(self, model, presenter, app):
        super(MyMainWindowPresenter, self).__init__()

        # Store view and model.
        self.model = model
        self.mainwindow = MyMainWindow()
        self.presenter = presenter
        self.app = app

        # Sub-presenters
        self.filterpresenter = FilterPresenter(self.model, self.mainwindow, self)
        self.textpresenter = TextPresenter(self.model, self.mainwindow, self)
        self.calendarpresenter = CalendarPresenter(self.model, self.mainwindow, self)
        self.searchpresenter = SearchPresenter(self.model, self.mainwindow, self)
        self.commentspresenter = CommentsPresenter(self.model, self.mainwindow, self)
        self.sitepresenter = SitePresenter(self.model, self.mainwindow, self)
        self.menupresenter = MenuPresenter(self.model, self.mainwindow, self)
        self.ignorepresenter = IgnorePresenter(self.model, self.mainwindow, self)
        self.analysispresenter = AnalysisPresenter(self.model, self.mainwindow, self)

        # Colors
        self.green = QtGui.QColor.fromRgbF(0.248478, 1.000000, 0.431632, 1.000000)
        self.red = QtGui.QColor.fromRgbF(1.000000, 0.343099, 0.419516, 1.000000)
        self.yellow = QtGui.QColor.fromRgbF(1.000000, 0.997757, 0.346044, 1.000000)
        self.blue = QtGui.QColor.fromRgbF(0.509743, 0.734401, 1.000000, 1.000000)

        self.mainwindow.progressBar.setMaximum(100)
        
        self.eventblocker = EventBlocker()
        self.app.installEventFilter(self.eventblocker)
        
        self.timer = QtCore.QTimer(self)

        self.connect_signals()

        self.menupresenter.update_menu()
        self.mainwindow.show()

        # This is to force people to use an updated version.
        #self.mainwindow.calendarWidget.setMaximumDate(QtCore.QDate(2019, 12, 31))

        
    def connect_signals(self):
        self.mainwindow.quit.connect(self.model.quit)

        self.mainwindow.calendarWidget.selectionChanged.connect(self.calendarpresenter.new_date_chosen)

        self.mainwindow.pushButton_NewFilter.clicked.connect(self.filterpresenter.new_filter)
        self.mainwindow.pushButton_EditFilter.clicked.connect(self.filterpresenter.edit_filter)
        self.mainwindow.pushButton_DeleteFilter.clicked.connect(self.filterpresenter.delete_filter)
        self.mainwindow.comboBox_ChooseFilter.currentIndexChanged.connect(self.filterpresenter.choose_filter)

        self.mainwindow.pushButton_CommitStringSearch.clicked.connect(self.searchpresenter.commit_string_search)
        self.mainwindow.pushButton_ResetStringSearch.clicked.connect(self.searchpresenter.reset_string_search)

        self.mainwindow.comboBox_ActiveSite.currentIndexChanged.connect(self.sitepresenter.set_active_site)
        
        self.mainwindow.comboBox_Coloring.currentIndexChanged.connect(self.calendarpresenter.set_coloring_scheme)

        self.mainwindow.importAction.triggered.connect(self.sitepresenter.import_capturesite)

        self.mainwindow.analysisAction.triggered.connect(self.analysispresenter.analyze)
        
        self.mainwindow.ignoreAction.triggered.connect(self.ignorepresenter.ignore_date)
        self.mainwindow.deIgnoreAction.triggered.connect(self.ignorepresenter.deignore_date)
        self.mainwindow.deIgnoreAllAction.triggered.connect(self.ignorepresenter.deignore_all_dates)
        self.mainwindow.nextIgnoredDateAction.triggered.connect(self.ignorepresenter.jump_to_next_ignored_date)
        
        self.mainwindow.aboutAction.triggered.connect(self.about)

        self.mainwindow.wrapAction.triggered.connect(self.textpresenter.set_wrap_mode)
        self.mainwindow.noWrapAction.triggered.connect(self.textpresenter.set_nowrap_mode)

        self.mainwindow.pushButton_FirstDate.clicked.connect(self.calendarpresenter.set_first_date)
        self.mainwindow.pushButton_LastDate.clicked.connect(self.calendarpresenter.set_last_date)
        self.mainwindow.pushButton_ActiveDate.clicked.connect(self.calendarpresenter.set_active_date)

        self.mainwindow.pushButton_NextSearch.clicked.connect(self.searchpresenter.set_next_search_date)
        self.mainwindow.pushButton_PreviousSearch.clicked.connect(self.searchpresenter.set_previous_search_date)

        self.mainwindow.plainTextEdit_StringSearch.textChanged.connect(self.searchpresenter.text_changed)
        self.mainwindow.plainTextEdit_StringSearch.returnPressed.connect(self.searchpresenter.return_pressed)

        self.mainwindow.pushButton_SaveComment.clicked.connect(self.commentspresenter.save_comment)
        self.mainwindow.pushButton_DeleteComment.clicked.connect(self.commentspresenter.delete_comment)

        self.mainwindow.pushButton_NextComment.clicked.connect(self.commentspresenter.set_next_comment_date)
        self.mainwindow.pushButton_PreviousComment.clicked.connect(self.commentspresenter.set_previous_comment_date)

        self.model.io_progress.connect(self.update_progressbar)



    # Helper methods and properties

    # TEXTPRESENTER
    def update_text(self):
        self.textpresenter.update_text()


    # MENUPRESENTER
    def update_menu(self):
        self.menupresenter.update_menu()


    # CALENDARPRESENTER
    def update_calendar(self):
        self.calendarpresenter.update_calendar()

    def update_calendar_cells(self):
        self.calendarpresenter.update_calendar_cells()
    
    def colored_dates(self, site_name):
        return self.calendarpresenter.colored_dates(site_name)
    
    def set_comment_dates(self, dates):
        self.calendarpresenter.set_comment_dates(dates)
    
    def set_search_hit_dates(self, dates):
        self.calendarpresenter.set_search_hit_dates(dates)
    
    @property
    def selected_date(self):
        return self.calendarpresenter.selected_date

    @selected_date.setter
    def selected_date(self, date):
        self.calendarpresenter.selected_date = date


    # COMMENTSPRESENTER
    def update_comment(self):
        self.commentspresenter.update_comment()


    # SEARCHPRESENTER
    def commit_string_search(self):
        self.searchpresenter.commit_string_search()

    @property
    def string_to_highlight(self):
        return self.searchpresenter.string_to_highlight


    # FILTERPRESENTER
    def filtered_text(self, atext):
        return self.filterpresenter.format_text(atext)


    # SITEPRESENTER
    @property
    def presentation_dict(self):
        return self.sitepresenter.presentation_dict

    def reload_active_site(self):
        self.sitepresenter.reload_active_site()

    @property
    def active_site_name(self):                         
        return self.sitepresenter.active_site_name


    # Misc methods who do not fit into any of the sub-presenters
    def update_progressbar(self, progress):
        self.mainwindow.progressBar.setValue(progress)
        QtGui.qApp.processEvents()
        if progress >= 100:
            if not self.timer.isActive():
                # Some delay, just for the feeling
                self.timer.singleShot(100, self.zero_progressbar)
            
    def zero_progressbar(self):
        if self.mainwindow.progressBar.value() == 100:
            self.mainwindow.progressBar.setValue(0)
        
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
        msgBox = QtWidgets.QMessageBox(parent=self.mainwindow)
        msgBox.setText(text)
        if title_text:
            msgBox.setWindowTitle(title_text)
        msgBox.exec_()
        
    def message_with_cancel_choice(self, text, informative_text, default_button):
        msgBox = QtWidgets.QMessageBox(parent=self.mainwindow)
        msgBox.setText(text)
        msgBox.setInformativeText(informative_text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok)
        msgBox.setDefaultButton(default_button)
        return msgBox.exec_()

    def about(self):
        QtWidgets.QMessageBox.about(self.mainwindow, 'About GCA Analysis Tool...', '''

GCA Analysis Tool, v3.20, a simple toot for inspecting GCA history logs.
    
Copyright (C) 2016-2020 Oscar Franzén

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

Software used:
Python ''' + platform.python_version() + '''
PySide2 ''' + PySide2.__version__ + '''
Qt ''' + PySide2.QtCore.__version__ + '''
Matplotlib ''' + matplotlib.__version__ + '''
Numpy ''' + numpy.__version__ )

