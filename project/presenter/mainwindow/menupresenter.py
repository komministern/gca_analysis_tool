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


from PySide2 import QtCore, QtGui, QtWidgets


class MenuPresenter(QtCore.QObject):

    def __init__(self, model, mainwindow, mainwindowpresenter):
        super(MenuPresenter, self).__init__()
        self.model = model
        self.mainwindow = mainwindow
        self.mainwindowpresenter = mainwindowpresenter

        self.mainwindow.noWrapAction.setCheckable(True)
        self.mainwindow.wrapAction.setCheckable(True)
        self.mainwindow.noWrapAction.setChecked(True)


    def update_menu(self):
        
        if self.mainwindowpresenter.active_site_name == u'':

            self.mainwindow.ignoreAction.setEnabled(False)
            self.mainwindow.deIgnoreAction.setEnabled(False)
            self.mainwindow.deIgnoreAllAction.setEnabled(False)
            self.mainwindow.nextIgnoredDateAction.setEnabled(False)

            self.mainwindow.analysisAction.setEnabled(False)

        else:

            self.mainwindow.analysisAction.setEnabled(True)

            if self.mainwindowpresenter.selected_date not in self.model.get_ignored_dates(self.mainwindowpresenter.active_site_name):

                self.mainwindow.deIgnoreAction.setEnabled(False)
                
                text = self.model.get_historylog(self.mainwindowpresenter.active_site_name, self.mainwindowpresenter.selected_date)
                if text != 'No history log exists for this date.':
                    self.mainwindow.ignoreAction.setEnabled(True)

            else:
                self.mainwindow.ignoreAction.setEnabled(False)
                self.mainwindow.deIgnoreAction.setEnabled(True)


            if len(self.model.get_ignored_dates(self.mainwindowpresenter.active_site_name)) > 0:
                self.mainwindow.deIgnoreAllAction.setEnabled(True)
                self.mainwindow.nextIgnoredDateAction.setEnabled(True)
            else:
                self.mainwindow.deIgnoreAllAction.setEnabled(False)
                self.mainwindow.nextIgnoredDateAction.setEnabled(False)

