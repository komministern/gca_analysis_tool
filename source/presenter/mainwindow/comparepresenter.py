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

class ComparePresenter(QtCore.QObject):

    def __init__(self, model, mainwindow, mainwindowpresenter):
        super(ComparePresenter, self).__init__()
        self.model = model
        self.mainwindow = mainwindow
        self.mainwindowpresenter = mainwindowpresenter



    def compare(self):

        old_compression_format_present = False
        
        capturesite_1_filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.mainwindow, u'Choose first capturesite file to compare', self.model.database.home_directory, u'Capturesite (*tar.gz *TAR.Z)')

        if capturesite_1_filename:
            capturesite_2_filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.mainwindow, u'Choose second capturesite file to compare', self.model.database.home_directory, u'Capturesite (*tar.gz *TAR.Z)')

            if capturesite_2_filename:

                print(capturesite_1_filename)
                print(capturesite_2_filename)

                if capturesite_1_filename[-2:] == '.Z' or capturesite_2_filename[-2:] == '.Z':
            
                    old_compression_format_present = True

                    if not self.model.database.exist_7z():
                        self.mainwindowpresenter.message(u'To decompress one of these Capturesite files, the application 7z needs to be installed. Either this is not the case, or it is installed in a non default location. Please enter the location of the file 7z.exe.')

                        path_to_7z, _ = QtWidgets.QFileDialog.getOpenFileName(self.mainwindow, u'Path to 7z.exe', self.model.database.home_directory, u'7z console application (7z.exe)')
                        self.model.database.set_path_to_7z(path_to_7z)



                if (not old_compression_format_present) or (old_compression_format_present and self.model.database.exist_7z()):

                    self.mainwindowpresenter.inhibit_mouseclicks()

                    self.model.create_temp_site(capturesite_1_filename)
                    # self.model.database.read_site_to_memory(site_name)

                    # comparison_data = self.model.get_comparison(capturesite_1_filename, capturesite_2_filename)

                    self.mainwindowpresenter.allow_mouseclicks()

                    # self.mainwindowpresenter.presenter.create_comparisonwindow_presenter(comparison_data)


        


        
        
        # active_site_name = self.mainwindowpresenter.active_site_name

        # self.mainwindowpresenter.inhibit_mouseclicks()

        # collected_data = self.model.get_analysis(active_site_name, self.model.get_first_entry_date(active_site_name), self.model.get_last_entry_date(active_site_name))

        # self.mainwindowpresenter.allow_mouseclicks()

        # self.mainwindowpresenter.presenter.create_graphwindow_presenter(collected_data)

