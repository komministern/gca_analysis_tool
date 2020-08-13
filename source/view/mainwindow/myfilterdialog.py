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



from PySide2 import QtGui, QtCore, QtWidgets
from ...view.ui.ui_filterdialog import Ui_Dialog
from ...presenter.mainwindow.localresources.filtercontainer import Filter

class MyFilterDialog(QtWidgets.QDialog, Ui_Dialog):

#    quit = QtCore.Signal()

    def __init__(self, initial_filter, name_editable = True, parent=None):
        super(MyFilterDialog, self).__init__(parent)
        
        # This really is not nice. Font size is set with pixel in view.
        font = parent.font()
        self.setFont(font)
        
        self.setupUi(self)

        self.possible_identifiers = [u'(00)', u'(01)', u'(02)', u'(03)', u'(04)',
                                     u'(05)', u'(06)', u'(07)', u'(08)', u'(09)',
                                     u'(0a)', u'(0b)', u'(0c)', u'(0d)', u'(0e)',
                                     u'(0f)', u'(10)', u'(11)', u'(12)', u'(13)',
                                     u'(14)', u'(15)', u'(16)', u'(17)', u'(18)',
                                     u'(19)', u'(1a)', u'(1b)', u'(1c)', u'(1d)',
                                     u'(1e)', u'(1f)', u'(20)', u'(21)', u'(22)',
                                     u'(23)', u'(24)']
                                     
        self.identifiers_explaining_text = {u'(00)': u'Radar Still On',
                                            u'(03)': u'Minutes Normal/Degr/Fault',
                                            u'(04)': u'Minutes Antenna Drive On',
                                            u'(05)': u'Transmitter On',
                                            u'(07)': u'Minutes per Radar Mode',
                                            u'(08)': u'Minutes SSR On',
                                            u'(09)': u'Minutes Maint Mode',
                                            u'(10)': u'Maintenance Mode On/Off',
                                            u'(11)': u'Runway Selection',
                                            u'(12)': u'Minutes System Off',
                                            u'(13)': u'Fault Condition',
                                            u'(14)': u'Fault Details',
                                            u'(15)': u'Further Fault Details',
                                            u'(16)': u'New Fault/Degr Count',
                                            u'(17)': u'Active Fault/Degr Count',
                                            u'(1a)': u'Weather Mode',
                                            u'(1b)': u'Antenna Tilt',
                                            u'(1e)': u'MTI Deviation Delta',
                                            u'(23)': u'Temperature/Auto-Test',
                                            u'(24)': u'Heater Control'}

        if not name_editable:
            self.lineEdit_FilterName.setEnabled(False)
        
        self.filter = initial_filter

        self.lineEdit_FilterName.setText(self.filter.name)

        self.plainTextEdit_FilterContent.setItems(self.filter.content, self.identifiers_explaining_text)
                                     
        self.plainTextEdit_PossibleContent.setItems(self.possible_identifiers, self.identifiers_explaining_text)

        self.filter_states = [u'Suppress', u'Show']
        self.comboBox_FilterState.addItems(self.filter_states)
        self.comboBox_FilterState.setCurrentIndex(self.filter.state)

        self.comboBox_FilterState.currentIndexChanged.connect(self.set_state)

        self.pushButton_Save.pressed.connect(self.validate_filter)
        self.pushButton_Cancel.pressed.connect(self.cancel_filter)
        
        self.pushButton_AddContent.pressed.connect(self.add_content)
        self.pushButton_RemoveContent.pressed.connect(self.remove_content)

        self.plainTextEdit_PossibleContent.doubleClicked.connect(self.add_content)
        self.plainTextEdit_FilterContent.doubleClicked.connect(self.remove_content)

  

    
    def set_state(self, index):
        self.filter.state = index
        

    def add_content(self):
        chosen_identifier_index = self.plainTextEdit_PossibleContent.chosen_index
        if self.possible_identifiers[chosen_identifier_index] not in self.filter.content:
            self.filter.content.append(self.possible_identifiers[chosen_identifier_index])
            self.filter.content.sort()
            index_to_highlight = self.filter.content.index(self.possible_identifiers[chosen_identifier_index])
            self.plainTextEdit_FilterContent.setItems(self.filter.content, self.identifiers_explaining_text, index_to_highlight)


    def remove_content(self):
        chosen_content_index = self.plainTextEdit_FilterContent.chosen_index
        if chosen_content_index != None:
            del self.filter.content[chosen_content_index]
            self.plainTextEdit_FilterContent.setItems(self.filter.content, self.identifiers_explaining_text)


    def get_final_filter(self):
        return self.filter


    def validate_filter(self):
        self.filter.name = self.lineEdit_FilterName.text()
        if self.filter.name == u'':
            self.message(u'You must name the filter to save it.')
        elif self.filter.content == []:
            self.message(u'Filter content is empty.')
        else:
            self.accept()


    def cancel_filter(self):
        self.reject()


    def message(self, text):
        msgBox = QtWidgets.QMessageBox(parent=self)
        msgBox.setText(text)
        msgBox.exec_()
        
    def message_with_cancel_choice(self, text, informative_text, default_button):
        msgBox = QtWidgets.QMessageBox(parent=self)
        msgBox.setText(text)
        msgBox.setInformativeText(informative_text)
        msgBox.setStandardButtons(QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Ok)
        msgBox.setDefaultButton(default_button)
        return msgBox.exec_()
