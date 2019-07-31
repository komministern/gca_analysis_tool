#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright � 2016, 2017, 2018 Oscar Franz�n <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.


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