# -*- coding: utf-8 -*-

#    Copyright � 2016, 2017, 2018 Oscar Franz�n <oscarfranzen@protonmail.com>
#
#    This file is part of GCA Analysis Tool.



from PySide2 import QtGui, QtCore, QtWidgets
from view.ui_analysisdialog import Ui_Dialog
#from presenter.filtercontainer import Filter

class MyAnalysisDialog(QtWidgets.QDialog, Ui_Dialog):

#    quit = QtCore.Signal()

    def __init__(self, parent=None):
        super(MyAnalysisDialog, self).__init__(parent)
        
        # This really is not nice. Font size is set with pixel in view.
        font = parent.font()
        self.setFont(font)

        self.setupUi(self)

        self.pushButton_Go.pressed.connect(self.go)

    
    def go(self):
        print('GO!!!!!!!!!!!!!!')
        self.accept()



    def message(self, text):
        msgBox = QtGui.QMessageBox(parent=self)
        msgBox.setText(text)
        msgBox.exec_()
        
    def message_with_cancel_choice(self, text, informative_text, default_button):
        msgBox = QtGui.QMessageBox(parent=self)
        msgBox.setText(text)
        msgBox.setInformativeText(informative_text)
        msgBox.setStandardButtons(QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Ok)
        msgBox.setDefaultButton(default_button)
        return msgBox.exec_()
