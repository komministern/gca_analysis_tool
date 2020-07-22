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

class MyStringSearchPlainTextEdit(QtWidgets.QPlainTextEdit):

    textEdited = QtCore.Signal()
    returnPressed = QtCore.Signal()

    def __init__(self, *args, **kwargs):
        super(MyStringSearchPlainTextEdit, self).__init__(*args, **kwargs)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.returnPressed.emit()
            event.accept()
        else:
            super(MyStringSearchPlainTextEdit, self).keyPressEvent(event)