#!/usr/bin/env python
# -*- coding: utf-8 -*-


#    Copyright � 2016, 2017 Oscar Franz�n <oscarfranzen@yahoo.se>
#
#    This file is part of GCA Analysis Tool.


from PySide import QtGui, QtCore
#from ui_filterdialog import Ui_Dialog
#from presenter.filtercontainer import Filter

class MyPlainTextEdit(QtGui.QPlainTextEdit):
    
    def __init__(self, *args, **kwargs):
        super(MyPlainTextEdit, self).__init__(*args, **kwargs)
        
        #self.setCursor(QtCore.Qt.ArrowCursor)
        self.setReadOnly(True)
        self.viewport().setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        self.chosen_index = None

        self.blue = QtGui.QColor.fromRgbF(0.509743, 0.734401, 1.000000, 1.000000)
        self.white = QtGui.QColor.fromRgbF(1.000000, 1.000000, 1.000000, 1.000000)

        self.last_block_begin = None
        self.last_block_lenght = None
        
        self.blue_format = QtGui.QTextCharFormat()
        self.blue_format.setBackground(QtGui.QBrush(self.blue))
        
        self.white_format = QtGui.QTextCharFormat()
        self.white_format.setBackground(QtGui.QBrush(self.white))


    def setItems(self, list_of_strings, dict_of_strings = {}, highlighted_index = 0):
        string = '\n'.join(list_of_strings)
        self.setPlainText(string)
        
        if len(string) > 0:
            self.chosen_index = highlighted_index
            self.highlight_block(self.chosen_index)
        else:
            self.chosen_index = None
        
        
    def highlight_block(self, block_number):
        for each in range(self.blockCount()):
            self.paint_block(each, self.white_format)
        self.paint_block(block_number, self.blue_format)
        

    def paint_block(self, block_number, char_format):
        cursor = self.textCursor()
        block = self.document().findBlockByLineNumber(block_number)

        block_begin = block.position()
        block_length = block.length()

        cursor.setPosition(block_begin)
        cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, block_length)
        cursor.mergeCharFormat(char_format)


    def mousePressEvent(self, e):
        
        super(MyPlainTextEdit, self).mousePressEvent(e)

        cursor = self.textCursor()
        block_number = cursor.blockNumber()
        
        if self.toPlainText() != u'':
            self.chosen_index = block_number
        else:
            self.chosen_index = None
        
        self.highlight_block(block_number)
        