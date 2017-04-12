#!/usr/bin/env python
# -*- coding: utf-8 -*-


#    Copyright © 2016, 2017 Oscar Franzén <oscarfranzen@yahoo.se>
#
#    This file is part of GCA Analysis Tool.


from PySide import QtGui, QtCore
#from ui_filterdialog import Ui_Dialog
#from presenter.filtercontainer import Filter

class MyPlainTextEdit(QtGui.QPlainTextEdit):
    
    def __init__(self, *args, **kwargs):
        super(MyPlainTextEdit, self).__init__(*args, **kwargs)
        
        self.setReadOnly(True)

        self.chosen_index = None

        self.blue = QtGui.QColor.fromRgbF(0.509743, 0.734401, 1.000000, 1.000000)
        self.white = QtGui.QColor.fromRgbF(1.000000, 1.000000, 1.000000, 1.000000)

        self.last_block_begin = None
        self.last_block_lenght = None
        
        self.blue_format = QtGui.QTextCharFormat()
        self.blue_format.setBackground(QtGui.QBrush(self.blue))
        
        self.white_format = QtGui.QTextCharFormat()
        self.white_format.setBackground(QtGui.QBrush(self.white))


    def mousePressEvent(self, e):
        
        super(MyPlainTextEdit, self).mousePressEvent(e)

        cursor = self.textCursor()
        block_number = cursor.blockNumber()
        
        if self.toPlainText() != u'':
            self.chosen_index = block_number
        else:
            self.chosen_index = None
        
        print self.chosen_index
        
        self.paint_block(block_number)
        
        
    def paint_block(self, block_number):
        
        cursor = self.textCursor()
        
        block = self.document().findBlockByLineNumber(block_number)
        
        block_begin = block.position()
        block_length = block.length()

        if self.last_block_begin != None:
            cursor.setPosition(self.last_block_begin)
            cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, self.last_block_length)
            cursor.mergeCharFormat(self.white_format)

        cursor.setPosition(block_begin)
        cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, block_length)
        cursor.mergeCharFormat(self.blue_format)

        self.last_block_begin = block_begin
        self.last_block_length = block_length


    def setPlainText(self, string):
        super(MyPlainTextEdit, self).setPlainText(string)
        
        if len(string) > 0:
            self.chosen_index = 0
            self.paint_block(0)
        else:
            self.chosen_index = None
            
        print self.chosen_index
        