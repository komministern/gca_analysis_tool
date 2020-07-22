"""
    This file is part of GCA Analysis Tool.

    Copyright (C) 2020 Oscar Franzén <oscarfranzen@protonmail.com>

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
from presenter.mainwindow.mainwindowpresenter import MyMainWindowPresenter
from presenter.graphwindow.graphwindowpresenter import GraphWindowPresenter

class Presenter(QtCore.QObject):

    def __init__(self, model, app):
        super(Presenter, self).__init__()

        self.model = model
        self.app = app

        self.mainwindowpresenter = None
        self.graphwindowpresenters = []

        self.create_mainwindow_presenter()

    # Sub-presenters
    def create_mainwindow_presenter(self):
        self.mainwindowpresenter = MyMainWindowPresenter(self.model, self, self.app)
    
    def create_graphwindow_presenter(self, data):
        self.graphwindowpresenters.append(GraphWindowPresenter(self.model, self, data))

    def destroy_graphwindow_presenter(self, obj):
        self.graphwindowpresenters.remove(obj)
        del obj
