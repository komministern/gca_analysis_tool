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

class AnalysisPresenter(QtCore.QObject):

    def __init__(self, model, mainwindow, mainwindowpresenter):
        super(AnalysisPresenter, self).__init__()
        self.model = model
        self.mainwindow = mainwindow
        self.mainwindowpresenter = mainwindowpresenter



    def analyze(self):
        active_site_name = self.mainwindowpresenter.active_site_name

        self.mainwindowpresenter.inhibit_mouseclicks()

        collected_data = self.model.get_analysis(active_site_name, self.model.get_first_entry_date(active_site_name), self.model.get_last_entry_date(active_site_name))

        self.mainwindowpresenter.allow_mouseclicks()

        self.mainwindowpresenter.presenter.create_graphwindow_presenter(collected_data)

